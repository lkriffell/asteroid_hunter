# asteroid_hunter

## Getting started
  - Clone this repo to your machine
  - Get a nasa api key here: https://api.nasa.gov/
  - Add your `API_KEY` to `.env` in the root file. ex: `API_KEY=MY_KEY`
  - If you are getting this error: `ModuleNotFoundError: No module named 'dotenv'`, run `sudo pip3 install python-dotenv`. This means the dependency in the lockfile is not properly working

## Running Tests
  - Run the test suite with `pytest`
  
## Functions
  - asteroid_closest_approach
    - Finds the closest approach out of all of Nasa's NEO data
    - How it works:
       - Gets every approach from each NEO and sorts by closest approach until there are no more pages left to retrieve. The first result is returned in json format.
  - month_closest_approaches(result_size, year, month)
    - Finds the closest N amount of approaches in a given month
    - How it works:
      - Gets every approach from each NEO in a given week and sorts by closest approach. Does this for each week in the month until the final week has been retrieved and sorted.
  - asteroid_closest_approaches(result_size = 10)
    - Finds the closest N amount of approaches out of all of Nasa's NEO data. Default result size is ten closest approaches
    - How it works:
       - Gets every approach from each NEO and sorts by closest approach until there are no more pages left to retrieve. The first N results are returned in json format.
  
## Tradeoffs and considerations
