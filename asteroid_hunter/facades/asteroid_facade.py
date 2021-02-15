from asteroid_hunter.services.asteroid_service import AsteroidService
import json
from pprint import pprint
import datetime

class AsteroidFacade:
  def closest_approach_id():
    page = 0
    asteroid_data = AsteroidFacade.get_asteroid_data_by_page(page)
    closest_approach = asteroid_data[0]
    # while asteroid_data != []:
    while page < 230:
      asteroid_data = AsteroidFacade.get_asteroid_data_by_page(page)
      page += 1
      for asteroid in asteroid_data:
        closest_approach = AsteroidFacade.look_for_closer_approach(asteroid, closest_approach)
    return closest_approach['id']

  # helpers for closest_approach_id()
  def get_asteroid_data_by_page(page):
    return AsteroidService.browse_neos(page).json()['near_earth_objects']

  def look_for_closer_approach(asteroid, closest_approach):
    # Changes the closest approach if any of this asteroid's approaches were closer
    for close_approach in asteroid['close_approach_data']:
      if (close_approach != []
          and close_approach['miss_distance']['astronomical'] < closest_approach['close_approach_data'][0]['miss_distance']['astronomical']):
        closest_approach = asteroid
    return closest_approach
  # --------------------------------

  def close_approaches_by_month(result_size, year, month):
    finished = False
    day = 1
    calendar = AsteroidFacade.calendar(year)
    closest_approaches = []
    while finished == False:
      start_date = datetime.date(year, month, day)
      day = AsteroidFacade.add_a_week_to_day(month, day, calendar)
      end_date = datetime.date(year, month, day)
      asteroid_data = AsteroidFacade.get_asteroid_data_by_date(start_date, end_date)
      AsteroidFacade.find_and_sort_closest_approaches(asteroid_data, closest_approaches, start_date)
      if day == calendar[month] : finished = True
    return closest_approaches[0 : result_size]

  # helpers for close_approaches_by_month()
  def get_asteroid_data_by_date(start_date, end_date):
    return AsteroidService.asteroid_approaches_by_week(start_date, end_date).json()['near_earth_objects']

  def find_and_sort_closest_approaches(asteroid_data, closest_approaches, date):
    for day in range (0, 7):
      for asteroid in asteroid_data[date.strftime("%Y-%m-%d")]:
        closest_approaches.append(asteroid)
        closest_approaches.sort(key=lambda x: x['close_approach_data'][0]['miss_distance']['astronomical'])
        # This next line would work properly but when I try to return the final list it would cut the list to 5 elements no matter what
        # closest_approaches = closest_approaches[0 : result_size]
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
                12: 31,
                }
    if (year % 4) == 0 : calendar[2] = 29
    return calendar

  def add_a_week_to_day(month, day, calendar):
    if (day + 6) > calendar[month]:
      return calendar[month]
    else:
      return day + 6
  #----------------------------------------
  
  def asteroid_by_id(id):
    return AsteroidService.asteroid_by_id(id)