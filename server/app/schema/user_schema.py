from marshmallow import Schema, fields, ValidationError


class UserSchema(Schema):
    email = fields.Email()
    password = fields.Str(required=True)

    @staticmethod
    def validate_request_data(schema, data):
        try:
            result = schema.load(data)
            return (
                None,
                result,
            )  # Doğrulama başarılı, result içinde dönüştürülmüş veriler
        except ValidationError as error:
            return (
                error.messages,
                None,
            )  # Doğrulama hatası, error.messages içinde hata mesajları