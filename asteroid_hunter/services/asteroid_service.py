import requests
import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('NEO_API_KEY')

class AsteroidService:
  def conn(uri):
    return 'https://api.nasa.gov/neo/rest/v1/' + uri + f"api_key={API_KEY}"

  def browse_neos_by_page(page):
    params = {'page': page}
    path = AsteroidService.conn('neo/browse?')
    return requests.get(path, params=params)

  def asteroid_approaches_by_week(start, end):
    params = {'start_date': start, 'end_date': end}
    path = AsteroidService.conn('feed?')
    return requests.get(path, params=params)

  def asteroid_by_id(id):
    uri = f"neo/{id}?"
    return requests.get(AsteroidService.conn(uri))
