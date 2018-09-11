from flask import jsonify, request, abort, Blueprint
from app.models import start_call, end_call, get_bill


bp_routes = Blueprint('routes', __name__)


@bp_routes.route('/call', methods=['POST'])
def call_record():
    js = request.get_json()
    call_type = js.get('type', '')
    if (call_type == 'start'):
        start_call(js)
    elif (call_type == 'end'):
        end_call(js)
    abort(404)


@bp_routes.route('/phone/<phone_number>/bill', methods=['GET'])
def get_phone_bill(phone_number):
    # ToDo: Need to insert period!
    get_bill(phone_number)
