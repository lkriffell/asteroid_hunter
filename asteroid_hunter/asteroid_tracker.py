from asteroid_hunter.facades.asteroid_facade import AsteroidFacade
import json

class AsteroidTracker:
  def asteroid_closest_approach():
    closest_approach = AsteroidFacade.closest_approaches(1)
    return json.dumps(closest_approach)

  def month_closest_approaches(result_size, year, month):
    closest_approaches = AsteroidFacade.closest_approaches_by_month(result_size, year, month)
    return json.dumps(closest_approaches)

  def asteroid_closest_approaches(result_size = 10):
    ten_closest_approaches = AsteroidFacade.closest_approaches(result_size)
    return json.dumps({'closest_approaches': ten_closest_approaches})
