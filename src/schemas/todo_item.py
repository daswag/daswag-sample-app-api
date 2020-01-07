from marshmallow import Schema, fields


class TodoItemSchema(Schema):
    id: fields.String(required=True)
    updatedAt: fields.String(required=True)
    title: fields.String(required=True)
    content: fields.String(required=False)
