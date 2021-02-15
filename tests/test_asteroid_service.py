from asteroid_hunter.services.asteroid_service import AsteroidService
import vcr
from local_api_keys import LocalApiKeys
from pprint import pprint
neo_key = LocalApiKeys().neo_key

def test_conn():
  assert AsteroidService.conn('neo/browse?') == ('https://api.nasa.gov/neo/rest/v1/neo/browse?' + neo_key)

@vcr.use_cassette('tests/fixtures/vcr_cassettes/browse.yaml', record_mode='once')
def test_browse_neos():
  response = AsteroidService.browse_neos(0)
  assert response.status_code == 200

@vcr.use_cassette('tests/fixtures/vcr_cassettes/asteroid_by_id.yaml', record_mode='once')
def test_asteroid_by_id():
  response = AsteroidService.asteroid_by_id('3292020')
  assert response.status_code == 200

@vcr.use_cassette('tests/fixtures/vcr_cassettes/asteroid_approaches_by_week.yaml', record_mode='once')
def test_asteroid_approaches_by_week():
  response = AsteroidService.asteroid_approaches_by_week('2021-01-01', '2021-01-08')
  assert response.status_code == 200

@vcr.use_cassette('tests/fixtures/vcr_cassettes/browse.yaml', record_mode='once')
def test_structure_browse_neos():
  response = AsteroidService.browse_neos(0)

  asteroids = response.json()

  assert type(asteroids['page']) is dict
  assert type(asteroids['page']['number']) is int
  assert type(asteroids['page']['size']) is int
  assert type(asteroids['page']['total_elements']) is int
  assert type(asteroids['page']['total_pages']) is int
  assert type(asteroids['near_earth_objects']) is list
  assert type(asteroids['near_earth_objects'][0]) is dict

  first_asteroid = asteroids['near_earth_objects'][0]

  assert type(first_asteroid['name_limited']) is str
  assert type(first_asteroid['designation']) is str
  verify_data_structure(first_asteroid)


@vcr.use_cassette('tests/fixtures/vcr_cassettes/asteroid_approaches_by_week.yaml', record_mode='once')
def test_structure_asteroid_approaches_by_week():
  response = AsteroidService.asteroid_approaches_by_week('2021-01-01', '2021-01-08')
  
  close_approaches = response.json()

  assert type(close_approaches['near_earth_objects']) is dict
  assert type(close_approaches['near_earth_objects']['2021-01-01']) is list

  first_new_years_asteroid = close_approaches['near_earth_objects']['2021-01-01'][0]

  verify_data_structure(first_new_years_asteroid)

def verify_data_structure(asteroid):
  assert type(asteroid) is dict
  assert type(asteroid['links']) is dict
  assert type(asteroid['links']['self']) is str
  assert type(asteroid['id']) is str
  assert type(asteroid['neo_reference_id']) is str
  assert type(asteroid['name']) is str
  assert type(asteroid['nasa_jpl_url']) is str
  assert type(asteroid['absolute_magnitude_h']) is float
  assert type(asteroid['estimated_diameter']) is dict
  assert type(asteroid['estimated_diameter']['kilometers']) is dict
  assert type(asteroid['estimated_diameter']['meters']) is dict
  assert type(asteroid['estimated_diameter']['miles']) is dict
  assert type(asteroid['estimated_diameter']['feet']) is dict
  assert type(asteroid['is_potentially_hazardous_asteroid']) is bool
  assert type(asteroid['is_sentry_object']) is bool
  assert type(asteroid['close_approach_data']) is list
  assert type(asteroid['close_approach_data'][0]) is dict
  assert type(asteroid['close_approach_data'][0]['close_approach_date']) is str
  assert type(asteroid['close_approach_data'][0]['close_approach_date_full']) is str
  assert type(asteroid['close_approach_data'][0]['epoch_date_close_approach']) is int
  assert type(asteroid['close_approach_data'][0]['relative_velocity']) is dict
  assert type(asteroid['close_approach_data'][0]['relative_velocity']['kilometers_per_second']) is str
  assert type(asteroid['close_approach_data'][0]['relative_velocity']['kilometers_per_hour']) is str
  assert type(asteroid['close_approach_data'][0]['relative_velocity']['miles_per_hour']) is str
  assert type(asteroid['close_approach_data'][0]['miss_distance']) is dict
  assert type(asteroid['close_approach_data'][0]['miss_distance']['astronomical']) is str
  assert type(asteroid['close_approach_data'][0]['miss_distance']['lunar']) is str
  assert type(asteroid['close_approach_data'][0]['miss_distance']['kilometers']) is str
  assert type(asteroid['close_approach_data'][0]['miss_distance']['miles']) is str
  assert type(asteroid['close_approach_data'][0]['orbiting_body']) is str