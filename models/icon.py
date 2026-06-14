from db import db

class Icon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    icon_picture = db.Column(db.LargeBinary, nullable=True)
    picture_mimetype = db.Column(db.String, nullable=True)  # z.B. "image/jpeg"