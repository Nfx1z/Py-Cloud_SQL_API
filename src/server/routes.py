from flask import Blueprint, jsonify, request
from src.handler import fetch_data_from_db, add_data_to_db
from src.controller import home_controller

# Define a Blueprint to organize the routes
bp = Blueprint('routes', __name__)

@bp.route('/', methods=['GET'])
def home():
    token = request.cookies.get('SQL_TOKEN')
    if not token:
        return jsonify({'error': 'No token provided'}), 401
    
    return home_controller(token)

@bp.route('/user/config', methods=['POST'])
def user_config():

    data = request.get_json()
    
    password = data.get('password')
    dbname = data.get('dbname')

    if not password or not dbname:
        return jsonify({'error': 'Both "password" and "dbname" are required'}), 400
    
    # Example: you could validate, store, or use this data to set up a connection
    # For now, we'll just return it as confirmation
    response = {
        'message': 'User configuration received successfully!',
        'password': password,
        'dbname': dbname
    }
    return jsonify(response)

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
