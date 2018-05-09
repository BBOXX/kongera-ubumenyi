from app import db
from app.common.models import Base

class SkillGroup(Base):

    __tablename__ = "skill_group"

    name = db.Column(db.String(128))
    skills = db.relationship("Skill", backref="skill_group")


class Skill(Base):
    """ Data Model for a Skill, this object has a parent SKillGroup and Child SkillLevels   
    """
    __tablename__ = "skill"

    name = db.Column(db.String(128))
    skill_group_id = db.Column(db.Integer, db.ForeignKey('skill_group.id'))
    skill_levels = db.relationship('SkillLevel', backref='skill')

    reviews = db.relationship('ReviewSkill', backref='skill')

class SkillLevel(Base):

    __tablename__ = "skill_level"

    skill_id = db.Column(db.Integer, db.ForeignKey('skill.id')) # This+level must be unique
    level = db.Column(db.Integer) # add contraint between 0 - 4
    description = db.Column(db.String(512))

    # review_current_levels = db.relationship('reviewskill.current_level_id', backref='skill_level')
    # review_target_levels = db.relationship('reviewskill.target_level_id', backref='skill_level')

    __table_args__ = (
        db.CheckConstraint(level >= 0, name='level_constraint_ge_0'),
        db.CheckConstraint(level < 4, name='level_constraint_lt_4'),
        {})
