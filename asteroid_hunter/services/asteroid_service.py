# import os
from local_api_keys import LocalApiKeys
import requests

class AsteroidService:
  def conn(uri):
    neo_key = LocalApiKeys().neo_key
    return 'https://api.nasa.gov/neo/rest/v1/' + uri + neo_key

  def browse_neos(page):
    params = {'page': page}
    path = AsteroidService.conn('neo/browse?')
    return requests.get(path, params=params)

  def close_approach_by_month():
    path = AsteroidService.conn('feed?start_date=2021-01-01&end_date=2021-01-08')
    requests.get(path, params=params)

  def asteroid_by_id(id):
    return requests.get(AsteroidService.conn(id + '?'))
