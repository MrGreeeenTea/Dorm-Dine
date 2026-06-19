from db import db

class Notification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    dish_order_id = db.Column(db.Integer, db.ForeignKey("dish_order.id"), nullable=True)
    types = db.Column(db.String, nullable=False)
    message = db.Column(db.String, nullable=False)
    is_read = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=db.func.now())

    user = db.relationship("User", back_populates="notifications")
    dish_order = db.relationship("DishOrder", back_populates="notifications")
