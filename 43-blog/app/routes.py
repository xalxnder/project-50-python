from flask import render_template, request
import requests
from app import app
from app.message_sender import *


@app.route('/')
def index():
    blog_post_data = 'https://api.npoint.io/8595ea108855569b1d32'
    response = requests.get(blog_post_data)
    posts = response.json()
    return render_template('index.html', posts=posts)


@app.route('/post/<int:post_id>')
def get_post(post_id):
    blog_post_data = 'https://api.npoint.io/8595ea108855569b1d32'
    response = requests.get(blog_post_data)
    posts = response.json()
    post = None
    for p in posts:
        if p['id'] == post_id:
            post = p
    return render_template('post.html', post=post)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact', methods=['POST', 'GET'])
def contact():
    method = request.method
    if method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        sender = MessageSender(message, email)
        sender.send_message()

    return render_template('contact.html', method=method)



