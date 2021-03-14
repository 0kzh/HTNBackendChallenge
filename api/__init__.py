from flask import Flask
from flask_restx import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from api.routes import api
from api.models import db
import os

app = Flask(__name__)
root_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(root_path, 'hackers.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api.init_app(app)
db.init_app(app)