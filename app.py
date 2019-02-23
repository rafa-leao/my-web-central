from flask import Flask, render_template

import api.weather

app = Flask(__name__)

@app.route('/')
def index():

    weather = api.weather.WeatherAPI()

    temperature_now = weather.temperature_now()

    return render_template('index.html', temperature_now=temperature_now )


app.run(debug=True)
