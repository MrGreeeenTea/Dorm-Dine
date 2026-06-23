from db import db

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    receiver_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    dish_order_id = db.Column(db.Integer, db.ForeignKey("dish_order.id"), nullable=True)
    content = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now())

    sender = db.relationship("User", foreign_keys="Message.sender_id", back_populates="sent_messages")
    receiver = db.relationship("User", foreign_keys="Message.receiver_id", back_populates="received_messages")
    dish_order = db.relationship("DishOrder", back_populates="messages")
