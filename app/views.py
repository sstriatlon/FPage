from flask import render_template, url_for
from app import app
from flask import views


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/login')
def login():
    return render_template('login.html')