from flask import Flask, render_template

from utils import utils

app = Flask(__name__)


@app.route('/')
def index():

    return render_template('index.html',
                           temperature_now=utils.temperature_now(),
                           bus_arrival=utils.buses_arrivals(),
                           one_hour_later=utils.hours_later(),
                           temperature_to_one_hour_later=utils.temperatures_to_one_hour_later())


if __name__ == "__main__":
    app.run(debug=True)
