from asteroid_hunter.services.asteroid_service import AsteroidService
import json

class AsteroidFacade:
  def closest_approach_id():
    page = 0
    approach_data = AsteroidFacade.get_approach_data_by_page(page)
    closest_approach = approach_data[0]
    # while approach_data != []:
    while page < 230:
      approach_data = AsteroidFacade.get_approach_data_by_page(page)
      page += 1
      for asteroid in approach_data:
        closest_approach = AsteroidFacade.consider_all_approaches(asteroid, closest_approach)
    return closest_approach['id']

  
  def asteroid_by_id(id):
    return AsteroidService.asteroid_by_id(id).json()

  # helpers
  
  def get_approach_data_by_page(page):
    return AsteroidService.browse_neos(page).json()['near_earth_objects']

  def consider_all_approaches(asteroid, closest_approach):
    # Changes the closest approach if any of this asteroids approache's were closer
    for close_approach in asteroid['close_approach_data']:
      if (close_approach != []
          and close_approach['miss_distance']['astronomical'] < closest_approach['close_approach_data'][0]['miss_distance']['astronomical']):
        closest_approach = asteroid
    return closest_approach