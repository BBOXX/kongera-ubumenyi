from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from app import app, db
from app.mod_skills.models import Skill, SkillLevel, SkillGroup
from app.mod_reviews.models import Review, ReviewSkill

admin = Admin(app, name='admin-kongera-ubumenyi', template_mode='bootstrap3')

class BaseModelView(ModelView):
    form_excluded_columns = ['date_created', 'date_modified']


# The admin panel for editing skills and groups
# TODO split this file across each modules controllers, doesn't need to be centrallised

class SkillModelView(BaseModelView):
    inline_models = [(SkillLevel, dict(form_columns=['id', 'level', 'description']))]
admin.add_view(SkillModelView(Skill, db.session))

class SkillGroupModelView(BaseModelView):
    inline_models = [(Skill, dict(form_columns=['id', 'name']))]
admin.add_view(SkillGroupModelView(SkillGroup, db.session))

# The admin panel for reviews - replace with a custom view for production
class ReveiwModelView(BaseModelView):
    """ Customise the view for the Review object """
    inline_models = [(ReviewSkill, dict(form_columns=[
        'skill',
        'target_date',
        'notes']))]
admin.add_view(ReveiwModelView(Review, db.session))
