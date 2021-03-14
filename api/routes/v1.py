from api.controllers import userController
from flask_restx import Namespace, Resource, reqparse

api = Namespace('v1', description='V1 API')

@api.route("/ping")
class User(Resource):
    def get(self):
        return userController.ping()