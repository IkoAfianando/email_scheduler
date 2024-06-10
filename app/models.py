from . import db


class Email(db.Model):
    email_id = db.Column(db.String(50), primary_key=True)
    event_id = db.Column(db.Integer, nullable=False)
    email_subject = db.Column(db.String(100), nullable=False)
    email_content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)
    sent = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f'<Email {self.email_id}>'
