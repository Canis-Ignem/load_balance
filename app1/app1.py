from flask_restful import Resource, Api, reqparse
import db_interface as dbi
from flask import Flask
import pandas as pd

app1 = Flask(__name__)
api = Api(app1)

class Users(Resource):

    def get(self):
        data = dbi.get_all_users()
        return data, 200

    def post(self):
        parser = reqparse.RequestParser()
        
        parser.add_argument('user', required = True)
        parser.add_argument('pas', required = True)
        parser.add_argument('email', required = True)
        parser.add_argument('DoB', required = True)
        parser.add_argument('country', required = True)
        parser.add_argument('batch', required = True)
        parser.add_argument('gender', required = True)
        
        args = parser.parse_args()
        
        if dbi.add_user(args['user'], args['pas'], args['email'], args['DoB'], args['country'], args['batch'], args['gender'] ):
            return {'data': args}, 200
        else:
            return "Data format error", 403

    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email', required = True)
        parser.add_argument('user', required = False)
        parser.add_argument('pas', required = False)
        parser.add_argument('DoB', required = False)
        parser.add_argument('country', required = False)
        parser.add_argument('batch', required = False)
        parser.add_argument('gender', required = False)
        args = parser.parse_args()


        
        if dbi.get_user(args["email"]):

            res = dbi.update_user(args["email"], pd.DataFrame(args.values(),columns=["values"], index=args.keys() ) )
            if res:
                return {'data':res}, 200
            else:
                return "Data format error", 403

        else:
            
            return {
                'message': f"'{args['email']}' user not found."
            }, 404
class Batches(Resource):

    def get(self):
        data = dbi.get_all_batches()
        return {'data': data}, 200

api.add_resource(Users, '/users')
api.add_resource(Batches, '/batches')




if __name__ == '__main__':
   app1.run(debug=True, host='0.0.0.0')
