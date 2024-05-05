from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"
bootstrap = Bootstrap5(app)
app.secret_key = 'abc'

db = SQLAlchemy(app)
from . import routes

from . import models

with app.app_context():
    # second_movie = models.Movies(
    #     title="Avatar The Way of Water",
    #     year=2022,
    #     description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
    #     rating=7.3,
    #     ranking=9,
    #     review="I liked the water.",
    #     img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
    # )
    # db.session.add(second_movie)
    # db.session.commit()
    db.create_all()
