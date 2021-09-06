from flask import request, Flask
import json
app2 = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Second End Point'

if __name__ == '__main__':
    app2.run(debug=True, host='0.0.0.0')