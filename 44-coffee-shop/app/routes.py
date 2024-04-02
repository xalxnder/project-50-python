from flask import render_template, request
import requests
from app import app
from app.message_sender import *
import csv


@app.route('/')
def index():
    blog_post_data = 'https://api.npoint.io/8595ea108855569b1d32'
    response = requests.get(blog_post_data)
    posts = response.json()
    return render_template('index.html', posts=posts)


@app.route('/cafes')
def cafes():
    with open('app/cafe-data.csv', 'r') as file:
        reader = csv.reader(file)
        cafe_items = list(reader)
        print(cafe_items)
    return render_template('cafes.html', cafes=cafe_items)



