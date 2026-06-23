from db import db
from datetime import datetime

class DishOrder(db.Model):
    __tablename__ = "dish_order"
    id = db.Column(db.Integer, primary_key=True)
    buyer_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    dish_id = db.Column(db.Integer, db.ForeignKey("dish.id"), nullable=False)
    portions = db.Column(db.Integer, nullable=False, default=1)
    message = db.Column(db.String, nullable=True)
    status = db.Column(db.Enum('pending', 'confirmed', 'ready', 'picked_up', 'cancelled', name='order_status'), nullable=False, default="pending")
    created_at = db.Column(db.DateTime, default=datetime.today)
    updated_at = db.Column(db.DateTime, default=datetime.today)

    buyer = db.relationship("User", foreign_keys="DishOrder.buyer_id", back_populates="dish_orders")
    dish = db.relationship("Dish", back_populates="dish_orders")
    messages = db.relationship("Message", back_populates="dish_order")
    notifications = db.relationship("Notification", back_populates="dish_order")
