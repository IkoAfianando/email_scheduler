from app import celery, db, create_app
from app.models import Email
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import Config


def send_email(email_subject, email_content):
    # Configuration
    port = Config.SMTP_PORT
    smtp_server = Config.SMTP_SERVER
    login = Config.SMTP_LOGIN
    password = Config.SMTP_PASSWORD

    sender_email = "Private Person <from@example.com>"
    receiver_email = "A Test User <to@example.com>"

    # Email content
    subject = f"{email_subject}"
    html = f"""\
    <html>
      <body>
        <p>Hi, This is email server<br>
        <p>{email_content}</p>
      </body>
    </html>
    """

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # Attach the HTML part
    message.attach(MIMEText(html, "html"))

    # Send the email
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls()
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, message.as_string())


@celery.task
def send_email_task(email_id):
    app = create_app()
    with app.app_context():
        email = Email.query.get(email_id)
        if email and not email.sent:
            email.sent = True
            db.session.commit()
            send_email(email.email_subject, email.email_content)


@celery.task
def check_and_send_emails():
    app = create_app()
    with app.app_context():
        now = datetime.now()
        unsent_emails = Email.query.filter(Email.sent == False, Email.timestamp <= now).all()
        for email in unsent_emails:
            send_email_task.delay(email.email_id)
