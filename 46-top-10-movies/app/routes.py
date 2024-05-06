from flask import render_template, request, redirect
from . import app, models, db
from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *


class EditForm(FlaskForm):
    new_rating = IntegerField('Your Rating Out of 10 e.g. 7.5', validators=[DataRequired()])
    new_review = StringField('Your Review', validators=[DataRequired()])

    submit = SubmitField('Submit')


class AddForm(FlaskForm):
    movie_title = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField('Add Movie')


@app.route('/')
def index():
    all_movies = models.Movies.query.order_by(models.Movies.id).all()
    for movie in all_movies:
        print(movie.title)

    print('here')
    return render_template('index.html', all_movies=all_movies)


@app.route('/add', methods=['GET', 'POST'])
def add():
    add_form = AddForm()
    if add_form.validate_on_submit():
        return redirect('/')
    return render_template('add.html', form=add_form )


@app.route('/edit', methods=['GET', 'POST'])
def edit():
    form = EditForm()
    movie_id = request.args.get('id')
    movies = models.Movies.query.get(movie_id)
    if form.validate_on_submit():
        new_rating = request.form['new_rating']
        new_review = request.form['new_review']
        movies.rating = new_rating
        movies.review = new_review
        db.session.commit()
        return redirect('/')
        print(new_rating)
    return render_template('edit.html', form=form, movies=movies)


@app.route('/delete')
def delete():
    movie_id = request.args.get('id')
    movies = models.Movies.query.get(movie_id)
    db.session.delete(movies)
    db.session.commit()

    return render_template('index.html', movies=movies)
