from asteroids import *
from dotenv import dotenv_values
import requests

# Asteroids - NeoWs endpoint
endpoint = 'https://api.nasa.gov/neo/rest/v1'

# Loads api key from .env file
config = dotenv_values('.env')
api_key = config['api_key']

def test_asteroid_closest_approach_api_response():
    res = requests.get(f'{endpoint}/neo/browse?api_key={api_key}', timeout=30)
    assert res.status_code == 200  

def test_asteroid_closest_approach_returned_data():
    assert asteroid_closest_approach() != []

def test_month_closest_approaches_api_response():
    start_day = '1'
    year = '2021'
    month = '1'
    res = requests.get(f'{endpoint}/feed?start_date={year}-{month}-{start_day}&api_key={api_key}', timeout=30)
    assert res.status_code == 200

def test_month_closest_approaches():
    assert month_closest_approaches('1', '2021') != []

def test_nearest_misses():
    assert nearest_misses() == 200