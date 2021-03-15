from api.models import db
from api.models.userModel import User
from api.models.skillModel import Skill
from api.util.helpers import makeSerializable
from api.controllers.userController import _get_skills_for_user
from sqlalchemy.sql.expression import func
from sqlalchemy import and_

# GET /skills
# returns list of skills and their frequencies
# `min_frequency` and `max_frequency` are optional
def get_skills(min_frequency, max_frequency):
    count = func.count()

    filters = []
    if min_frequency:
        filters.append(count >= min_frequency)
    if max_frequency:
        filters.append(count <= max_frequency)

    skill_counts = db.session.query(Skill.name, count)\
                             .group_by(Skill.name)\
                             .having(and_(*filters))\
                             .all()
    
    res = []
    for skill in skill_counts:
        skill_json = {
            "name": skill[0],
            "frequency": skill[1]
        }
        res.append(skill_json)

    return res


# GET /skills/<skill_name>
# returns the list of users and their ratings for a certain skill, sorted in descending order
def get_skill(name):
    skills = Skill.query.filter(Skill.name == name).order_by(Skill.rating.desc())

    res = []
    for skill in skills:
        user = User.query.get(skill.user_id)
        user_json = makeSerializable(user)
        user_json["skills"] = _get_skills_for_user(user)
        skill_json = {
            "rating": skill.rating,
            "user": user_json
        }
        res.append(skill_json)

    return res
