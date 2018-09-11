# ToDo: Validations

from app.db import get_dict_resultset, ONE, ALL


def start_call(js):
    sql = '''
        INSERT INTO CALLS (
            timestamp_begin,
            call_id,
            source,
            destination
        ) VALUES (%s, %s, %s, %s)
        RETURNING id
    '''
    param = (
        js.get('timestamp'),
        js.get('call_id'),
        js.get('source'),
        js.get('destination')
    )
    return get_dict_resultset(sql, param, ONE)


def end_call(js):
    sql = '''
        UPDATE CALLS SET
            timestamp_end=%s,
        WHERE call_id=%s
        RETURNING id
    '''
    param = (
        js.get('timestamp'),
        js.get('call_id')
    )
    return get_dict_resultset(sql, param, ONE)


def get_bill(phone_number):
    # ToDo
    sql = '''
    '''
    return