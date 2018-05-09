from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_required
import os

app = Flask(__name__)
app.config.from_object('config')
    
db = SQLAlchemy(app)

# Homepage
@app.route('/')
@login_required
def index():
    return render_template('home.html')

@app.route('/healthcheck')
def heathcheck():
    return jsonify({'app': 'kongera-ubumenyi', 'status': 'okay'}), 200

# Load in the blueprint modules
from app.mod_auth.controllers import mod_auth as auth_module
app.register_blueprint(auth_module)

from app.mod_reviews.controllers import mod_reviews as reviews_module
app.register_blueprint(reviews_module)

from app.mod_admin.controllers import admin

# Create the database
db.create_all()


if app.config['DEBUG'] == True:
    from .common.test_data import populate_test_data    
    # If dev create some sample data
    populate_test_data()