"""
Main application module.

Configures the "FLASK" framework and registers the URLs used by the
application.
"""


__author__ = "Giovanni Gaspar"
__version__ = "0.1"
__maintainer__ = "Giovanni Gaspar"
__email__ = "giovannigaspar@outlook.com"
__status__ = "Development"


from flask import Flask
from flask.json import JSONEncoder
from datetime import timedelta, datetime, date, time
from app import config
from app.routes import bp_routes


# Custom JSON encoder, since, by default, FLASK won't decode the timestamps
# the way it is needed in this application.
class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        try:
            if isinstance(obj, timedelta):
                t = str(obj).split(':')
                return (t[0]+'h:')+(t[1]+'m:')+(t[2]+'s')
            if isinstance(obj, datetime):
                return obj.isoformat()
            if isinstance(obj, date):
                return str(obj)
            if isinstance(obj, time):
                return str(obj)
        except TypeError:
            pass
        return super().default(obj)


app = Flask(__name__) # Flask default syntax
app.json_encoder = CustomJSONEncoder # Defining a custom JSONEncoder
app.config.from_object(config) # Getting APP configs from file
app.jinja_env.cache = {} # Disabling some caches for better performance


@app.route('/')
def home():
    return "Hi there!!! Welcome to my app ;)"

@app.route('/version')
def get_version():
    """
    Get app version.

    :return: App version.
    """
    return __version__


# Registering routes
app.register_blueprint(bp_routes)
