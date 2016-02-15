from flask import render_template, session
from flask import request, jsonify, flash, redirect, url_for
from app import app, db, util
from app.models import User
import sqlite3
from flask import views

app.config.update(dict(
    USERNAME='sstriatlon',
    EMAIL='sstriatlon@gmail.com'
))

@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['email'] != app.config['EMAIL']:
            error = 'Invalid email'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('home'))
    return render_template('login.html', error=error)


@app.route('/home', methods=['POST', 'GET'])
def home():
        error = None
        if request.method == 'POST':
            username = request.form.get('username')
            email = request.form.get('email')
            if not all([username, email]):
                error = 'All label is required!'
            elif User.query.filter_by(username=username).first():
                error = 'This username has been registered!'
            elif User.query.filter_by(email=email).first():
                error = 'This email has been registered!'
            else:
                user = User(username, email)
                db.session.add(user)
                db.session.commit()
                error = 'User created.'

        return render_template('home.html',error = error)

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/user/<id>')
def product(id):
    user = User.query.get_or_404(id)
    return 'User - %s, $%s' % (user.username, user.email)


@app.route('/users')
def users():
    users = util.get_users()
    return render_template('users.html', data=users)


@app.route('/user-create', methods=['POST',])
def create_user():
    name = request.form.get('name')
    mail = request.form.get('mail')
    user = User(name, mail)
    db.session.add(user)
    db.session.commit()
    return 'User created.'