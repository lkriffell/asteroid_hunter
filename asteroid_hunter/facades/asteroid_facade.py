from asteroid_hunter.services.asteroid_service import AsteroidService
import json
from calendar import monthrange
import datetime

class AsteroidFacade:  
  def closest_approaches(result_size):
    page = 0
    closest_misses = []
    asteroid_data = AsteroidService.browse_neos_by_page(page).json()
    # Commented out so cassette doesn't record 'Request limit reached'
    # total_pages = asteroid_data['page']['total_pages']
    # while page <= total_pages:
    while page <= 200:
      AsteroidFacade.order_closest_misses(asteroid_data['near_earth_objects'], closest_misses, result_size)
      page += 1
      asteroid_data = AsteroidService.browse_neos_by_page(page).json()
    if result_size > 1:
      return AsteroidFacade.gather_asteroids(closest_misses[0 : result_size])
    else:
      return AsteroidFacade.gather_asteroids(closest_misses)[0]

  def order_closest_misses(asteroid_data, closest_misses, result_size):
    for asteroid in asteroid_data:
      for close_approach in asteroid['close_approach_data']:
        close_approach = {'asteroid': asteroid, 'close_approach_data': close_approach.copy()}
        closest_misses.append(close_approach)
    return closest_misses.sort(key=lambda x: x['close_approach_data']['miss_distance']['astronomical'])

  def gather_asteroids(closest_misses):
    results = []
    for miss in closest_misses:
      asteroid = miss['asteroid']
      asteroid['close_approach_data'] = miss['close_approach_data']
      results.append(asteroid)
    return results

# ---------------------------------------

  def closest_approaches_by_month(result_size, year, month):
    finished = False
    day = 1
    closest_approaches = []
    total_days = monthrange(year, month)[-1]
    while finished == False:
      start_date = datetime.date(year, month, day)
      day = AsteroidFacade.add_days_to_date(start_date, total_days)
      end_date = datetime.date(year, month, day)
      asteroid_data = AsteroidService.asteroid_approaches_by_week(start_date, end_date).json()
      closest_approaches = AsteroidFacade.sort_closest_approaches_by_month(asteroid_data['near_earth_objects'], closest_approaches, start_date, month)
      if day == total_days : finished = True
    return {
            'closest_approaches': closest_approaches[0 : result_size], 
            'element_count': len(closest_approaches)
            }

  def sort_closest_approaches_by_month(asteroid_data, closest_approaches, date, month):
    for day in range (0, 7):
      if date.month == month:
        for asteroid in asteroid_data[date.strftime("%Y-%m-%d")]:
          closest_approaches.append(asteroid)
          closest_approaches.sort(key=lambda x: x['close_approach_data'][0]['miss_distance']['astronomical'])
        date += datetime.timedelta(1)
    return closest_approaches

  def add_days_to_date(date, total_days):
    if (date.day + 7) > total_days:
      return total_days
    else:
      return date.day + 7