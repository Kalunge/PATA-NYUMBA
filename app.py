from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from db import db
from configs.config import Development

app = Flask(__name__)
db.init_app(app)

app.config.from_object(Development)


api = Api(app)

jwt = JWT(app)


if __name__ == "__main__":
    app.run(debug=True)