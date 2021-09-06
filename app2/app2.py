from flask import request, Flask
from flask_restful import Resource, Api, reqparse
import json

app2 = Flask(__name__)
api = Api(app2)

class Users(Resource):

    def get(self):
        
        return "Hello2", 200

api.add_resource(Users, '/users')

if __name__ == '__main__':
   app2.run(debug=True, host='0.0.0.0')
