from flask import Flask
from flask_restx import Resource, Api
from api.routes import api

import sqlite3
conn = sqlite3.connect('hackers.db')

app = Flask(__name__)
api.init_app(app)