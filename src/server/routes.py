from flask import Blueprint, jsonify, request, make_response
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

@bp.route('/delete_cookie')
def delete_cookie():
    # Create a response object
    response = make_response( jsonify("Cookie has been deleted."))
    
    # Set the cookie expiration date in the past (e.g., one day ago)
    response.set_cookie('SQL_TOKEN', '', expires=0)
    
    # Alternatively, set a max-age of 0 to delete the cookie
    # response.set_cookie('my_cookie', '', max_age=0)
    
    return response