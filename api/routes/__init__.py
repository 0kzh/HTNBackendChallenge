from flask_restx import Api,Resource

from .v1 import api as ns

api = Api(title='Hack the North Hacker API', version='1.0', description='API for HTN Backend Challenge')

api.add_namespace(ns)