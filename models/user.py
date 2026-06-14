from db import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    password_hash = db.Column(db.String, nullable=False)
    username = db.Column(db.String, unique=True, nullable=False)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    profile_picture = db.Column(db.LargeBinary, nullable=True)
    picture_mimetype = db.Column(db.String, nullable=True)  # z.B. "image/jpeg"
    bio = db.Column(db.String, nullable=True)
    is_cook = db.Column(db.Boolean, default=False)
    dorm_id = db.Column(db.Integer, db.ForeignKey("dorm.id"), nullable=True) #db.Integer vllt redundant? 
    phone_number = db.Column(db.String, nullable=True)
    created_at = db.Column(db.DateTime, default=db.func.now())
    
    dorm = db.relationship("Dorm", back_populates="users")
    dish_orders = db.relationship("DishOrder", back_populates="buyer")
    sent_messages = db.relationship("Message", foreign_keys="Message.sender_id", back_populates="sender")
    received_messages = db.relationship("Message", foreign_keys="Message.receiver_id", back_populates="receiver")
    notifications = db.relationship("Notification", back_populates="user")