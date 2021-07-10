import requests
import json
import logging
import os
import time
import datetime
from datetime import timedelta
import pandas as pd
from pandas.io.json import json_normalize
from flatten_json import flatten
from dotenv import load_dotenv

load_dotenv()

"""
Setting the Log Settings
"""
logging.basicConfig(level=logging.DEBUG)
main = logging.getLogger('main')
main.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
format = logging.Formatter('%(asctime)s  %(name)s %(levelname)s: %(message)s')
handler.setFormatter(format)
main.addHandler(handler)

"""
open-weather data
set parameters to be passed in the url and get the json response
"""


def get_data_open_weather():
    city_id = 2950158
    app_id = os.getenv('APPID')
    try:
        url = 'http://api.openweathermap.org/data/2.5/forecast?id=' + str(
            city_id) + '&appid=' + app_id + '&units=' + 'metric'
        main.info('api accessed successfully')
    except:
        main.error("Error while connecting to the api")
    finally:
        api_result = requests.get(url)
        response = api_result.json()

        """
        only parse the present day data in the json response
        """
        today = (datetime.date.today() + timedelta(days=0)).strftime('%s')
        tomorrow = (datetime.date.today() + timedelta(days=1)).strftime('%s')
        today, tomorrow = int(today), int(tomorrow)
        filtered_data = [d for d in response["list"] if d['dt'] >= today and d['dt'] < tomorrow]
        """
        create dataframe from the filtered data
        """
        df = pd.DataFrame([flatten(_d) for _d in filtered_data])

        """
        rename the columns names which are more user friendly
        """
        df.rename(
            columns={'main_temp': 'Temperature', 'main_feels_like': 'Feels_like',
                     'main_temp_min': 'Minimum_Temperature',
                     'main_temp_max': 'Maximum_Temperature', 'main_humidity': 'Humidity', 'weather_0_main': 'Weather',
                     'weather_0_description': 'Weather_Description', 'dt_txt': 'Date&Time'}, inplace=True)
        """
        drop unrequired columns from the dataframe
        """
        df = df.drop(
            ['dt', 'main_pressure', 'main_sea_level', 'main_grnd_level', 'main_temp_kf', 'weather_0_id',
             'weather_0_icon','clouds_all', 'wind_deg', 'pop', 'sys_pod'], axis=1)
        return df
