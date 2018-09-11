from app.db import get_dict_resultset, ONE, ALL


def start_call(js):
    """
    INSERT a new call to the database or UPDATE if it is already there.
    Since inconsistencies can happen, it's possible to receive the "end signal"
    before the "start signal".
    """

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
    return get_dict_resultset(sql, params, ONE)


def end_call(js):
    """
    UPDATE a call in database based on its unique "call_id".
    Since inconsistencies can happen, the code will try to insert if the
    "call_id" is not yet present.
    """

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
    return get_dict_resultset(sql, params, ONE)


def get_bill(phone_number):
    # ToDo -> Just a placeholder
    sql = '''
        SELECT * FROM CALLS
    '''
    return get_dict_resultset(sql, None, ALL)
