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

  def close_approaches_by_month(start, end):
    params = {'start_date': start, 'end_date': end}
    path = AsteroidService.conn('feed?')
    return requests.get(path, params=params)

  def asteroid_by_id(id):
    uri = 'neo/' + id + '?'
    return requests.get(AsteroidService.conn(uri))
