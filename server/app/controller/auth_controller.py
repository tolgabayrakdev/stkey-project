from flask import Blueprint, jsonify, request
from service.auth_service import AuthService


auth_controller = Blueprint("auth_controller", __name__)

@auth_controller.route("/login", methods=["POST"])
def login():
    data = request.get_json()