from datetime import datetime
from pydantic import BaseModel
from config import db

class Note(db.Model):
    __tablename__ = "note"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    content = db.Column(db.String, nullable=False)
    created_date = db.Column(
        db.DateTime, default=datetime.utcnow
    )
    updated_date = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    lname = db.Column(db.String(32), unique=False)
    fname = db.Column(db.String(32))
    created_date = db.Column(
        db.DateTime, default=datetime.utcnow
    )
    updated_date = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    notes = db.relationship(
        Note,
        backref="user",
        cascade="all, delete, delete-orphan",
        single_parent=True,
        order_by="desc(Note.updated_date)"
    )    

class PlainUser(BaseModel):
    id: int
    fname: str
    lname: str
    created_date: datetime
    updated_date: datetime

class PlainNote(BaseModel):
    id: int
    user_id: int
    content: str
    created_date: datetime
    updated_date: datetime
    