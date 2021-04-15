from datetime import datetime
from app import db


class MascleData(db.Model):
    __tablename__ = 'mascle_data'
    id = db.Column(db.Integer, primary_key=True)
    kind_of_mascle = db.Column(db.String(255), nullable=False)
    reps = db.Column(db.Float, nullable=False)
    weight = db.Column(db.Float, nullable=False)
    done_at = db.Column(db.DateTime, nullable=False, default=datetime.now)

def init():
    db.create_all()
