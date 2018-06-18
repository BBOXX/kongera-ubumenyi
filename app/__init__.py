import os
from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_required

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


from app.mod_admin.controllers import admin
from app.mod_auth.models import *
from app.mod_reviews.models import *
from app.mod_reviews.models import *

# Create the database
if app.config['DEBUG']:
    app.logger.info("Dropping and recreating db")
    # db.drop_all()
    db.create_all()

    from .common.test_data import populate_test_data
    # If dev create some sample data
    populate_test_data()
else:
    db.create_all()


# Load in the blueprint modules
from app.mod_auth.controllers import mod_auth as auth_module
app.register_blueprint(auth_module)

from app.mod_reviews.controllers import mod_reviews as reviews_module
app.register_blueprint(reviews_module)

