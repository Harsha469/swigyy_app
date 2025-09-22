from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api 
from flask_jwt_extended import JWTManager
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_SECRET_KEY"] = os.environ.get("JWT_SECRET_KEY", "fallback_secret")


db = SQLAlchemy(app)
api = Api(app)
jwt = JWTManager(app)


