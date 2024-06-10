from .models import Email
from . import db
import uuid


def add_data_email(new_data):
    email_id = str(uuid.uuid4())
    email = Email(
        email_id=email_id,
        event_id=new_data['event_id'],
        email_subject=new_data['email_subject'],
        email_content=new_data['email_content'],
        timestamp=new_data['timestamp'],
        sent=False
    )
    db.session.add(email)
    db.session.commit()
    return email


def get_email():
    return Email.query.all()
