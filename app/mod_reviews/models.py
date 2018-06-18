from sqlalchemy.orm import relationship

from app import db
from app.common.models import Base
from app.mod_auth.models import User
from app.mod_skills.models import Skill

class Review(Base):

    __tablename__ = "review"

    review_date = db.Column(db.DateTime, default=db.func.current_timestamp())

    reviewee_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    reviewee = relationship("User", foreign_keys=[reviewee_id])

    reviewer_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    reviewer = relationship("User", foreign_keys=[reviewer_id])

    # Skill groups should specify which groups of skills are being evaluated in this review
    # skill_groups = [None]

    review_objectives = db.relationship('Objective', backref='review')

# Each Review is made up of multiple skills
class Objective(Base):

    __tablename__ = "objective"

    review_id = db.Column(db.Integer, db.ForeignKey('review.id'))
    skill_id = db.Column(db.Integer, db.ForeignKey('skill.id'))
    # current_level_id = db.Column(db.Integer, db.ForeignKey('skill_level.id'))
    # target_level_id = db.Column(db.Integer, db.ForeignKey('skill_level.id'))
    target_date = db.Column(db.DateTime)
    notes = db.Column(db.String(1024))
