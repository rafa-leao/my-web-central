from flask import Flask, render_template

import time

from api.weather import WeatherAPI
from api.bus_traffic import BusAPI

app = Flask(__name__)


@app.route('/')
def index():

    weather_info = WeatherAPI()
    temperature_now = weather_info.temperature_now()

    return render_template('index.html',
                           temperature_now=temperature_now,
                           bus_arrival=buses_arrivals(),
                           one_hour_later=hours_later(),
                           temperature_to_one_hour_later=temperatures_to_one_hour_later())


def buses_arrivals():

    bus_info = BusAPI()

    # These are buses I take to go to subway station at morning

    # sptrans is not giving the metro_penha information today, so try other day :c
    #
    # bus_metro_penha = bus_info.arrival_forecast(650005666, 929)
    bus_metro_vl_matilde_1 = bus_info.arrival_forecast(650005666, 932)
    bus_metro_vl_matilde_2 = bus_info.arrival_forecast(650005666, 390)

    buses = {"bus1": bus_metro_vl_matilde_1,
             "bus2": bus_metro_vl_matilde_2}

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


if __name__ == "__main__":
    app.run(debug=True)
