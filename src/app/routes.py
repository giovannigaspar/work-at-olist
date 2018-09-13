import datetime
from flask import request, abort, Blueprint
from app.models import start_call, end_call, get_bill
from app.tools import validate_phone_number


bp_routes = Blueprint('routes', __name__)


@bp_routes.route('/call', methods=['POST'])
def call_record():
    """
    Route used to start/end a call.
    Receives a JSON contaning the following information:

        "type":  Indicate if it's a call "start" or "end" record;
        "timestamp":  The timestamp of when the event occured;
        "call_id":  Unique for each call record pair;
        "source"*:  The subscriber phone number that originated the call;
        "destination"*:  The phone number receiving the call.

    * Not required for the type "end".

    If any of the required items is not present, return a HTTP response status
    code 500 contaning a custom message.
    """

    js = request.get_json()
    call_type = js.get('type', '')
    r = None
    if (call_type == 'start'):
        r = start_call(js)
    elif (call_type == 'end'):
        r = end_call(js)
    return r if r else abort(500, "Invalid JSON")


@bp_routes.route('/phone/<phone_number>/bill', methods=['GET'])
def get_phone_bill(phone_number):
    """
    Route to get a subscriber bill.
    Receibe the subscriber phone number in the URL and the period as an
    argument.

    For example: http://localhost/phone/99988526423/bill?period=12/2017
    """
    period = request.args.get('period', None)
    now = datetime.datetime.now()
    if not period:
        month = (now.month-1) if (now.month > 1) else 12
        year = (now.year) if (month != 12) else (now.year-1)
        period = (str(month)+'/'+str(year))
    else:
        period = period.lstrip('0')
        if (period == (str(now.month)+'/'+str(now.year))):
            abort(500, 'The current period is not yet closed!')
    print(period)
    validate_phone_number(phone_number)
    r = get_bill(phone_number, period)
    return r if r else abort(500)
