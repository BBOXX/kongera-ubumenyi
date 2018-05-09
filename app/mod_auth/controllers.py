from app import app, db
from flask import Blueprint, request, render_template, redirect
from flask_login import LoginManager, login_user, login_required, logout_user
from .models import User

# Create the auth module Blueprint
mod_auth = Blueprint('mod_auth', __name__, url_prefix='/auth', template_folder='templates')

# Create the flask-login object
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'mod_auth.login'

# Callback to load user for flask-login module
@login_manager.user_loader
def load_user(user_id):
    if user_id == 'None':
        return None
    return User.query.filter_by(id=int(user_id)).first()


@mod_auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('mod_auth/login.html')
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if user is already in the users table
        user = User.query.filter_by(username=username).first()

        # If user not in user table, check AD and create
        if user is None:
            user = User(username, password)
            db.session.add(user)
            db.session.commit()

        if user is None:
            return "Incorrect Login", 401
        else:
            login_user(user)

            next = request.args.get('next')
            # TODO
            # is_safe_url should check if the url is safe for redirects.
            # See http://flask.pocoo.org/snippets/62/ for an example.
            # if not is_safe_url(next):
            #     return flask.abort(400)

            return redirect(next or '/')


@mod_auth.route("/logout", methods=['POST'])
@login_required
def logout():
    if request.method == 'POST':
        logout_user()
        return redirect('/auth/login')


