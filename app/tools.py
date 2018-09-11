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
