from asteroid_hunter.services.asteroid_service import AsteroidService
import vcr
from local_api_keys import LocalApiKeys
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

@vcr.use_cassette('tests/fixtures/vcr_cassettes/close_approaches_by_month.yaml', record_mode='once')
def test_close_approaches_by_month():
  response = AsteroidService.close_approaches_by_month('2021-01-01', '2021-01-08')
  assert response.status_code == 200
