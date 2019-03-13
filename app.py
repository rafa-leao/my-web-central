from flask import Flask, render_template

import time

from api.weather import WeatherAPI
from api.bus_traffic import BusAPI

app = Flask(__name__)


@app.route('/')
def index():

    weather_info = WeatherAPI()
    temperature_now = weather_info.temperature_now()

    one_hour_later = hours_later()
    bus_arrival = buses_arrivals()
    temperature_to_one_hour_later = temperatures_to_one_hour_later()

    return render_template('index.html',
                           temperature_now=temperature_now,
                           bus_arrival=bus_arrival,
                           one_hour_later=one_hour_later,
                           temperature_to_one_hour_later=temperature_to_one_hour_later)


def buses_arrivals():

    bus_info = BusAPI()

    # These are buses a take to go to subway station at morning

    bus_metro_vl_matilde_1 = bus_info.arrival_forecast(650005666, 932)
    bus_metro_vl_matilde_2 = bus_info.arrival_forecast(650005666, 390)

    # sptrans is not giving the metro penha information today, so try other day :c
    #
    # bus_metro_penha = bus_info.arrival_forecast(650005666, 929)
    #   buses = [bus_metro_vl_matilde_1,
    #            bus_metro_vl_matilde_2,
    #            bus_metro_penha]

    buses = [bus_metro_vl_matilde_1,
             bus_metro_vl_matilde_2]

    return buses


def temperatures_to_one_hour_later():

    weather_info = WeatherAPI()

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


app.run(debug=True)
