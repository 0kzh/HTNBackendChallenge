from api import application
from api.models import db, userModel, skillModel
import json

DATA_FILE_PATH = "./hacker-data-2021.json"

def load_db_data():
    with application.app_context():
        db.create_all()
        with open(DATA_FILE_PATH) as f:
            data = json.load(f)
            populate_users(data)

def populate_users(data):
    for user in data:
        skills = user["skills"]

        new_user = userModel.User(
            name=user["name"],
            picture=user["picture"],
            company=user["company"],
            email=user["email"],
            phone=user["phone"]
        )

        db.session.add(new_user)
        db.session.flush()
        
        populate_skills_for_user(new_user.id, skills)

    db.session.commit()

def populate_skills_for_user(user_id, skills):
    for skill in skills:
        skill = skillModel.Skill(
            name=skill["name"],
            rating=skill["rating"],
            user_id=user_id
        )
        db.session.add(skill)

if __name__ == '__main__':
    load_db_data()
