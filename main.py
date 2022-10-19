from flask import Flask
from flask_restful import Api
from resources.qr import Qr

app = Flask(__name__)
api = Api(app)

api.add_resource(Qr, '/qr')

if __name__ == '__main__':
    app.run(debug=True)
