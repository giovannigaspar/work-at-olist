"""
Module used to calculate a phone bill.
"""


import datetime


# Fixed values for more flexibility. When changed, will reflect in all
# application
STANDING_CHARGE = 0.36
DAY_TAX = 0.09


# The simplest way of doing it!!! :)
def _calculate_call_tariff(begin, end, duration):
    """
    Calculate the call tariff based on the call start, end and duration.
    Loops from the "start timestamp" to the "end timestamp" incrementing one
    minute at a time and checking the tariff of the current value in loop.

    :param begin: Start of call timestamp.
    :param end: End of call timestamp.
    :param duration: Duration of call in timedelta format
    """
    current_time = begin
    minutes = 0
    price = STANDING_CHARGE

    # Best scenario: one comparison
    # Worst scenario: one comparison + loop
    # Very fast, even looping through 24h+ calls
    if not (((begin.hour < 6) or (begin.hour >= 22)) and
            ((end.hour < 6) or (end.hour >= 22))):
        while (current_time < end):
            if (current_time.hour >= 6) and (current_time.hour < 22):
                minutes = (minutes+1)
            current_time = current_time + datetime.timedelta(0,60)
        if (str(duration).split(':')[2] != '00'):
            minutes = (minutes-1)
        price = price + (minutes * DAY_TAX)
    return str(round(price, 2))
