from db import db

class DishTag(db.Model):
    __tablename__ = "dish_tag"
    dish_id = db.Column(db.Integer, db.ForeignKey("dish.id"), primary_key=True)
    tag_id = db.Column(db.Integer, db.ForeignKey("tag.id"), primary_key=True)