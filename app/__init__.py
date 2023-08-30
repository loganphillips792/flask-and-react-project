import os

from logging.config import dictConfig
from flask import Flask
from dotenv import load_dotenv


# def create_app():
app = Flask(__name__)

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

load_dotenv()

DATABASE_USER=os.environ.get('DATABASE_USERNAME')

print(f"database user is {DATABASE_USER}")

from . import routes