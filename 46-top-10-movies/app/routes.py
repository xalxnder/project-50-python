from flask import render_template, request, redirect, url_for
from . import app, models, db
from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *
from .movie_search import *


movie_api = MovieAPI()


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

    if request.args.get('id'):
        movie_id = request.args.get('id')
        movie_details = movie_api.get_movie_details(movie_id)
        title = movie_details['title']
        year = movie_details['year']
        description = movie_details['description']
        img_url = movie_details['image_url']
        new_movie = models.Movies(title=title, year=year, description=description, img_url=img_url)
        # test = models.Movies.query.get(movie_id)
        db.session.add(new_movie)
        db.session.commit()
        movies = models.Movies.query.get(movie_id)

        print(new_movie.id)
        return redirect(url_for('edit', id=new_movie.id))


    else:
        print('nay')
    for movie in all_movies:
        print(movie.title)
    print('here')
    return render_template('index.html', all_movies=all_movies)


@app.route('/add', methods=['GET', 'POST'])
def add():
    add_form = AddForm()
    if add_form.validate_on_submit():
        movie_title = request.form['movie_title']
        search_results = movie_api.search(movie_title)
        return render_template('select.html', search_results=search_results)
    return render_template('add.html', form=add_form)


# @app.route('/select')
# def select():
#     return render_template('select.html')


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
    return render_template('edit.html', form=form, movies=movies)


@app.route('/delete')
def delete():
    movie_id = request.args.get('id')
    movies = models.Movies.query.get(movie_id)
    db.session.delete(movies)
    db.session.commit()

    return render_template('index.html', movies=movies)
