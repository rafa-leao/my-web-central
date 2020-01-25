from apis_client.bus_traffic import BusAPI


def buses_arrivals():

    # These are buses I take to go to subway station at morning!

    # Sptrans is not giving the metro_penha information today, so try other day :c
    #
    # bus_metro_penha = BusAPI().arrival_forecast(650005666, 929)
    bus_metro_vl_matilde_1 = BusAPI().arrival_forecast(650005666, 932)
    bus_metro_vl_matilde_2 = BusAPI().arrival_forecast(650005666, 390)

    buses = {"bus1": bus_metro_vl_matilde_1,
             "bus2": bus_metro_vl_matilde_2}

    return buses
    