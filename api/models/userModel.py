from api.models import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))
    picture = db.Column(db.String(255))
    company = db.Column(db.String(255))
    email = db.Column(db.String(255))
    phone = db.Column(db.String(255))
    skills = db.relationship("Skill") # one to many

    def update(self, data):
        for k, v in data.items():
            setattr(self, k, v)
        return self