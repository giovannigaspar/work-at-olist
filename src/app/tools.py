"""
Useful functions.

This module is responsible for some useful tools/functions that are used in the
application.
"""


from flask import abort


def numbers_only(s):
    """
    Filters a string and extract numbers from it.

    :param s: String to be analysed.
    :return: String containing numbers only.
    """

    n = '0123456789'
    r = ''
    for d in s:
        if d in n:
            r += d
    return r

def validate_phone_number(phone_number):
    """
    Validate the length of a phone number.

    :param phone_number: Number to be validated.

    :return: True if phone is valid or HTTP status code 500 if it's not.
    """

    p = numbers_only(phone_number)
    if ((len(p) != 10) and (len(p) != 11)):
        abort(500, "Invalid phone number!")
    return True

def validate_params(params, js):
    """
    Validate a list of parameters based on a JSON. If one of the required
    parameters is not present, the application will abort and return a HTTP
    status code 500 containing a message describing the missing parameter.

    :param params: List of the parameters to be analysed.
    :param js: JSON to be analysed.

    :return: True if all parameters are present or HTTP status code 500 if one
    or more is missing.
    """

    for param in params:
        if not js.get(param, None):
            abort(500, "Missing parameter " + str(param) +" in JSON")
    return True
