from flask import Blueprint, jsonify, request
from service.auth_service import AuthService
from schema.user_schema import UserSchema

auth_controller = Blueprint("auth_controller", __name__)


@auth_controller.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data["email"]
    password = data["password"]
    try:
        result = AuthService.login(email=email, password=password)
        if result:
            response = jsonify(
                {
                    "access_token": result["access_token"],
                    "refresh_token": result["refresh_token"],
                }
            )
        response.set_cookie("access_token", result["access_token"], httponly=True)
        response.set_cookie("refresh_token", result["refresh_token"], httponly=True)
        return response, 200
    except:
        return jsonify({"message": "Internal server error"}), 500
