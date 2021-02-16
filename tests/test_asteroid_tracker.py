from asteroid_hunter.asteroid_tracker import AsteroidTracker
import vcr
from pprint import pprint
import json

@vcr.use_cassette('tests/fixtures/vcr_cassettes/browse_two.yaml', record_mode='once', filter_query_parameters=['api_key'])
def test_asteroid_closest_approach(): 
  closest_approach = AsteroidTracker.asteroid_closest_approach()
  closest_approach = json.loads(closest_approach)
  assert type(closest_approach) == dict
  assert type(closest_approach['id']) == str
  assert type(closest_approach['name']) == str
  assert type(closest_approach['close_approach_data']) == dict
  assert type(closest_approach['close_approach_data']['miss_distance']) == dict
  assert type(closest_approach['close_approach_data']['miss_distance']['astronomical']) == str

@vcr.use_cassette('tests/fixtures/vcr_cassettes/december_closest_approaches.yaml', record_mode='once', filter_query_parameters=['api_key'])
def test_month_closest_approaches(): 
  closest_approaches = AsteroidTracker.month_closest_approaches(10, 2020, 12)
  closest_approaches = json.loads(closest_approaches)
  assert type(closest_approaches) == dict
  assert type(closest_approaches['closest_approaches']) == list
  assert len(closest_approaches['closest_approaches']) == 10
  assert type(closest_approaches['element_count']) == int

  for asteroid in closest_approaches['closest_approaches']:
    assert type(asteroid) == dict
    assert type(asteroid['close_approach_data']) == list
    assert len(asteroid['close_approach_data']) == 1

@vcr.use_cassette('tests/fixtures/vcr_cassettes/browse_two.yaml', record_mode='once', filter_query_parameters=['api_key'])
def test_asteroid_closest_approaches(): 
  ten_closest_approaches = AsteroidTracker.asteroid_closest_approaches()
  ten_closest_approaches = json.loads(ten_closest_approaches)
  assert type(ten_closest_approaches) == dict
  assert type(ten_closest_approaches['closest_approaches']) == list
  assert len(ten_closest_approaches['closest_approaches']) == 10

  for asteroid in ten_closest_approaches['closest_approaches']:
    assert type(asteroid) == dict
    assert type(asteroid['close_approach_data']) == dict
