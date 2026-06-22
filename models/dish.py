from db import db

class Dish(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cook_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    icon_id = db.Column(db.Integer, db.ForeignKey("icon.id"), nullable=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=True)
    price = db.Column(db.Float, nullable=False)
    total_portions = db.Column(db.Integer, nullable=False)
    left_portions = db.Column(db.Integer, nullable=True)
    pickup_time = db.Column(db.DateTime, nullable=False)
    pickup_timeend = db.Column(db.DateTime, nullable=True)
    created_at = db.Column(db.DateTime, default=db.func.now())
    status = db.Column(db.String, nullable=False, default='scheduled')
    ingredients = db.Column(db.String, nullable=True) #could also use db.text
    dish_orders = db.relationship("DishOrder", back_populates="dish")