from enum import unique
from marshmallow import Schema, fields
from serializers.authors import AuthorSchema


class BookSchema(Schema):
    book_id = fields.Integer(required=True, dump_only=True)
    title = fields.Str(required=True)
    publisher = fields.Str(required=True)
    description = fields.Str(required=True)
    isbn = fields.Integer(required=True, unique=True)
    author = fields.List(fields.Nested(AuthorSchema))