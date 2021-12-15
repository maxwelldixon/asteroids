from dotenv import dotenv_values
import requests

# Loads api key from .env file
config = dotenv_values('.env')
api_key = config['api_key']

def asteroid_closest_approach():
    res = requests.get(f'https://api.nasa.gov/neo/rest/v1/neo/browse?api_key={api_key}')
    return res.status_code

def month_closest_approaches(month: str, year: str):
    res = requests.get(f'https://api.nasa.gov/neo/rest/v1/feed?start_date={year}-{month}-01&api_key={api_key}')
    return res.status_code

def nearest_misses():
    res = requests.get(f'https://api.nasa.gov/neo/rest/v1/neo/browse?api_key={api_key}')
    return res.status_code