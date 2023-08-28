from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from controller.auth_controller import auth_controller

app = Flask(__name__)
load_dotenv()

CORS(app, supports_credentials=True)

app.register_blueprint(auth_controller, url_prefix="/api/v1/auth")

if __name__ == "__main__":
    app.run(port=5000)
