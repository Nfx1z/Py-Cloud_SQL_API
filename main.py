import os
from flask import Flask
from flask_cors import CORS
from src.routes import bp


app = Flask(__name__)

# Register the SQL routes blueprint
app.register_blueprint(bp)

# Enable CORS for all endpoints
CORS(
    app,
    resources={
        r"/*": {
            "origins": ["*"],
            "methods": ["GET", "POST", "DELETE", "PUT"],
        },
    },
    supports_credentials=True,
)

# Start the Flask server
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port, debug=True)
