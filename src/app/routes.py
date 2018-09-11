from flask import jsonify, request, abort, Blueprint
from app.models import start_call, end_call, get_bill


bp_routes = Blueprint('routes', __name__)


@bp_routes.route('/call', methods=['POST'])
def call_record():
    """
    Route used to start/end a call. Receives a JSON contaning
    """
    js = request.get_json()
    call_type = js.get('type', '')
    r = None
    if (call_type == 'start'):
        r = start_call(js)
    elif (call_type == 'end'):
        r = end_call(js)
    return jsonify(objects=r) if r else abort(500)


@bp_routes.route('/phone/<phone_number>/bill', methods=['GET'])
def get_phone_bill(phone_number):
    # ToDo: Need to insert period!
    get_bill(phone_number)
