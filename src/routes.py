from flask import Blueprint, jsonify, request, make_response
from src.service.controller import ( 
    user_controller,
    get_tables_controller,
    get_contents_controller,
)

# Define a Blueprint to organize the routes
bp = Blueprint('routes', __name__)

@bp.route('/', methods=['GET'])
def based():
    return jsonify({'message': 'Hello, World!'}), 200


@bp.route('/user', methods=['POST'])
def user_config():
    return user_controller(request)


@bp.route('/tables', methods=['GET'])
def home():
    token = request.cookies.get('SQL_TOKEN')
    # Check if the token is present
    if not token:
        return jsonify({'error': 'No token provided'}), 401
    return get_tables_controller(token)


@bp.route('/table/contents', methods=['GET'])
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