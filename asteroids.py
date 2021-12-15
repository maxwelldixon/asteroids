from dotenv import dotenv_values
import requests
import calendar


# Asteroids - NeoWs endpoint
endpoint = 'https://api.nasa.gov/neo/rest/v1'

# Loads api key from .env file
config = dotenv_values('.env')
api_key = config['api_key']

def asteroid_closest_approach():
    try:
        res = requests.get(f'{endpoint}/neo/browse?api_key={api_key}', timeout=30)
        json = res.json()
        total_pages = json['page']['total_pages']
        closest_approaches = []

        # loop through each page of data
        for page_num in range(0, total_pages+1):
            res = requests.get(f'{endpoint}/neo/browse?page={page_num}&size=20&api_key={api_key}', timeout=30)
            json = res.json()
            asteroids = json['near_earth_objects']
            for asteroid in asteroids:
                approach_data = asteroid['close_approach_data']
                minimum_miss_distance_miles = float('inf')
                new_close_approach_data = []
                # find closest approach
                for val in approach_data:
                    if float(val['miss_distance']['miles']) < minimum_miss_distance_miles:
                        minimum_miss_distance_miles = float(val['miss_distance']['miles'])
                        if new_close_approach_data == []:
                            new_close_approach_data.append(val)
                        else:
                            new_close_approach_data.pop()
                            new_close_approach_data.append(val)

                # updates close_approach_data list with only the closest approach in miles
                asteroid['close_approach_data'] = new_close_approach_data
                closest_approaches.append(asteroid)

    except requests.exceptions.HTTPError as err_HTTP:
        print('HTTP Error:', err_HTTP)
    except requests.exceptions.ConnectionError as err_connection:
        print('Connection Error:', err_connection)
    except requests.exceptions.Timeout as err_timeout:
        print('Timeout Error:', err_timeout)
    except requests.exceptions.RequestException as err:
        print('Whoopsy, something went wrong', err)

    return closest_approaches

def month_closest_approaches(month: str, year: str):
    try:
        month_approaches = {}
        total_element_count = 0
        start_day = '1'
        last_day = calendar.monthrange(int(year), int(month))[1]
        while last_day - int(start_day) >= 7: 
            res = requests.get(f'{endpoint}/feed?start_date={year}-{month}-{start_day}&api_key={api_key}', timeout=30)
            json = res.json()

            # increment total_element_count by each element_count value in each week
            total_element_count += json['element_count']

            # loop through each day and find the closest approach distance for each asteroid
            days = json['near_earth_objects'].keys()
            for day in days:
                month_approaches[day] = []
                for asteroid in json['near_earth_objects'][day]:
                    approach_data = asteroid['close_approach_data']
                    minimum_miss_distance_miles = float('inf')
                    new_close_approach_data = []
                    # find closest approach
                    for val in approach_data:
                        if float(val['miss_distance']['miles']) < minimum_miss_distance_miles:
                            minimum_miss_distance_miles = float(val['miss_distance']['miles'])
                            if new_close_approach_data == []:
                                new_close_approach_data.append(val)
                            else:
                                new_close_approach_data.pop()
                                new_close_approach_data.append(val)

                    # updates close_approach_data list with only the closest approach in miles
                    asteroid['close_approach_data'] = new_close_approach_data 
                    month_approaches[day].append(asteroid)

            # increment start_day to 1 greater than the last day in the previous response
            start_day = str(int(start_day) + 8)

        # make last request with remaining days in month
        if last_day - int(start_day) >= 2:
            res = requests.get(f'{endpoint}/feed?start_date={year}-{month}-{start_day}&end_date={year}-{month}-{str(last_day)}&api_key={api_key}', timeout=30)
            json = res.json()
            # increment total_element_count by each element_count value in each week
            total_element_count += json['element_count']
            days = json['near_earth_objects'].keys()
            for day in days:
                month_approaches[day] = []
                for asteroid in json['near_earth_objects'][day]:
                    approach_data = asteroid['close_approach_data']
                    minimum_miss_distance_miles = float('inf')
                    new_close_approach_data = []
                    # find closest approach
                    for val in approach_data:
                        if float(val['miss_distance']['miles']) < minimum_miss_distance_miles:
                            minimum_miss_distance_miles = float(val['miss_distance']['miles'])
                            if new_close_approach_data == []:
                                new_close_approach_data.append(val)
                            else:
                                new_close_approach_data.pop()
                                new_close_approach_data.append(val)

                    # updates close_approach_data list with only the closest approach in miles
                    asteroid['close_approach_data'] = new_close_approach_data 
                    month_approaches[day].append(asteroid)

        # append total_element_count for the month
        month_approaches['total_element_count'] = total_element_count

    except requests.exceptions.HTTPError as err_HTTP:
        print('HTTP Error:', err_HTTP)
    except requests.exceptions.ConnectionError as err_connection:
        print('Connection Error:', err_connection)
    except requests.exceptions.Timeout as err_timeout:
        print('Timeout Error:', err_timeout)
    except requests.exceptions.RequestException as err:
        print('Whoopsy, something went wrong', err)

    return month_approaches

def nearest_misses():
    try:
        res = requests.get(f'{endpoint}/neo/browse?api_key={api_key}', timeout=30)
 
    except requests.exceptions.HTTPError as err_HTTP:
        print('HTTP Error:', err_HTTP)
    except requests.exceptions.ConnectionError as err_connection:
        print('Connection Error:', err_connection)
    except requests.exceptions.Timeout as err_timeout:
        print('Timeout Error:', err_timeout)
    except requests.exceptions.RequestException as err:
        print('Whoopsy, something went wrong', err)

    return res.status_code
