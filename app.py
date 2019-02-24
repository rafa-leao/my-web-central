from flask import Flask, render_template

import time

import api.weather
import api.bus_traffic

app = Flask(__name__)


@app.route('/')
def index():

    weather_info = api.weather.WeatherAPI()
    temperature_now = weather_info.temperature_now()

    bus_info = api.bus_traffic.BusAPI()
    bus_arrival = bus_info.arrival_forecast(650005666, 932)

    time_now = time.localtime()[3]

    one_hour_later = [time_now + 1,
                      time_now + 2,
                      time_now + 3,
                      time_now + 4]

    temperature_to_one_hour_later = [weather_info.temperature(time_now+1),
                      weather_info.temperature(time_now+2),
                      weather_info.temperature(time_now+3),
                      weather_info.temperature(time_now+4)]

    return render_template('index.html',
                           temperature_now=temperature_now,
                           bus_arrival=bus_arrival,
                           one_hour_later=one_hour_later,
                           temperature_to_one_hour_later=temperature_to_one_hour_later)


app.run(debug=True)
