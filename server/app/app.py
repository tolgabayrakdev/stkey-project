from flask import Flask, jsonify
from database import DatabaseHelper
from sqlalchemy import text

app = Flask(__name__)

db_uri = "postgresql://root:root@localhost/postgres"
db_helper = DatabaseHelper(db_uri)


@app.route("/deneme", methods=["GET"])
def deneme_query():
    sql_query = "SELECT * FROM users"
    rows = db_helper.execute_query(text(sql_query))
    user_list = [{"username": row.username} for row in rows]
    return jsonify({"users": user_list})


if __name__ == "__main__":
    app.run(port=5000)
