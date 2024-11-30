from flask import Blueprint, jsonify, request
from src.MySQL.handler import fetch_data_from_db, add_data_to_db

# Define a Blueprint to organize the routes
sql_bp = Blueprint('routes', __name__)

@sql_bp.route('/')
def index():
    rows = fetch_data_from_db()
    return jsonify(rows)

@sql_bp.route('/add', methods=['POST'])
def add_entry():
    data = request.get_json()
    name = data.get('name')
    age = data.get('age')

    add_data_to_db(name, age)
    return jsonify({'message': 'Data added successfully!'})
