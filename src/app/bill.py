import datetime


STANDING_CHARGE = 0.36
DAY_TAX = 0.09


def calculate_call_tariff(begin, end):
    current_time = begin
    minutes = 0
    price = STANDING_CHARGE
    while (current_time < end):
        current_time = current_time + datetime.timedelta(0,60)
        if (current_time.hour >= 6) and (current_time.hour < 22):
            minutes = minutes+1
    price = price + (minutes * DAY_TAX)
    print(price)
