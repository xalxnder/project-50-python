from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from . import models
from . import routes, models

app = Flask(__name__)


"""
Only need this section if utilizing a database. 

 app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db_name.db"
 db = SQLAlchemy(app)
 with app.app_context():
     db.create_all()

"""
