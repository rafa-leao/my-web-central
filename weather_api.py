import requests


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

        url_forecast_info = '/api/v1/forecast/locale/{}/hours/72?token={}'.format(self.__sao_paulo_id, self.__token)

        r = requests.get(self.__default_api_url + url_forecast_info)

        json_response = r.json()

        # If you get confuse at this data extraction, see how the response is in the documentation:
        # http://apiadvisor.climatempo.com.br/doc/index.html#api-Forecast-Forecast72HoursByCity
        json_id = json_response['data'][0]['temperature']['temperature']

        return json_id

    def forecast_data(self):

            url_forecast_info = '/api/v1/forecast/locale/{}/hours/72?token={}'.format(self.__sao_paulo_id, self.__token)

            r = requests.get(self.__default_api_url + url_forecast_info)

            json_response = r.json()

            json_id = json_response

            return json_id


id_from_SP = WeatherAPI().state_id('São Paulo', 'SP')
print("O ID de São Paulo é: {}".format(id_from_SP))

temperatura_de_agora = WeatherAPI().temperature_now()
print("A temperatura é de {}ºC".format(temperatura_de_agora))

all_data = WeatherAPI().forecast_data()
print(all_data)
