__author__ = "Giovanni Gaspar"
__version__ = "0.1"
__maintainer__ = "Giovanni Gaspar"
__email__ = "giovannigaspar@outlook.com"
__status__ = "Development"


from flask import Flask
from app import config


app = Flask(__name__)
app.config.from_object(config)
app.jinja_env.cache = {}


@app.route('/')
def login_page():
    return 'Hello World!'
