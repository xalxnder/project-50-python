from flask import render_template, redirect, url_for
from flask_wtf import FlaskForm

import requests
from app import app
import csv
from wtforms import *
from wtforms.validators import *


class MyForm(FlaskForm):
    name = StringField('Cafe Name', validators=[DataRequired()])
    location = StringField('Cafe Location', validators=[DataRequired(), URL()])
    opening_time = StringField('Opening Time', validators=[DataRequired()])
    closing_time = StringField('Closing Time', validators=[DataRequired()])
    rating = SelectField("Coffee Rating", choices=["☕️", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"], validators=[DataRequired()])
    wifi = SelectField('Wifi Strength Rating', choices=["💪🏾","💪🏾💪🏾","💪🏾💪🏾💪🏾","💪🏾💪🏾💪🏾💪🏾","💪🏾💪🏾💪🏾💪🏾💪🏾💪🏾"], validators=[DataRequired()])
    power = SelectField('Power Socket Availability', choices=["🔌","🔌🔌","🔌🔌🔌","🔌🔌🔌🔌","🔌🔌🔌🔌🔌"], validators=[DataRequired()])



    submit = SubmitField('Submit')



@app.route('/')
def index():
    blog_post_data = 'https://api.npoint.io/8595ea108855569b1d32'
    response = requests.get(blog_post_data)
    posts = response.json()
    return render_template('index.html', posts=posts)


@app.route('/cafes')
def cafes():
    with open('app/cafe-data.csv', 'r') as file:
        reader = csv.reader(file, delimiter=',')
        cafe_items = []
        for row in reader:
            cafe_items.append(row)
    return render_template('cafes.html', cafes=cafe_items)


@app.route('/add',methods=['GET', 'POST'])
def add():
    form = MyForm()
    if form.validate_on_submit():
        with open('app/cafe-data.csv', 'a' )as file:
            name = form.name.data
            location = form.name.data
            opening_time = form.opening_time.data
            closing_time = form.closing_time.data
            rating = form.rating.data
            wifi = form.wifi.data
            power=form.power.data
            file.write(f'\n{name},{location},{opening_time},{closing_time}, {rating},{wifi},{power}')
        return redirect(url_for('cafes'))


    return render_template('add.html', form=form)
