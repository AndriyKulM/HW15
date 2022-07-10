from marshmallow import Schema, fields


class AuthorSchema(Schema):
    author_id = fields.Integer(required=True, dump_only=True)
    name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    book_id_ = fields.Integer(required=False)