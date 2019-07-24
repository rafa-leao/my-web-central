from api.weather import WeatherAPI

import time

def temperature_to_one_hour_later():

    time_now = time.localtime()[3]

    return [WeatherAPI().temperature(time_now+1),
            WeatherAPI().temperature(time_now+2),
            WeatherAPI().temperature(time_now+3),
            WeatherAPI().temperature(time_now+4)]
