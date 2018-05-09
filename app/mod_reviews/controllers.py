from flask import Blueprint, render_template
from app import db
from .models import Review

# Define the blueprint
mod_reviews = Blueprint('reviews', __name__, url_prefix='/reviews', template_folder='templates')

# View all previous reviews
@mod_reviews.route('/', methods=['GET'])
def get_reviews():
    # Right Screen - Details of the logged in users last review
    my_review = Review.query.first()

    # Left Screen - List of people on my team, their last view and button to start a new on


    return render_template(
        'mod_reviews/reviews.html',
        team_reviews=[x for x in range(10)],
        my_review=my_review
    )

# View a previous review
@mod_reviews.route('/person/<person_id>/review/<review_id>')
def person(person_id, review_id):
	return person_id+review_id, 200

@mod_reviews.route('/person/<person_id>/review/create', methods=['GET', 'POST'])
def create_review(person_id):
    if request.method == 'GET':
        return render_template(
            'mod_reviews/new_review.html'
        )
    elif request.method == 'POST':
        # ToDo: Show a flash to confirm it's been saved
        # return redirect
        return "thanks"


# The manager/team view
@mod_reviews.route('/person/<person_id>/team')
def team(person_id):
	return person_id+" team", 200