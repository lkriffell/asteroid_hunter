from asteroid_hunter.facades.asteroid_facade import AsteroidFacade
import vcr

@vcr.use_cassette('tests/fixtures/vcr_cassettes/browse_two.yaml', record_mode='once', filter_query_parameters=['api_key'])
def test_closest_approaches():
  ten_closest_approaches = AsteroidFacade.closest_approaches(10)
  assert len(ten_closest_approaches) == 10
  for near_miss in ten_closest_approaches:
    assert type(near_miss['close_approach_data']) == dict

@vcr.use_cassette('tests/fixtures/vcr_cassettes/nearest_miss.yaml', record_mode='once', filter_query_parameters=['api_key'])
def test_closest_approaches_can_return_the_closest_miss():
  nearest_miss = AsteroidFacade.closest_approaches(1)
  assert type(nearest_miss) == dict
  assert type(nearest_miss['close_approach_data']) == dict

@vcr.use_cassette('tests/fixtures/vcr_cassettes/january_approaches_by_month.yaml', record_mode='once', filter_query_parameters=['api_key'])
def test_closest_approaches_by_month_can_get_top_ten():
  closest_approaches_in_january = AsteroidFacade.closest_approaches_by_month(10, 2021, 1)
  assert len(closest_approaches_in_january['closest_approaches']) == 10
  assert closest_approaches_in_january['closest_approaches'][0]['name'] == '(2021 BO)'
  assert closest_approaches_in_january['element_count'] == 483

@vcr.use_cassette('tests/fixtures/vcr_cassettes/january_approaches_by_month.yaml', record_mode='once', filter_query_parameters=['api_key'])
def test_closest_approaches_by_month_can_get_top_twenty():
  closest_approaches_in_january = AsteroidFacade.closest_approaches_by_month(20, 2021, 1)
  assert len(closest_approaches_in_january['closest_approaches']) == 20
  assert closest_approaches_in_january['closest_approaches'][0]['name'] == '(2021 BO)'
  assert closest_approaches_in_january['element_count'] == 483

