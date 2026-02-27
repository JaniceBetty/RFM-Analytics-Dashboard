import os
from flask import Flask
from flaskplot.config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

from flaskplot import routes