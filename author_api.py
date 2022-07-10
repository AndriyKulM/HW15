import http

from flask import Blueprint, request, jsonify
from marshmallow import ValidationError

from database import db
from models.authors import Author
from models.books import Book
from serializers.authors import AuthorSchema


author_router = Blueprint('author', __name__, url_prefix='/author')


@author_router.route('')
def get():
    author_schema = AuthorSchema()

    authors = Author.query.order_by(Author.author_id)
    authors_json = author_schema.dump(authors, many=True)
    return jsonify(authors_json)


@author_router.route('/<int:id_>')
def retrieve(id_):
    author_schema = AuthorSchema()
    author = Author.query.filter_by(author_id=id_).first()
    author_json = author_schema.dump(author)
    return jsonify(author_json)


@author_router.route('', methods=['POST'])
def create():
    data = request.get_json(force=True)

    schema = AuthorSchema()
    try:
        author_data = schema.load(data)
        new_author = Author(
            name=author_data['name'],
            last_name=author_data['last_name']
        )
        db.session.add(new_author)
        db.session.commit()

        new_author_json = schema.dump(new_author)
    except ValidationError as e:
        return {'errors': e.messages}, http.HTTPStatus.UNPROCESSABLE_ENTITY

    return new_author_json


@author_router.route('/<int:id_>', methods=['PUT'])
def update(id_):
    data = request.get_json(force=True)

    schema = AuthorSchema()
    try:
        author_data = schema.load(data)
        author = Author.query.filter_by(author_id=id_).first()
        author.name = author_data['name']
        author.last_name = author_data['last_name']
        db.session.add(author)
        db.session.commit()

        new_author_json = schema.dump(author)
    except ValidationError as e:
        return {'errors': e.messages}, http.HTTPStatus.UNPROCESSABLE_ENTITY

    return new_author_json


@author_router.route('/<int:id_>', methods=['DELETE'])
def delete(id_):
    Author.query.filter_by(author_id=id_).delete()
    db.session.commit()
    return {}, http.HTTPStatus.NO_CONTENT


# add the author to the book; one book can have several authors
@author_router.route('/<int:id_>/add_book/<int:book_id_>', methods=['POST'])
def add_to_book(id_, book_id_):
    author = Author.query.filter_by(author_id=id_).first()
    if book := Book.query.filter_by(book_id=book_id_).first():
        author.book_id_ = book.book_id
        db.session.add(author)
        db.session.commit()
        schema = AuthorSchema()
        new_author_json = schema.dump(author)
        return new_author_json, http.HTTPStatus.OK
    else:
        return {"No book found"}, http.HTTPStatus.BAD_REQUEST
