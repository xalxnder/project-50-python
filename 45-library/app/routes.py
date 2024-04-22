from flask import render_template, request, redirect
from . import app, models, db


@app.route('/')
def index():
    method = request.method
    book_id = request.args.get('id')
    if book_id:
        book = models.Books.query.get(book_id)
        db.session.delete(book)
        db.session.commit()
    all_books = models.Books.query.order_by(models.Books.title).all()
    for book in all_books:
        print(book.author)
    return render_template('index.html', all_books=all_books)


@app.route('/edit', methods=['GET', 'POST'])
def edit():
    method = request.method
    book_id = request.args.get('id')
    book = models.Books.query.get(book_id)
    if method == 'POST':
        new_rating = request.form['current-rating']
        book.rating = new_rating
        db.session.commit()
        return redirect('/')

    return render_template('edit.html', book=book)


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
        return redirect('/')

    return render_template('add.html', )