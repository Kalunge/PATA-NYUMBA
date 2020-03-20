from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from db import db


from configs.config import Development
from security import authenticate, identity
from resources.landlord import LandLord, LandLordList

app = Flask(__name__)
db.init_app(app)

app.config.from_object(Development)

@app.before_first_request
def create_tables():
    db.create_all()


api = Api(app)

jwt = JWT(app, authenticate, identity)

api.add_resource(LandLordList, '/landlords')
api.add_resource(LandLord, '/landlord')


if __name__ == "__main__":
    app.run(debug=True)