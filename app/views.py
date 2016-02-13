from flask import render_template, url_for
from flask import request, jsonify, flash
from app import app, db
from app.models import User
from flask import views


@app.route('/')
@app.route('/home', methods=['POST', 'GET'])
def home():
        error = None
        if request.method == 'POST':
            username = request.form.get('username')
            email = request.form.get('email')
            if not all([username, email]):
                error = 'All label is required!'


                #return 'User created.'
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


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/user/<id>')
def product(id):
    user = User.query.get_or_404(id)
    return 'User - %s, $%s' % (user.username, user.email)


@app.route('/users')
def products():
    users = User.query.all()
    res = {}
    for user in users:
        res[user.id] = {
            'name': user.username,
            'mail': user.email
        }
    return jsonify(res)


@app.route('/user-create', methods=['POST',])
def create_user():
    name = request.form.get('name')
    mail = request.form.get('mail')
    user = User(name, mail)
    db.session.add(user)
    db.session.commit()
    return 'User created.'