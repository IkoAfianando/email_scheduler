# Email Scheduler

Email Scheduler is a simple application that allows you to schedule email deliveries automatically based on a specific
schedule.

## Features

- Manage a list of emails to be sent.
- Schedule the time of email delivery.
- Use Celery to schedule email delivery tasks automatically.
- Configure email server settings via the `.env` file.

## Installation

1. Make sure you have Python 3 and pip installed.
2. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/IkoAfianando/email_scheduler
    ```

3. Navigate to the project directory:

    ```bash
    cd email_scheduler
    ```

4. Create a virtual environment:

    ```bash
    python3 -m venv venv
    ```

5. Activate the virtual environment:

    ```bash
    source venv/bin/activate
    ```

6. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

7. Create a `.env` file and configure the required environment variables:

    ```plaintext
    MYSQL_URL=mysql://root:root@127.0.0.1/email_scheduler
    REDIS_URL=redis://127.0.0.1:6379/0
    SMTP_PORT=587
    SMTP_SERVER=sandbox.smtp.mailtrap.io
    SMTP_LOGIN=-
    SMTP_PASSWORD=-
    ```

## Usage

1. Activate the virtual environment if not already activated:

    ```bash
    source venv/bin/activate
    ```

   2. Run the Celery worker to schedule email delivery tasks:

       ```bash
       celery -A celery_worker.celery worker --loglevel=info
       ```

       ```bash
       celery -A celery_worker.celery beat --loglevel=info
      ```

3. Run the Flask application:

    ```bash
    flask run
    ```

4. Open the application in your browser and start scheduling email delivery.


# Email Scheduler using Docker Compose

Email Scheduler is a simple application that allows you to schedule email deliveries automatically based on a specific schedule. This setup guide explains how to run the Email Scheduler application using Docker Compose.

## Prerequisites

- Docker
- Docker Compose
- `.env` file with configuration settings (see Configuration section)

## Configuration

Create a `.env` file in the project directory with the following configuration settings:

```plaintext
MYSQL_URL=-
REDIS_URL=-
SMTP_PORT=587
SMTP_SERVER=sandbox.smtp.mailtrap.io
SMTP_LOGIN=-
SMTP_PASSWORD=-
```
```bash
docker-compose up --build -d
```


