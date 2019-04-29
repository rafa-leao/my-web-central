from api import weather
from api import bus_traffic


import time


# -- bus-wise


def buses_arrivals():

    bus_info = bus_traffic.BusAPI()

    # These are buses I take to go to subway station at morning!

    # Sptrans is not giving the metro_penha information today, so try other day :c
    #
    # bus_metro_penha = bus_info.arrival_forecast(650005666, 929)
    bus_metro_vl_matilde_1 = bus_info.arrival_forecast(650005666, 932)
    bus_metro_vl_matilde_2 = bus_info.arrival_forecast(650005666, 390)

    buses = {"bus1": bus_metro_vl_matilde_1,
             "bus2": bus_metro_vl_matilde_2}

    return buses


# -- temperature-wise


def temperature_now():

    return weather.WeatherAPI().temperature_now()


def temperatures_to_one_hour_later():

    weather_info = weather.WeatherAPI()

    time_now = time.localtime()[3]

    return [weather_info.temperature(time_now+1),
            weather_info.temperature(time_now+2),
            weather_info.temperature(time_now+3),
            weather_info.temperature(time_now+4)]


def hours_later():

    time_now = time.localtime()[3]

    return [time_now + 1,
            time_now + 2,
            time_now + 3,
            time_now + 4]
