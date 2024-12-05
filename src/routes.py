from flask import Blueprint, jsonify, request
from src.controller.controller import ( 
    login_controller,    
)
from src.controller.tables import (
    get_tables_controller,
    create_table_controller
)
from src.controller.contents import (
    get_contents_controller,
)

# Define a Blueprint to organize the routes
bp = Blueprint('routes', __name__)

# =============================================================================================
@bp.route('/', methods=['GET'])
def based():
    return jsonify({'message': 'Hello, World!'}), 200

@bp.route('/auth/login', methods=['POST'])
def user_config():
    return login_controller(request)

# =============================================================================================
@bp.route('/tables', methods=['GET'])
def home():
    token = request.cookies.get('SQL_TOKEN')
    # Check if the token is present
    if not token:
        return jsonify({'error': 'No token provided'}), 401
    return get_tables_controller(token)

@bp.route('/table/create', methods=['POST'])
def create_table():
    token = request.cookies.get('SQL_TOKEN')
    # Check if the token is present
    if not token:
        return jsonify({'error': 'No token provided'}), 401
    return create_table_controller(token, request)

# =============================================================================================
@bp.route('/contents', methods=['GET'])
def get_tables():
    token = request.cookies.get('SQL_TOKEN')
    table = request.json.get('table')
    # Check if the token is present
    if not token:
        return jsonify({'error': 'No token provided'}), 401
    # Check if the table is present
    if not table:
        return jsonify({'error': 'No table provided'}), 401
    return get_contents_controller(token, table)