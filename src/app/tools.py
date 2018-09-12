from flask import abort


def numbers_only(s):
    """
    Filters a string and extract numbers from it.

    :param s: String to be analised.
    :return: String containing numbers only.
    """

    n = '0123456789'
    r = ''
    for d in s:
        if d in n:
            r += d
    return r


def validate_params(params, js):
    """
    Validate a list of parameters based on a JSON. If one of the required
    parameters is not present, the application will abort and return a HTTP
    status code 500 containing a message describing the missing parameter.

    :param params: List of the parameters to be analised.
    :param js: JSON to be analised.

    :return: True if all parameters are present or HTTP status code 500 if one
    or more is missing.
    """

    for param in params:
        if not js.get(param, None):
            abort(500, "Missing parameter " + str(param) +" in JSON")
    return True
