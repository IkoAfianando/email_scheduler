from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from celery import Celery
from dotenv import load_dotenv

db = SQLAlchemy()

load_dotenv()


def create_app():
    app = Flask(__name__)

    # Configuring the app
    app.config.from_object(Config)
    db.init_app(app)
    with app.app_context():
        db.create_all()

    # Registering the blueprint
    from .controller import main_controller
    app.register_blueprint(main_controller)

    return app


def make_celery(app=None):
    app = app or create_app()
    celery = Celery(
        app.import_name,
        broker=app.config['CELERY_BROKER_URL'],
        backend=app.config['CELERY_RESULT_BACKEND'],
        include=['app.tasks']  # Ensure tasks are included
    )
    celery.conf.update(app.config)
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask
    return celery


app = create_app()
celery = make_celery(app)
