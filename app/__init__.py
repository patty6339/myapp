from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.auth import init_oidc

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


init_oidc(app)
