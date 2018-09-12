__author__ = "Giovanni Gaspar"
__version__ = "0.1"
__maintainer__ = "Giovanni Gaspar"
__email__ = "giovannigaspar@outlook.com"
__status__ = "Development"


from flask import Flask
from flask.json import JSONEncoder
from datetime import timedelta, datetime
from app import config
from app.routes import bp_routes


# Custom JSON encoder, since, by default, FLASK won't decode a datetime as ISO
class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        try:
            #if isinstance(obj, timedelta):
            #    return str(obj)
            if isinstance(obj, datetime):
                return obj.isoformat()
        except TypeError:
            pass
        return super().default(obj)


app = Flask(__name__) # Flask default syntax
app.json_encoder = CustomJSONEncoder
app.config.from_object(config) # Getting APP configs from file
app.jinja_env.cache = {} # Disabling some caches for better performance


@app.route('/version')
def get_version():
    """
    Get app version.

    :return: App version.
    """
    return __version__


# Registering routes
app.register_blueprint(bp_routes)
