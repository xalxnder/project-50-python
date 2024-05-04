from flask import render_template, request
from . import app, models, db


@app.route('/')
def index():
    print('here')
    return render_template('index.html')
