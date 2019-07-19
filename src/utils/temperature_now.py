from api.weather import WeatherAPI


def temperature_now():

    return WeatherAPI().temperature_now()
    