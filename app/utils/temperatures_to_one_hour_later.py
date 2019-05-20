from api import weather
import time

def temperatures_to_one_hour_later():

    weather_info = weather.WeatherAPI()

    time_now = time.localtime()[3]

    return [weather_info.temperature(time_now+1),
            weather_info.temperature(time_now+2),
            weather_info.temperature(time_now+3),
            weather_info.temperature(time_now+4)]
