from asteroids import *
import requests

def test_asteroid_closest_approach():
    assert asteroid_closest_approach() == 200   

def test_month_closest_approaches():
    assert month_closest_approaches('01', '2021') == 200

def test_nearest_misses():
    assert nearest_misses() == 200