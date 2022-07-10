from enum import unique
from database import db


class Book(db.Model):
    __tablename__ = "books"

    book_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(300), nullable=False)
    publisher = db.Column(db.String(300), nullable=False)
    description = db.Column(db.String(900), nullable=False)
    isbn = db.Column(db.Integer, unique=True)
    author = db.relationship("Author")