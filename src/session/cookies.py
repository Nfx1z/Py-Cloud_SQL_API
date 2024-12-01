import jwt
import secrets
from session.config import Config
from dotenv import set_key

# Generate a random secret key for JWT authentication
def generate_secret_key():
    # Generate a random secret key
    secret_key = secrets.token_hex(16)
    # Set the secret key in the '.env' file
    set_key('.env', 'JWT_SECRET_KEY', secret_key)

# Generate a JWT for authentication purposes with user information
def generate_jwt(db_name, db_user, db_password):
    payload = {'db_name' : db_name, 'db_user' : db_user, 'db_password' : db_password }
    token = jwt.encode(payload, Config.JWT_SECRET_KEY, algorithm='HS256')
    return token

# Decode and verify the JWT
def verify_jwt(token):
    try:
        payload = jwt.decode(token, Config.JWT_SECRET_KEY, algorithms=['HS256'])
        db_name = payload['db_name']
        db_user = payload['db_user']
        db_password = payload['db_password']
        return db_name, db_user, db_password
    except jwt.ExpiredSignatureError:
        raise Exception('Token has expired')
    except jwt.InvalidTokenError:
        raise Exception('Invalid token')