import datetime


STANDING_CHARGE = 0.36
DAY_TAX = 0.09


def _calculate_call_tariff(begin, end, duration):
    """
    Calculate the call tariff based on the call start, end and duration.

    :param begin: Start of call timestamp.
    :param end: End of call timestamp.
    :param duration: Duration of call in timedelta format
    """
    current_time = begin
    minutes = 0
    price = STANDING_CHARGE
    while (current_time < end):
        current_time = current_time + datetime.timedelta(0,60)
        if (current_time.hour >= 6) and (current_time.hour < 22):
            minutes = (minutes+1)
    if (str(duration).split(':')[2] != '00'):
        minutes = (minutes-1)
    price = price + (minutes * DAY_TAX)
    return str(round(price, 2))
