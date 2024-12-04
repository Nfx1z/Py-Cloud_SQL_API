import jwt
import secrets
from .config import JWT_SECRET_KEY
from dotenv import set_key

# Generate a random secret key for JWT authentication
def generate_secret_key():
    # Generate a random secret key
    secret_key = secrets.token_hex(6)
    # Set the secret key in the '.env' file
    set_key('.env', 'JWT_SECRET_KEY', secret_key)

# Generate a JWT for authentication purposes with user information
def generate_jwt(db_name, db_user, user_password):
    payload = {
        'db_name': db_name,
        'db_user': db_user,
        'user_password': user_password
        }
    token = jwt.encode(payload, JWT_SECRET_KEY, algorithm='HS256')
    return token

# Decode and verify the JWT
def verify_jwt(token):
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=['HS256'])
        db_name = payload.get('db_name')
        db_user = payload.get('db_user')
        user_password = payload.get('user_password')
        return db_name, db_user, user_password
    except Exception as e:
        raise e