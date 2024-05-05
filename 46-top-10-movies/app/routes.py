from flask import render_template, request
from . import app, models, db
from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *


class EditForm(FlaskForm):
    new_rating = IntegerField('Your Rating Out of 10 e.g. 7.5', validators=[DataRequired()])
    new_review = StringField('Your Review', validators=[DataRequired()])

    submit = SubmitField('Submit')


@app.route('/')
def index():
    all_movies = models.Movies.query.order_by(models.Movies.id).all()
    for movie in all_movies:
        print(movie.title)

    print('here')
    return render_template('index.html', all_movies=all_movies)


@app.route('/edit', methods=['GET', 'POST'])
def edit():
    form = EditForm()
    method = request.method
    movie_id = request.args.get('id')
    movies = models.Movies.query.get(movie_id)

    if method == 'POST':
        new_rating = request.form['new_rating']
        print(new_rating)
    return render_template('edit.html', form=form, movies=movies)
