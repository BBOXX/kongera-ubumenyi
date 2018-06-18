from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, TextAreaField, FormField, FieldList
from  wtforms.fields.html5 import DateField
from app.mod_skills.models import Skill
from app.mod_auth.models import User

class AttributeDict(dict):
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__


class ObjectiveForm(FlaskForm):

    skills = [(skill.id, skill.skill_group.name+" - "+skill.name) for skill in Skill.query.all()]

    skill_id = SelectField("Skill", choices=skills, coerce=int)
    target_date = DateField(label="Target Date")
    notes = TextAreaField(label="Notes")

class ReviewForm(FlaskForm):

    review_date = DateField(label="Review Date")
    review_objectives = FieldList(
        FormField(
            ObjectiveForm
            # default=lambda: AttributeDict(skill_select=None, target_date=None, notes="")
        ),
        max_entries=10,
        min_entries=2
    )

    submit = SubmitField(label="Submit")

