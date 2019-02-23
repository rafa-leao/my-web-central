from flask import Flask, render_template

import api.weather
import api.bus_traffic

app = Flask(__name__)


@app.route('/')
def index():

    weather_info = api.weather.WeatherAPI()
    temperature_now = weather_info.temperature_now()

    bus_info = api.bus_traffic.BusAPI()
    bus_arrival = bus_info.arrival_forecast(650005666, 932)

    return render_template('index.html', temperature_now=temperature_now, bus_arrival=bus_arrival)


app.run(debug=True)
