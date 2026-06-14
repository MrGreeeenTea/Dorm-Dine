from db import db

class UserLanguage(db.Model):
    __tablename__ = "user_language"
    language_id = db.Column(db.Integer, db.ForeignKey("language.id"), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True)