from flask_restful import Resource


class Qr(Resource):
    def get(self):
        return {'id': '1', 'tipo': 'ap', 'valor': "https://google.com"}
