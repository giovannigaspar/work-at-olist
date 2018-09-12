from flask import jsonify
from app.db import get_dict_resultset, ONE, ALL
from app.tools import validate_params
from app.bill import _calculate_call_tariff


def start_call(js):
    """
    INSERT a new call to the database.
    If one of the required parameters is not present, return an HTTP error.

    :param js: JSON contaning the necessary parameters.

    :return: JSON containing the ID of the inserted item or an error containing
    the HTTP status code 500.
    """

    validate_params(['call_id', 'timestamp', 'source', 'destination'], js)

    sql = '''
        INSERT INTO CALLS (
            timestamp_begin,
            source,
            destination,
            call_id
        ) VALUES (%s, %s, %s, %s)
        RETURNING id
    '''
    params = (
        js.get('timestamp'),
        js.get('source'),
        js.get('destination'),
        js.get('call_id')
    )
    return jsonify(get_dict_resultset(sql, params, ONE))


def end_call(js):
    """
    Terminate a call.
    UPDATE a call in database based on its unique "call_id": set the ending time
    of the call and calculate the call tariff.
    If one of the required parameters is not present, return an HTTP error.

    :param js: JSON contaning the necessary parameters.

    :return: JSON containing the ID of the updated item or an error containing
    the HTTP status code 500.
    """

    validate_params(['call_id', 'timestamp'], js)

    sql = '''
        UPDATE CALLS SET
            timestamp_end=%s
        WHERE (
            (call_id=%s) AND
            (timestamp_begin is not null) AND
            (timestamp_end is null)
        )
        RETURNING
            timestamp_begin,
            timestamp_end,
            (timestamp_begin - %s ) as duration,
            id
    '''
    params = (
        js.get('timestamp'),
        js.get('call_id'),
        js.get('timestamp')
    )
    r = get_dict_resultset(sql, params, ONE)

    if r:
        price = _calculate_call_tariff(
            r['timestamp_begin'],
            r['timestamp_end'],
            r['duration']
        )
        sql = '''
            UPDATE CALLS SET
                price=%s
            WHERE id=%s
            RETURNING id
        '''
        params = (
            price,
            r['id']
        )
        return jsonify(get_dict_resultset(sql, params, ONE))


def get_bill(phone_number, period):
    """
    Get a subscriber bill within the given period.

    :param phone_number: Subscriber's phone number
    :param period: The bill period (MM/YYYY)

    :return: JSON containing the bill data if it's available. Example:
      {
        "call_price": "R$0,99",
        "call_start_date": "2017-12-12",
        "call_start_time": "15:07:13",
        "destination": "9993468278",
        "duration": "0h:07m:43s"
      }
    """
    sql = '''
        SELECT
            destination,
            timestamp_begin::DATE as call_start_date,
            timestamp_begin::TIME as call_start_time,
            (timestamp_end - timestamp_begin) as duration,
            ('R$' || ' ' || price) as call_price
        FROM CALLS
        WHERE (
            (timestamp_end IS NOT NULL) AND
            (timestamp_begin IS NOT NULL) AND
            (timestamp_end > timestamp_begin) AND
            (source = %s) AND
            (EXTRACT(MONTH FROM timestamp_end) = %s) AND
            (EXTRACT(YEAR FROM timestamp_end) = %s)
        )
    '''
    period = period.split('/')
    params = (
        phone_number,
        period[0],
        period[1]
    )
    return jsonify(get_dict_resultset(sql, params, ALL))
