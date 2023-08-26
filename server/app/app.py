from flask import Flask
from flask_cors import CORS
from database import DatabaseHelper
from sqlalchemy import text
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv()

db_uri = os.getenv("DB_URL")
db_helper = DatabaseHelper(db_uri)


CORS(app, supports_credentials=True)





if __name__ == "__main__":
    app.run(port=5000)

