from db import db

class DishPhoto(db.Model):
    __tablename__ = "dish_photo"
    id = db.Column(db.Integer, primary_key=True)
    dish_id = db.Column(db.Integer, db.ForeignKey("dish.id"), nullable=True)
    dish_picture = db.Column(db.LargeBinary, nullable=True)
    picture_mimetype = db.Column(db.String, nullable=True)  # z.B. "image/jpeg"
    is_primary = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=db.func.now())