from marshmallow import Schema, fields


class EmailSchema(Schema):
    email_id = fields.String()
    event_id = fields.Integer()
    email_subject = fields.String()
    email_content = fields.String()
    timestamp = fields.DateTime()
    sent = fields.Boolean()
