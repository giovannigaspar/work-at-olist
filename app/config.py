import os

# Can be set to false to suppress some excessive logs once the app is ready
DEBUG = True
SECRET_KEY = os.getenv('FLASK_SECRET_KEY')

