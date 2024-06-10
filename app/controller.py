from flask import request, jsonify, Blueprint
from .services import add_data_email, get_email
from .validation import EmailEventSchema
from marshmallow import ValidationError
from .serializers import EmailSchema

main_controller = Blueprint('main', __name__)


@main_controller.route('/send_emails', methods=['POST'])
def save_emails():
    data = request.get_json()
    schema = EmailEventSchema()
    try:
        try:
            schema.load(data)
            add_data_email(data)
            return jsonify({'message': 'Emails saved successfully'}), 201
        except ValidationError as e:
            return jsonify({"error": "Invalid data", "details": e.messages}), 400
    except Exception as e:
        return jsonify({'message': str(e)}), 500



@main_controller.route('/get_emails', methods=['GET'])
def get_emails():
    try:
        data = get_email()
        schema = EmailSchema(many=True)
        data = schema.dump(data)
        return jsonify({'message': 'Emails retrieved successfully', 'data': data}), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500

