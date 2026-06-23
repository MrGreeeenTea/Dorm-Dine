from db import db

class KitchenProof(db.Model):
    __tablename__ = "kitchen_proof"
    id = db.Column(db.Integer, primary_key=True)
    dish_order_id = db.Column(db.Integer, db.ForeignKey("dish_order.id"), nullable=False)
    cook_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    photo_url = db.Column(db.String, nullable=False)
    proof_type = db.Column(db.Enum('before', 'after', name="proof_type"), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now())

    dish_order = db.relationship("DishOrder", backref="kitchen_proofs")
    cook = db.relationship("User", backref="kitchen_proofs")