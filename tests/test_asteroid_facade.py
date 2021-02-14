from asteroid_hunter.facades.asteroid_facade import AsteroidFacade
import vcr

@vcr.use_cassette('tests/fixtures/vcr_cassettes/browse.yaml', record_mode='once')
def test_closest_approach_id():
  closest_approach_id = AsteroidFacade.closest_approach_id()
  assert closest_approach_id == '3292020'


def test_get_approach_data_by_page():
  approach_data = AsteroidFacade.get_approach_data_by_page(0)
  assert len(approach_data) == 20

@vcr.use_cassette('tests/fixtures/vcr_cassettes/asteroid_by_id.yaml', record_mode='once')
def test_asteroid_by_id():
  asteroid = AsteroidFacade.asteroid_by_id('3709286')
  assert asteroid['name'] == '(2002 LX64)'

