
from flask import request, render_template, redirect
from flaskauth import app
from UserModel import User

import flask_login

login_manager = flask_login.LoginManager()
login_manager.init_app(app)

# Login Manager configuration
login_manager.session_protection = "strong"
login_manager.login_view = "homepage"


@login_manager.user_loader
def load_user(user_id):
    user = User()
    user.id = user_id
    return user


# Basic routes
@app.route('/login')
def login_static():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    if request.method == "POST":
        email = request.form['email']
        passwd = request.form['password']

        # Create login logic and proceed with the authentication
        user_class = User()
        user_class.id = email
        flask_login.login_user(user_class)

    return redirect('/protected')


@app.route('/logout')
@flask_login.login_required
def logout():
    flask_login.logout_user()
    return redirect('/')


# Protected routes
@app.route('/protected')
@flask_login.login_required
def protected():
    return 'Logged in as: ' + flask_login.current_user.id
