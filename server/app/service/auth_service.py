from sqlalchemy import text
from werkzeug.exceptions import HTTPException
from util.helper import Helper
import os
from database import connection


class AuthService:
    @staticmethod
    def login(email: str, password: str):
        hashed_password = Helper.generate_hash_password(password)
        cur = connection.cursor()
        cur.execute("SELECT * FROM users WHERE email = %s and password = %s", (email, hashed_password))
        data = cur.fetchall()
        print("-------")
        print(data)
        return data
