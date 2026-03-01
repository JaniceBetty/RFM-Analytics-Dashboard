import os
from flask import Flask
from flaskplot.config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

# IMPORT MODELS FIRST
from flaskplot import models
from flaskplot import routes

# THEN create tables
with app.app_context():
    db.create_all()