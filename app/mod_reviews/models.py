from app import db
from app.common.models import Base
from app.mod_skills.models import Skill

class PeerReview(Base):
    pass

class Review(Base):

    __tablename__ = "review"

    reviewee = db.Column(db.Integer, db.ForeignKey('user.id'))
    review_date = db.Column(db.DateTime, default=db.func.current_timestamp())
    reviewer = db.Column(db.Integer, db.ForeignKey('user.id'))
    # Skill groups should specify which groups of skills are being evaluated in this review
    # skill_groups = [None]
    review_skills = db.relationship('ReviewSkill', backref='review')


# Each Review is made up of multiple skills
class ReviewSkill(Base):

    __tablename__ = "reviewskill"

    review_id = db.Column(db.Integer, db.ForeignKey('review.id'))
    skill_id = db.Column(db.Integer, db.ForeignKey('skill.id'))
    # current_level_id = db.Column(db.Integer, db.ForeignKey('skill_level.id'))
    # target_level_id = db.Column(db.Integer, db.ForeignKey('skill_level.id'))
    target_date = db.Column(db.DateTime)
    notes = db.Column(db.String(1024))
    
