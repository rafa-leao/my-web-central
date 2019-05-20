import time


def hours_later():

    time_now = time.localtime()[3]

    return [time_now + 1,
            time_now + 2,
            time_now + 3,
            time_now + 4]
            