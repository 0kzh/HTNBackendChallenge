from flask import Flask
from flask_restx import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from api.routes import api
from api.models import skillModel, userModel
from api.models import db
import os

application = Flask(__name__)
root_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(root_path, 'hackers.db')
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api.init_app(application)
db.init_app(application)