from db import db

class Dorm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    district = db.Column(db.String, nullable=False)
    postcode = db.Column(db.String, nullable=False)
    place = db.Column(db.String, nullable=False)

    users = db.relationship( "User", back_populates="dorm")