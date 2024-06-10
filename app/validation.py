from marshmallow import Schema, fields


class EmailEventSchema(Schema):
    event_id = fields.Integer(required=True, strict=True)
    email_subject = fields.String(required=True)
    email_content = fields.String(required=True)
    timestamp = fields.DateTime(required=True)
