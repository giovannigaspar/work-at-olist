__author__ = "Giovanni Gaspar"
__version__ = "0.1"
__maintainer__ = "Giovanni Gaspar"
__email__ = "giovannigaspar@outlook.com"
__status__ = "Development"


from flask import Flask
from app import config
from app.routes import bp_routes


app = Flask(__name__) # Flask default syntax
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
