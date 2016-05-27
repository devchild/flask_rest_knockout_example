from flask import Flask
from flask.ext.httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()
app = Flask(__name__)
app.config.from_object('config')

from app import views
from app.api import v1_0
