import os
from flask import Flask
from flaskplot.config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

with app.app_context():
    db.create_all()

from flaskplot import routes