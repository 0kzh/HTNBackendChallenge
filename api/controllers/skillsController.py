from api.models import db
from api.models.skillModel import Skill
from api.util.helpers import makeSerializable
from sqlalchemy.sql.expression import func
from sqlalchemy import and_

# GET /skills
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