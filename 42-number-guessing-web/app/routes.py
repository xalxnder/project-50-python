from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/correct')
def correct():
    return render_template('correct.html')

@app.route('/low')
def low():
    return render_template('low.html')

@app.route('/high')
def high():
    return render_template('high.html')