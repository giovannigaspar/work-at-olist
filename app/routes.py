from flask import jsonify, request, abort, Blueprint
from app.models import start_call, end_call, get_bill


bp_routes = Blueprint('routes', __name__)


@bp_routes.route('/call/<type>', methods=['POST'])
def call_record(type):
    if (type == 'start'):
        start_call(request.get_json())
    elif (type == 'end'):
        end_call(request.get_json())
    abort(404)


@bp_routes.route('/phone/<int: phone_number>/bill', methods=['GET'])
def get_phone_bill(phone_number):
    # ToDo: Need to insert period!
    get_bill(phone_number)