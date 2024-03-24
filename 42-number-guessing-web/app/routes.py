from flask import render_template, redirect, blueprints
from app import app
from .logic import *


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<int:user_guess>')
def user_input(user_guess):
    answer = guess_number(user_guess)
    if answer == 'low':
        return redirect('/low')
    elif answer == 'high':
        return redirect('/high')
    else:
        return redirect('/correct')


@app.route('/correct')
def correct():
    return render_template('correct.html')


@app.route('/low')
def low():
    return render_template('low.html')


@app.route('/high')
def high():
    return render_template('high.html')
