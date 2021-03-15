from api.controllers import userController,skillsController
from flask_restx import Namespace, Resource, reqparse

api = Namespace('v1', description='V1 API')

@api.route("/users")
class Users(Resource):
    def get(self):
        return userController.fetch_all_users()
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True)
        parser.add_argument('picture', type=str, required=True)
        parser.add_argument('company', type=str, required=True)
        parser.add_argument('email', type=str, required=True)
        parser.add_argument('phone', type=str, required=True)
        parser.add_argument('skills', type=dict, action="append", required=True) 

        return userController.add_user(**parser.parse_args())

@api.route("/users/<id>")
class User(Resource):
    def get(self, id):
        return userController.fetch_user(id)

    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, store_missing=False)
        parser.add_argument('picture', type=str, store_missing=False)
        parser.add_argument('company', type=str, store_missing=False)
        parser.add_argument('email', type=str, store_missing=False)
        parser.add_argument('phone', type=str, store_missing=False)
        parser.add_argument('skills', type=dict, action="append", store_missing=False)

        return userController.update_user(id, parser.parse_args())

@api.route("/skills")
class Skills(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('min_frequency', type=int)
        parser.add_argument('max_frequency', type=int)
        return skillsController.get_skills(**parser.parse_args())

@api.route("/skills/<name>")
class Skill(Resource):
    def get(self, name):
        return skillsController.get_skill(name)