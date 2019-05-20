from api import weather


def temperature_now():

    return weather.WeatherAPI().temperature_now()
    