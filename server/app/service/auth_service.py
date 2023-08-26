from util.helper import Helper
from sqlalchemy import text
from database import DatabaseHelper
import os

db = DatabaseHelper(os.getenv("DB_URL"))


class AuthService:
    @staticmethod
    def login(email: str, password: str):
        query = f"""
            SELECT * FROM users
            WHERE email = {email};
            """
        row = db.execute_query(text(query))
        if row:
            return row
        else:
            False
