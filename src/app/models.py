from flask import jsonify
from app.db import get_dict_resultset, ONE, ALL
from app.tools import validate_params
from app.bill import calculate_call_tariff


def start_call(js):
    """
    INSERT a new call to the database or UPDATE if it is already there.
    Since inconsistencies can happen, it's possible to receive the "end signal"
    before the "start signal".
    If one of the required parameters is not present, return an HTTP error.

    :param js: JSON contaning the necessary parameters.

    :return: JSON containing the ID of the inserted/updated item or an error
    containing the HTTP status code 500.
    """

    validate_params(['call_id', 'timestamp', 'source', 'destination'], js)

    sql = '''
        INSERT INTO CALLS (
            timestamp_begin,
            source,
            destination,
            call_id
        ) VALUES (%s, %s, %s, %s)
        ON CONFLICT(call_id) DO UPDATE SET
            timestamp_begin=%s,
            source=%s,
            destination=%s
        RETURNING id
    '''
    params = (
        js.get('timestamp'),
        js.get('source'),
        js.get('destination'),
        js.get('call_id'),

        js.get('timestamp'),
        js.get('source'),
        js.get('destination')
    )
    return jsonify(get_dict_resultset(sql, params, ONE))


def end_call(js):
    """
    UPDATE a call in database based on its unique "call_id".
    Since inconsistencies can happen, the code will try to insert if the
    "call_id" is not yet present.
    If one of the required parameters is not present, return an HTTP error.

    :param js: JSON contaning the necessary parameters.

    :return: JSON containing the ID of the inserted/updated item or an error
    containing the HTTP status code 500.
    """

    validate_params(['call_id', 'timestamp'], js)

    sql = '''
        INSERT INTO CALLS (
            timestamp_end,
            call_id
        ) VALUES (%s, %s)
        ON CONFLICT(call_id) DO UPDATE SET
            timestamp_end=%s
        RETURNING id
    '''
    params = (
        js.get('timestamp'),
        js.get('call_id'),

        js.get('timestamp')
    )
    # Maybe I should calculate the price after inserting the end call
    # Update where call_id = X and timestamp_begin is not null
    # I must assume that every call already has a "begin"
    # ToDo: New Logic!
    return jsonify(get_dict_resultset(sql, params, ONE))


def get_bill(phone_number):
    # ToDo -> Just a placeholder
    sql = '''
        SELECT
            timestamp_begin,
            timestamp_end,
            (EXTRACT(EPOCH FROM (timestamp_end - timestamp_begin))) as duration,
            price
        FROM CALLS
        WHERE (
            (timestamp_end IS NOT NULL) AND
            (timestamp_begin IS NOT NULL) AND
            (timestamp_end > timestamp_begin)
        )
    '''
    sql_result = get_dict_resultset(sql, None, ALL)
    if sql_result:
        for item in sql_result:
            calculate_call_tariff(
                item['timestamp_begin'],
                item['timestamp_end']
            )
    return jsonify(get_dict_resultset(sql, None, ALL))
