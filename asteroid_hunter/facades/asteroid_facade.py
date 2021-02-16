from asteroid_hunter.services.asteroid_service import AsteroidService
import json
from pprint import pprint
import datetime

class AsteroidFacade:  
  def nearest_misses(result_size = 10):
    page = 0
    closest_misses = []
    asteroid_data = AsteroidService.browse_neos_by_page(page).json()
    # total_pages = asteroid_data['page']['total_pages']
    # while page <= total_pages:
    while page <= 50:
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
        close_approach = {'id': asteroid['id'], 'close_approach_data': close_approach.copy()}
        closest_misses.append(close_approach)
    return closest_misses.sort(key=lambda x: x['close_approach_data']['miss_distance']['astronomical'])

  def gather_asteroids(closest_misses):
    results = []
    for miss in closest_misses:
      asteroid = AsteroidService.asteroid_by_id(miss['id']).json()
      asteroid['close_approach_data'].sort(key=lambda x: x['miss_distance']['astronomical'])
      asteroid['close_approach_data'] = asteroid['close_approach_data'][0]
      results.append(asteroid)
    return results
      

# ---------------------------------------
  def close_approaches_by_month(result_size, year, month):
    finished = False
    day = 1
    closest_approaches = []
    calendar = AsteroidFacade.calendar(year)
    while finished == False:
      start_date = datetime.date(year, month, day)
      day = AsteroidFacade.add_days_to_date(start_date, calendar)
      end_date = datetime.date(year, month, day)
      asteroid_data = AsteroidFacade.get_asteroid_data_by_date(start_date, end_date)
      closest_approaches = AsteroidFacade.find_and_sort_closest_approaches(asteroid_data['near_earth_objects'], closest_approaches, start_date, month)
      if day == calendar[month] : finished = True
    element_count = len(closest_approaches)
    result = {
              'closest_approaches': closest_approaches[0 : result_size], 
              'element_count': element_count
              }
    return result

# helpers for close_approaches_by_month()
  def get_asteroid_data_by_date(start_date, end_date):
    return AsteroidService.asteroid_approaches_by_week(start_date, end_date).json()

  def find_and_sort_closest_approaches(asteroid_data, closest_approaches, date, month):
    for day in range (0, 7):
      if date.month == month:
        for asteroid in asteroid_data[date.strftime("%Y-%m-%d")]:
          closest_approaches.append(asteroid)
          closest_approaches.sort(key=lambda x: x['close_approach_data'][0]['miss_distance']['astronomical'])
        date += datetime.timedelta(1)
    return closest_approaches

  def calendar(year):
    calendar = {
                1: 31,
                2: 28,
                3: 31,
                4: 30,
                5: 31,
                5: 31,
                6: 30,
                7: 31,
                8: 31,
                9: 30,
                10: 31,
                11: 30,
                12: 31
                }
    if (year % 4) == 0 : calendar[2] = 29
    return calendar

  def add_days_to_date(date, calendar):
    if (date.day + 7) > calendar[date.month]:
      return calendar[date.month]
    else:
      return date.day + 7
#----------------------------------------