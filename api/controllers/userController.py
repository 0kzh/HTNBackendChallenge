from api.models import db
from api.models.userModel import User
from api.models.skillModel import Skill
from api.util.helpers import makeSerializable

# internal function to get skills for a user
def _get_skills_for_user(user_obj):
    skills = []
    for skill in user_obj.skills:
        skills.append({
            'name': skill.name,
            'rating': skill.rating,
        })
    return skills    

def _validate_skills(skills):
    for skill in skills:
        if not "name" in skill or not "rating" in skill:
            return False
    return True

# GET /users
def fetch_all_users():
    users = User.query.all()
    res = []

    for user in users:
        user_json = makeSerializable(user)
        user_json["skills"] = _get_skills_for_user(user)
        res.append(user_json)

    return res

# POST /users
def add_user(name, picture, company, email, phone, skills):
    if not _validate_skills(skills):
        return "Need to specify a name and rating for all skills!", 400

    new_user = User(
        name=name,
        picture=picture,
        company=company,
        email=email,
        phone=phone
    )
    db.session.add(new_user)
    db.session.flush()

    for skill in skills:
        skill = Skill(
            name=skill["name"],
            rating=skill["rating"],
            user_id=new_user.id
        )
        db.session.add(skill)

    db.session.commit()
    
    user_json = makeSerializable(new_user)
    user_json["skills"] = _get_skills_for_user(new_user)

    return user_json

# GET /users/:id
def fetch_user(id):
    user = User.query.get(id)

    if not user:
        return "User not found", 404

    user_json = makeSerializable(user)
    user_json["skills"] = _get_skills_for_user(user)

    return user_json

# PUT /users/:id
def update_user(id, data):
    user = User.query.get(id)

    if "skills" in data:
        skills = data["skills"]
        for skill_data in skills:
            if not "name" in skill_data or not "rating" in skill_data:
                return "Need to specify a name and rating for all skills!", 400

            skill = Skill.query.filter(Skill.user_id == id, Skill.name == skill_data["name"])
            if skill:
                # update
                skill.update({ "rating": skill_data["rating"] })
            else:
                # insert
                new_skill = Skill(
                    name=skill["name"],
                    rating=skill["rating"],
                    user_id=id
                )
                db.session.add(new_skill)
                
        del data["skills"] # delete before modifying `User` model
    
    new_user = user.update(data)
    db.session.commit()

    user_json = makeSerializable(new_user)
    user_json["skills"] = _get_skills_for_user(new_user)
    
    return user_json