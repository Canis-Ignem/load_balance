from flask_restful import Resource, Api, reqparse
from flask import Flask


app1 = Flask(__name__)
api = Api(app1)

class Test(Resource):

    def get(self):
        
        return {'Data': 'This is endpoint one'}


api.add_resource(Test, '/test')





if __name__ == '__main__':
   app1.run(debug=True, host='0.0.0.0')
