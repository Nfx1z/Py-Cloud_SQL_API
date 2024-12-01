from flask import Blueprint, jsonify, request
from src.handler import fetch_data_from_db, add_data_to_db
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

@bp.route('/')
def index():
    # Get the token from the 'Authorization' header
    token = request.headers.get('Authorization')  
    rows = fetch_data_from_db()
    return jsonify(rows)

@bp.route('/add', methods=['POST'])
def add_entry():
    data = request.get_json()
    name = data.get('name')
    age = data.get('age')

    add_data_to_db(name, age)
    return jsonify({'message': 'Data added successfully!'})
