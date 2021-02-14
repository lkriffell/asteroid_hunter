# import os
from local_api_keys import LocalApiKeys
import requests

class AsteroidService:
  def conn(uri):
    neo_key = LocalApiKeys().neo_key
    return 'https://api.nasa.gov/neo/rest/v1/neo/' + uri + neo_key

  def browse_neos(page):
    params = {'page': page}
    return requests.get(AsteroidService.conn('browse?'), params=params)

  def asteroid_by_id(id):
    return requests.get(AsteroidService.conn(id + '?'))
