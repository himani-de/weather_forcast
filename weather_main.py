import requests
import json
import logging
import os
import time
import pandas as pd
from pandas import json_normalize
from dotenv import load_dotenv
load_dotenv()
from weather_data import get_data_open_weather

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
initialise the function which had the data from open_weather api
"""
open_weather_data = get_data_open_weather()

"""
we are using the Weather Forecast api end point as we have to check the weather for tomorrow
"""
api_url = 'http://api.weatherstack.com/current'
access_key = os.getenv('ACCESS_KEY')  # read access key from .env file

params = {
    'access_key': access_key,  # access key for the authentication to access the api
    'query': 'Berlin',
    'units': 'm'
}
try:
    api_result = requests.get(api_url, params)  # use python get method to extract the data
except:
    main.error("Error while connecting to the api")
finally:
    response = api_result.json()

    """
    we will normalize the data as it is a nested json response and create dataframe
    """
    weather_df = pd.DataFrame.from_dict(pd.json_normalize(response), orient='columns')

    """
    take the columns which are required
    """
    df_new = weather_df.filter(['location.name', 'location.country', 'location.timezone_id', 'location.localtime',
                                'current.wind_dir', 'current.precip', 'current.uv_index', 'current.is_day'], axis=1)
    """
    rename the column names which are user understandable
    """
    df_new.rename(
        columns={'location.name': 'City', 'location.country': 'Country', 'location.timezone_id': 'Timezone_Id',
                 'location.localtime': 'Date&Time', 'current.wind_dir': 'Wind_Direction', 'current.precip': 'Percipitation',
                 'current.uv_index': 'UV_Index'}, inplace=True)
    """
    join both the dataframes
    """
    combined_df = pd.merge(open_weather_data,df_new, on='Date&Time', how='outer')
