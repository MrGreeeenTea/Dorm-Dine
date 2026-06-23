from db import db

class DishPhoto(db.Model):
    __tablename__ = "dish_photo"
    id = db.Column(db.Integer, primary_key=True)
    dish_id = db.Column(db.Integer, db.ForeignKey("dish.id"), nullable=True)
    photo_url = db.Column(db.String, nullable=True)

    dish = db.relationship("Dish", backref="photos")