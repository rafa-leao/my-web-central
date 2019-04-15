import requests


class BusAPI:
    def __init__(self,
                 token='82adddc3366e99208ab4d40163e90f20a2391d9574bf826dc3679ae4fc5adc50',
                 default_api_url='http://api.olhovivo.sptrans.com.br/v2.1'):

        self.__token = token
        self.__default_api_url = default_api_url

    def bus_line_id(self, line_supposition):

        # Makes the authentication and catch its cookies
        url_authentication = '/Login/Autenticar?token={}'.format(self.__token)
        r = requests.post(self.__default_api_url + url_authentication)
        cookies = r.cookies

        # Here is where the method really happens
        url_bus_line = '/Linha/Buscar?termosBusca={}'.format(line_supposition)

        r = requests.get(self.__default_api_url + url_bus_line, cookies=cookies)

        json_response = r.json()

        # Every bus line has two ids
        line_id_1 = json_response[0]['cl']
        line_id_2 = json_response[1]['cl']

        lines = [line_id_1, line_id_2]

        return lines

    def arrival_forecast(self, bus_stop_id, bus_line_id):
        # my stop_id
        # --- 650005666
        # my line_id to metro vl. matilde
        # --- 932
        # --- 390
        # my line_id to metro penha
        # --- 929

        # Makes the authentication and catch its cookies
        url_authentication = '/Login/Autenticar?token={}'.format(self.__token)
        r = requests.post(self.__default_api_url + url_authentication)
        cookies = r.cookies

        # Here is where the method really happens
        url_arrival_forecast = '/Previsao?codigoParada={}&codigoLinha={}'.format(bus_stop_id, bus_line_id)

        r = requests.get(self.__default_api_url + url_arrival_forecast, cookies=cookies)

        json_response = r.json()

        buses_arrival = json_response['p']['l'][0]['vs'][0]['t']

        return buses_arrival
