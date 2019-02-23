import requests


class BusAPI:
    def __init__(self,
                 token='82adddc3366e99208ab4d40163e90f20a2391d9574bf826dc3679ae4fc5adc50',
                 default_api_url='http://api.olhovivo.sptrans.com.br/v2.1'):

        self.__token = token
        self.__default_api_url = default_api_url

    # The line and stop id are not precise. If wanted this specific information, create a method for that
    def arrival_forecast(self, stop_id, line_id):

        # Makes the authentication and catch its cookies
        url_authentication = '/Login/Autenticar?token={}'.format(self.__token)
        r = requests.post(self.__default_api_url + url_authentication)
        cookies = r.cookies

        # Here is where the method really happens
        url_arrival_forecast = '/Previsao?codigoParada={}&codigoLinha={}'.format(stop_id, line_id)

        r = requests.get(self.__default_api_url + url_arrival_forecast, cookies=cookies)

        json_response = r.json()

        return json_response
