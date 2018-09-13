"""
Database module.

Module responsible for all the database operations: configure, connect, execute
"""


import os
import psycopg2
import psycopg2.extras


# Control variables
ONE = 1
ALL = 2


# Database connection using enviroment variables (see file exports.sh)
conn = psycopg2.connect(
    host='localhost',
    dbname=os.getenv('DATABASE_NAME'),
    user=os.getenv('DATABASE_USER'),
    password=os.getenv('DATABASE_PASSWORD')
)


def get_dict_resultset(sql, param, results):
    """
    Execute a database operation and return the results (if applicable) as
    a dictionary.

    If the operation is well succeeded, a "commit" operation will be made in
    the database. Otherwise, a "rollback" operation will be made.

    :param sql: SQL instruction to be executed.
    :param param: SQL parameters.
    :param results: Number of expected results.
    (ONE -> one result, ALL -> More than one result. None -> No result)

    :return: Formatted dictionary containing the expected returning values or
    "None" if the execution fails.
    """

    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    ans = None
    dict_result = []

    try:
        cur.execute(sql, param)
    except Exception as e:
        cur.execute('ROLLBACK')
        print(str(e)) # Debug
        return None

    if results == ONE:
        ans = cur.fetchone()
        if ans:
            dict_result.append(dict(ans))
            cur.execute('COMMIT')
            return dict_result[0]
    elif results == ALL:
        ans = cur.fetchall()
        if ans:
            for row in ans:
                dict_result.append(dict(row))
            cur.execute('COMMIT')
            return dict_result
    return None
