from flask_restful import Resource, Api, reqparse
import db_interface as dbi
from flask import Flask
import pandas as pd
from text_generation_chat_bot import run

app1 = Flask(__name__)
api = Api(app1)

class Chat(Resource):



    def post(self):
        parser = reqparse.RequestParser()
        
        parser.add_argument('text', required = True)
        
        args = parser.parse_args()
        
        response = run.evaluateInput(run.encoder, run.decoder, run.searcher, run.voc, args['text'])
        return {"data": response}


api.add_resource(Chat, '/users')





if __name__ == '__main__':
   app1.run(debug=True, host='0.0.0.0')
