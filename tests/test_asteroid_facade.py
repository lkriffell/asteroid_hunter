from asteroid_hunter.facades.asteroid_facade import AsteroidFacade
import vcr

@vcr.use_cassette('tests/fixtures/vcr_cassettes/browse.yaml', record_mode='once')
def test_closest_approach_id():
  closest_approach_id = AsteroidFacade.closest_approach_id()
  assert closest_approach_id == '3292020'

@vcr.use_cassette('tests/fixtures/vcr_cassettes/browse.yaml', record_mode='once')
def test_get_approach_data_by_page():
  approach_data = AsteroidFacade.get_asteroid_data_by_page(0)
  assert len(approach_data) == 20

@vcr.use_cassette('tests/fixtures/vcr_cassettes/asteroid_by_id.yaml', record_mode='once')
def test_asteroid_by_id():
  asteroid = AsteroidFacade.asteroid_by_id('3292020').json()
  assert asteroid['name'] == '(2005 TF)'

@vcr.use_cassette('tests/fixtures/vcr_cassettes/asteroid_approaches_by_month.yaml', record_mode='once')
def test_close_approaches_by_month_can_get_top_ten():
  closest_approaches_in_january = AsteroidFacade.close_approaches_by_month(10, 2021, 1)
  assert len(closest_approaches_in_january) == 10
  assert closest_approaches_in_january[0]['name'] == '(2021 BO)'

@vcr.use_cassette('tests/fixtures/vcr_cassettes/asteroid_approaches_by_month.yaml', record_mode='once')
def test_close_approaches_by_month_can_get_top_twenty():
  closest_approaches_in_january = AsteroidFacade.close_approaches_by_month(20, 2021, 1)
  assert len(closest_approaches_in_january) == 20
  assert closest_approaches_in_january[0]['name'] == '(2021 BO)'

