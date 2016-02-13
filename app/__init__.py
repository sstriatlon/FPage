import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.sqlite'  #'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

db.create_all()
from app import views