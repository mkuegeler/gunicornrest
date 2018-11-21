from flask import Flask
from flask_restplus import Resource, Api

application = Flask(__name__)
api = Api(application)

@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

@api.route('/start')
class HelloStart(Resource):
    def get(self):
        return {'start': 'now'}

if __name__ == '__main__':
    application.run(host='0.0.0.0')
    