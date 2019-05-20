from api import bus_traffic


def buses_arrivals():

    bus_info = bus_traffic.BusAPI()

    # These are buses I take to go to subway station at morning!

    # Sptrans is not giving the metro_penha information today, so try other day :c
    #
    # bus_metro_penha = bus_info.arrival_forecast(650005666, 929)
    bus_metro_vl_matilde_1 = bus_info.arrival_forecast(650005666, 932)
    bus_metro_vl_matilde_2 = bus_info.arrival_forecast(650005666, 390)

    buses = {"bus1": bus_metro_vl_matilde_1,
             "bus2": bus_metro_vl_matilde_2}

    return buses