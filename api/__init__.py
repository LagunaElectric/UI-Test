from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os


basedir: str = os.path.abspath(os.path.dirname(__file__))

app: Flask = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = (
    os.environ.get("DATABASE_URL") or
    "sqlite:///" + os.path.join(basedir, "app.db")
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db: SQLAlchemy = SQLAlchemy(app)
migrate = Migrate(app, db)

from api import models, routes