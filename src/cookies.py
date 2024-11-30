import os
import jwt
import datetime
import secrets
from src.config import Config
from dotenv import load_dotenv, set_key

# Load environment variables from.env file (if it exists)
load_dotenv()

secret_key = os.getenv('JWT_SECRET_KEY')
# Generate a random 32-byte key and encode it in hexadecimal (64 characters)
if secret_key is None:
    set_key(".env", "JWT_SECRET_KEY", secrets.token_hex(32))
    

def generate_jwt(user_data):
    """
    Generate a JWT token for the authenticated user.
    """
    expiration_time = datetime.timedelta(hours=1)  # Token expires in 1 hour
    payload = {
        'user': user_data,
        'exp': datetime.datetime.utcnow() + expiration_time
    }
    token = jwt.encode(payload, Config.JWT_SECRET_KEY, algorithm='HS256')
    return token

def verify_jwt(token):
    """
    Verify the JWT token. Returns the payload if the token is valid, else raises an exception.
    """
    try:
        payload = jwt.decode(token, Config.JWT_SECRET_KEY, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        raise Exception('Token has expired')
    except jwt.InvalidTokenError:
        raise Exception('Invalid token')