from flask_restful import Resource, Api, reqparse
import db_interface as dbi
from flask import Flask
import pandas as pd

app1 = Flask(__name__)
api = Api(app1)

class Chat(Resource):



    def post(self):
        parser = reqparse.RequestParser()
        
        parser.add_argument('text', required = True)
        
        args = parser.parse_args()
        
        if dbi.add_user(args['user'], args['pas'], args['email'], args['DoB'], args['country'], args['batch'], args['gender'] ):
            return {'data': args}, 200
        else:
            return "Data format error", 403


api.add_resource(Chat, '/users')





if __name__ == '__main__':
   app1.run(debug=True, host='0.0.0.0')
