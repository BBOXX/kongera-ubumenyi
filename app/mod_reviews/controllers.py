import datetime as dt
from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_required, current_user
from app import db, app
from .models import Review, Objective
from .forms import ReviewForm
from app.mod_auth.models import User

# Define the blueprint
mod_reviews = Blueprint('reviews', __name__, url_prefix='/reviews', template_folder='templates')


# View all previous reviews
@mod_reviews.route('/', methods=['GET'])
@login_required
def get_reviews():
    # Right Screen - Details of the logged in users last review
    # my_review = Review.query.filter_by(reviewee=current_user)\
    #     .order_by(Review.review_date.desc())\
    #     .first()
    my_review = Review.query.first()

    # Left Screen - List of people on my team, their last view and button to start a new on

    return render_template(
        'mod_reviews/reviews.html',
        team_reviews=[x for x in range(10)],
        my_review=my_review
    )


# View a previous review
@mod_reviews.route('/person/<person_id>/review/<review_id>')
@login_required
def person(person_id, review_id):
    return person_id+review_id, 200


@mod_reviews.route('/person/<person_id>/review/create', methods=['GET', 'POST'])
@login_required
def create_review(person_id):

    review = Review(
        review_date = dt.datetime.now(),
        reviewee = None,
        reviewer = current_user,
        review_objectives=[]
    )

    review_form = ReviewForm()
    if review_form.validate_on_submit():
        try:
            for _ in review_form.review_objectives.entries:
                review.review_objectives.append(Objective())
            review_form.populate_obj(review)

            db.session.add(review)
            # for objective in review.review_objectives:
            #     db.session.add(objective)
            db.session.commit()
            flash("Review saved successfully 😀")
        except Exception as e:
            flash("Review was not able to be saved: "+str(e))

        return redirect(url_for('reviews.get_reviews'))

    # validate_on_submit = false for a GET request so return template
    return render_template(
        'mod_reviews/new_review.html',
        form=review_form
    )



# The manager/team view
@mod_reviews.route('/person/<person_id>/team')
def team(person_id):
    return person_id+" team", 200
