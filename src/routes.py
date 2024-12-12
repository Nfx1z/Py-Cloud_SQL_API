from flask import Blueprint, jsonify, request
from src.controller.controller import ( 
    login_controller,    
)
from src.controller.tables import (
    get_tables_controller,
    create_table_controller,
    describe_table_controller,
    rename_table_controller,
    drop_table_controller
)
from src.controller.contents import (
    get_contents_controller,
    search_contents_controller,
    insert_contents_controller,
    update_contents_controller,
    delete_contents_controller
)

# Define a Blueprint to organize the routes
bp = Blueprint('routes', __name__)

# =============================================================================================
@bp.route('/', methods=['GET'])
def based():
    return jsonify({'message': 'Hello, World!'}), 200

@bp.route('/login', methods=['POST'])
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

@bp.route('/table/describe', methods=['GET'])
def describe_table():
    token = request.cookies.get('SQL_TOKEN')
    table = request.json.get('table')
    # Check if the token is present
    if not token:
        return jsonify({'error': 'No token provided'}), 401
    # Check if the table is present
    if not table:
        return jsonify({'error': 'No table provided'}), 401
    return describe_table_controller(token, table)

@bp.route('/table/create', methods=['POST'])
def create_table():
    token = request.cookies.get('SQL_TOKEN')
    # Check if the token is present
    if not token:
        return jsonify({'error': 'No token provided'}), 401
    return create_table_controller(token, request)

@bp.route('/table/rename', methods=['PUT'])
def rename_table():
    token = request.cookies.get('SQL_TOKEN')
    table = request.json.get('table')
    new_table = request.json.get('new_table')
    # Check if the token is present
    if not token:
        return jsonify({'error': 'No token provided'}), 401
    # Check if the table and new_table is present
    if not table or not new_table:
        return jsonify({'error': 'No table or new_table provided'}), 401
    return rename_table_controller(token, table, new_table)

@bp.route('/table/delete', methods=['DELETE'])
def drop_table():
    token = request.cookies.get('SQL_TOKEN')
    table = request.json.get('table')
    # Check if the token is present
    if not token:
        return jsonify({'error': 'No token provided'}), 401    
    # Check if the table is present
    if not table:
        return jsonify({'error': 'No table provided'}), 401
    return drop_table_controller(token, table)

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

@bp.route('/content/add', methods=['POST'])
def insert_into_table():
    token = request.cookies.get('SQL_TOKEN')
    # Check if the token is present
    if not token:
        return jsonify({'error': 'No token provided'}), 401
    return insert_contents_controller(token, request)

@bp.route('/content/update', methods=['PUT'])
def update_content_in_table():
    token = request.cookies.get('SQL_TOKEN')
    # Check if the token is present
    if not token:
        return jsonify({'error': 'No token provided'}), 401
    return update_contents_controller(token, request)

@bp.route('/content/delete', methods=['DELETE'])
def delete_content_from_table():
    token = request.cookies.get('SQL_TOKEN')
    # Check if the token is present
    if not token:
        return jsonify({'error': 'No token provided'}), 401
    return delete_contents_controller(token, request)

@bp.route('/content/specific', methods=['GET'])
def search_content_in_table():
    token = request.cookies.get('SQL_TOKEN')
    # Check if the token is present
    if not token:
        return jsonify({'error': 'No token provided'}), 401
    return search_contents_controller(token, request)