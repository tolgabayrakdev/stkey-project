from flask import Flask
from database import db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://root:root@localhost/postgres"

db.init_app(app)


if __name__ == "__main__":
    app.run(port=5000)