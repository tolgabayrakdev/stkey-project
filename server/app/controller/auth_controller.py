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
        print(result)
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
        raise result


@auth_controller.route("/register")
def register():
    data = request.get_json()
    username = data["username"]
    email = data["email"]
    password = data["password"]
    try:
        if not all([username, email, password]):
            return jsonify({"message": "Parameters is not correct"}), 400
        AuthService.register(username=username, email=email, password=password)
        return jsonify({"message": "Account created successfull"}), 201
    except:
        return jsonify({"message": "Internal Server Error"}), 500


@auth_controller.route("/logout", methods=["POST"])
def logout():
    response = jsonify({"message": "You are logout successful"})
    response.delete_cookie("access_token")
    response.delete_cookie("refresh_token")
    return response, 200
