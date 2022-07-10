from database import db


# mapping table
AuthorBook = db.Table(
    'author_book', db.Model.metadata,
    db.Column('author_id', db.Integer, db.ForeignKey('authors.author_id')),
    db.Column('book_id', db.Integer, db.ForeignKey('books.book_id'))
)
