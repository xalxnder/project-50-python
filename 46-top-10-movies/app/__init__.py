from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"
bootstrap = Bootstrap5(app)

db = SQLAlchemy(app)
from . import routes


from. import models


with app.app_context():
    db.create_all()




