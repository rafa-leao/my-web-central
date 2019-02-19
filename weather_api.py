import requests

import time


class WeatherAPI:
    def __init__(self,
                 token='c5bd235249d641dbbc1e93e2ca90e04b',
                 default_api_url='http://apiadvisor.climatempo.com.br',
                 sao_paulo_id=3477):

        self.__token = token
        self.__default_api_url = default_api_url
        self.__sao_paulo_id = sao_paulo_id

    def state_id(self, city_name, city_state):

        url_state_info = '/api/v1/locale/city?name={}&state={}&token={}'\
            .format(city_name, city_state, self.__token)

        r = requests.get(self.__default_api_url + url_state_info)

        json_response = r.json()
        json_id = json_response[0]['id']

        return json_id

    def temperature_now(self):

        # get just the hour from a str_time()
        time_now = time.localtime()[3]

        url_forecast_info = '/api/v1/forecast/locale/{}/hours/72?token={}'.format(self.__sao_paulo_id, self.__token)
        r = requests.get(self.__default_api_url + url_forecast_info)

        json_response = r.json()
        # If you get confuse at this data extraction, see how the response is in the documentation:
        # http://apiadvisor.climatempo.com.br/doc/index.html#api-Forecast-Forecast72HoursByCity

        json_temperature = json_response['data'][time_now]['temperature']['temperature']

        return json_temperature

    def forecast_data(self):

            url_forecast_info = '/api/v1/forecast/locale/{}/hours/72?token={}'.format(self.__sao_paulo_id, self.__token)

            r = requests.get(self.__default_api_url + url_forecast_info)

            json_response = r.json()
            json_all_data = json_response

            return json_all_data


temperature = WeatherAPI().temperature_now()
print(temperature)
