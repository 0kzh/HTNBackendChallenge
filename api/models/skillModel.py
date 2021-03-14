from api.models import db
from sqlalchemy import ForeignKey

class Skill(db.Model):
    __tablename__ = 'skill'
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))
    rating = db.Column(db.Integer)
    user = db.Column("User", ForeignKey('user.id'))