# asteroid_hunter

## Getting started
  - Clone this repo to your machine
  - Get a nasa api key here: https://api.nasa.gov/
  - Currently api keys are stored in a gitignored class, not handled by something like dotenv.
  - Add this `local_api_keys.py` class with your key to the root file
  ```
  class LocalApiKeys:
    def __init__(self):
      self.neo_key = 'api_key=YOUR_KEY'
  ```
