import os


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('MYSQL_URL', '-')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    CELERY_BROKER_URL = os.getenv('REDIS_URL', '-')
    CELERY_RESULT_BACKEND = os.getenv('REDIS_URL', '-')
    TIMEZONE = 'Asia/Singapore'
    CELERYBEAT_SCHEDULE = {
        'check_and_send_emails': {
            'task': 'app.tasks.check_and_send_emails',
            'schedule': 5,  # run every 5 seconds
        },
    }
    SMTP_PORT = os.getenv('SMTP_PORT', 0)
    SMTP_SERVER = os.getenv('SMTP_SERVER', "-")
    SMTP_LOGIN = os.getenv('SMTP_LOGIN', "-")
    SMTP_PASSWORD = os.getenv('SMTP_PASSWORD', "-")