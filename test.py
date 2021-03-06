from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

users = [
    {
        "name": "Nicholas",
        "age": 41,
        "address": "CA"
    },
        {
        "name": "Han",
        "age": 19,
        "address": "LA"
    },
        {
        "name": "John",
        "age": 56,
        "address": "ND"
    }
]

class User(Resource):
    def get(self,name):
        if name is None:
            return users,200

        for user in users:
            if(name == user["name"]):
                return user,200
        return "User not found", 404

    def post(self,name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("address")
        args = parser.parse_args()

        for user in users:
            if(name == user["name"]):
                return "User with name {} already exists".format(name), 400
        
        user = {
            "name": name,
            "age": args["age"],
            "address": args["address"],
        }
        users.append(user)
        return user, 201

    def put(self,name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("address")
        args = parser.parse_args()

        for user in users:
            if(name == user["name"]):
                user["age"] = args["age"]
                user["address"] = user["address"]
                return user, 200
        
        user = {
            "name": name,
            "age": args["age"],
            "address": args["address"],
        }
        users.append(user)
        return user, 201

    def delete(self,name):
        global users
        users = [user for user in users if user["name"] != name]
        return "{} is deleted.".format(name), 200

api.add_resource(User, "/user/<string:name>")

app.run(debug=True)

