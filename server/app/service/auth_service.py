from sqlalchemy import text
from werkzeug.exceptions import HTTPException, BadRequest
from util.helper import Helper
from database import connection
import psycopg2

cur = connection.cursor()


class AuthService:
    @staticmethod
    def login(email: str, password: str):
        hashed_password = Helper.generate_hash_password(password)
        try:
            cur.execute(
                "SELECT * FROM users WHERE email = %s and password = %s",
                (email, hashed_password),
            )
            data = cur.fetchall()
            connection.commit()
            if data:
                access_token = Helper.generate_access_token({"email": data[0][0]})
                refresh_token = Helper.generate_access_token({"email": data[0][0]})
                return {"access_token": access_token, "refresh_token": refresh_token}
            else:
                return BadRequest(description="User not found")
        except psycopg2.DatabaseError as error:
            connection.rollback()
            return error

    @staticmethod
    def register(username: str, email: str, password: str):
        try:
            hash_password = Helper.generate_hash_password(password=password)
            cur.execute(
                """
                INSERT INTO users(username, email, password, created_at, updated_at)
                VALUES(%s, %s, %s, now(), now())
                """,
                (username, email, hash_password),
            )
            connection.commit()
        except psycopg2.DatabaseError as error:
            connection.rollback()
            return error
        