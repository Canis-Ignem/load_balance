from flask_restful import Resource, Api, reqparse
from flask import Flask
import pandas as pd


app2 = Flask(__name__)
api = Api(app2)

class Test(Resource):

    def get(self):
        
        return {'Data': 'This is endpoint two'}


api.add_resource(Test, '/test')


if __name__ == '__main__':
   app2.run(host='0.0.0.0')
