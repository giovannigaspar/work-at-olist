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
            (timestamp_end > timestamp_begin)
        )
        RETURNING timestamp_begin, duration, id
    '''
    params = (
        js.get('timestamp'),
        js.get('call_id')
    )
    r = jsonify(get_dict_resultset(sql, params, ONE))

    if r:
        price = _calculate_call_tariff(
            r['timestamp_begin'],
            js.get('timestamp'),
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
    """
    sql = '''
        SELECT
            destination,
            timestamp_begin::DATE as call_start_date,
            timestamp_begin::TIME as call_start_time,
            (timestamp_end - timestamp_begin) as duration,
            price as call_price
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
