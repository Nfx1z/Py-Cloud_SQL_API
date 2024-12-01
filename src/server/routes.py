from flask import Blueprint, jsonify, request
from src.controller import home_controller, user_config_controller

# Define a Blueprint to organize the routes
bp = Blueprint('routes', __name__)

@bp.route('/', methods=['GET'])
def based():
    return jsonify({'message': 'Hello, World!'}), 200

@bp.route('/home', methods=['GET'])
def home():
    token = request.cookies.get('SQL_TOKEN')
    # Check if the token is present
    if not token:
        return jsonify({'error': 'No token provided'}), 401
    return home_controller(token)

@bp.route('/user/config', methods=['POST'])
def user_config():
    return user_config_controller(request)

