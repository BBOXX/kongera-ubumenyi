from app.mod_reviews.models import Review, Objective
from app.mod_skills.models import SkillGroup, Skill, SkillLevel
from app import db

def populate_test_data():
    
    # Add skills and skill groups
    if len(SkillGroup.query.filter_by(name="Numeric Skills").all()) == 0:
        numeric_skill_group = SkillGroup(name="Numeric Skills")
        db.session.add(numeric_skill_group)
        db.session.flush()
        skill = Skill(name="Addition", skill_group_id=numeric_skill_group.id)
        db.session.add(skill)
        db.session.flush()
        db.session.add(SkillLevel(level=0, description="Addition level 0", skill_id=skill.id))
        db.session.add(SkillLevel(level=1, description="Addition level 1", skill_id=skill.id))
        db.session.add(SkillLevel(level=2, description="Addition level 2", skill_id=skill.id))
        db.session.add(SkillLevel(level=3, description="Addition level 3", skill_id=skill.id))

        skill = Skill(name="Subtraction", skill_group_id=numeric_skill_group.id)
        db.session.add(skill)
        db.session.flush()
        db.session.add(SkillLevel(level=0, description="Subtraction level 0", skill_id=skill.id))
        db.session.add(SkillLevel(level=1, description="Subtraction level 1", skill_id=skill.id))
        db.session.add(SkillLevel(level=2, description="Subtraction level 2", skill_id=skill.id))
        db.session.add(SkillLevel(level=3, description="Subtraction level 3", skill_id=skill.id))

        skill = Skill(name="Division", skill_group_id=numeric_skill_group.id)
        db.session.add(skill)
        db.session.flush()
        db.session.add(SkillLevel(level=0, description="Division level 0", skill_id=skill.id))
        db.session.add(SkillLevel(level=1, description="Division level 1", skill_id=skill.id))
        db.session.add(SkillLevel(level=2, description="Division level 2", skill_id=skill.id))
        db.session.add(SkillLevel(level=3, description="Division level 3", skill_id=skill.id))

        db.session.commit()

    # Add a second skill group with skills and level descriptions
    if len(SkillGroup.query.filter_by(name="Verbal Skills").all()) == 0:
        verbal_skills_group = SkillGroup(name="Verbal Skills")
        db.session.add(verbal_skills_group)
        db.session.flush()
        db.session.add(Skill(name="Whispering", skill_group_id=verbal_skills_group.id))
        db.session.add(Skill(name="Talking", skill_group_id=verbal_skills_group.id))
        db.session.add(Skill(name="Shouting", skill_group_id=verbal_skills_group.id))
        db.session.commit()

    # Add some reviews
