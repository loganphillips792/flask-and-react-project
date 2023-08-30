import os

from logging.config import dictConfig
from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

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

SQLALCHEMY_DATABASE_URI=os.environ.get('SQLALCHEMY_DATABASE_URI')

db = SQLAlchemy()

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

print(f"database url for sqlalchemy is {SQLALCHEMY_DATABASE_URI}")

db.init_app(app)

from . import routes