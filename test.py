from flask import flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)