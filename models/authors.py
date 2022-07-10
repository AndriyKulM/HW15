from database import db
from models.author_book import AuthorBook


class Author(db.Model):
    __tablename__ = 'authors'

    author_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(300), nullable=False)
    last_name = db.Column(db.String(300), nullable=False)
    book_id_ = db.Column(db.Integer, db.ForeignKey("books.book_id"))
    books = db.relationship("Book",  secondary=AuthorBook)