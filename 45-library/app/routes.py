from flask import render_template, request, redirect
from . import app, models, db

all_books = []


@app.route('/')
def index():
    print(all_books)
    return render_template('index.html', all_books=all_books)


@app.route('/add', methods=['GET', 'POST'])
def add():
    method = request.method
    print(method)
    if method == 'POST':
        title = request.form['book-title']
        author = request.form['book-author']
        rating = request.form['book-author']
        new_book = models.Books(title=title, author=author, rating=rating)
        db.session.add(new_book)
        db.session.commit()
        print(all_books)
        return redirect('/')

    return render_template('add.html', )
