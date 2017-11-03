from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

# Define an endpoint
class HealthCheck(Resource):
    def get(self):
        return {"message": "API is alive and helthy."}

# Route
api.add_resource(HealthCheck, '/check')

if __name__ == '__main__':
     app.run(port='5002')
