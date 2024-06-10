import unittest
import json
from app import app
from flask_testing import TestCase


class TestApp(TestCase):
    def create_app(self):
        return app

    def setUp(self):
        self.app = app.test_client()

    def test_send_emails(self):
        response = self.app.post(
            '/send_emails',
            data=json.dumps({
                'event_id': 10000,
                'email_subject': 'this is subject email',
                'email_content': 'this is email content',
                'timestamp': '2023-06-08 18:20:40.166218'
            }),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, 201)
        self.assertIn('Emails saved successfully', response.get_data(as_text=True))

    def test_get_emails(self):
        response = self.app.get('/get_emails')
        self.assertEqual(response.status_code, 200)

        # Parse and validate the JSON response
        data = json.loads(response.get_data(as_text=True))
        self.assertIn('message', data)
        self.assertEqual(data['message'], 'Emails retrieved successfully')
        self.assertIn('data', data)
        self.assertIsInstance(data['data'], list)

        # Additional Assertions (Example)
        email = data['data'][0]  # Assuming at least one email is present
        self.assertIn('email_id', email)
        self.assertIn('email_subject', email)
        self.assertIn('email_content', email)
        self.assertIn('event_id', email)
        self.assertIn('sent', email)
        self.assertIn('timestamp', email)



if __name__ == '__main__':
    unittest.main()
