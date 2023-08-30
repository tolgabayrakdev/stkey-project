from app.service.auth_service import AuthService
from app.database import connection


def test_change_password():
    change_func = AuthService.change_password(
        email="tolga123@gmail.com",
        current_password="123456",
        new_password="deneme123"
    )
    