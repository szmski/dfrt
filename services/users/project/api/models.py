from project import db, bcrypt
from flask import current_app
import datetime
import jwt

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)

    def encode_auth_token(self, user_id):
        """Generate the auth token"""

        try:
            payload = {
                "exp": datetime.datetime.utcnow() + datetime.timedelta(
                    days=current_app.config.get('TOKEN_EXPIRATION_DAYS'),
                    seconds=current_app.config.get('TOKEN_EXPIRATION_SECONDS')
                ),
                "iat": datetime.datetime.utcnow(),
                "sub": user_id
            }

            return jwt.encode(
                payload,
                current_app.config.get("SECRET_KEY"),
                algorithms="HS256"
            )
        except as e:
            return e

    def decode_auth_token(auth_token):
        """
        Decodes auth token - :param auth_token: - :return: integer|string
        """

        try:
            payload = jwt.decode(
                auth_token, current_app.config.get("SECRET_KEY")
            )

            return payload["sub"]
        except jwt.ExpiredSignatureError:
            return "Signature expired - please log in again."
        
        except jwt.InvalidTokenError:
            return "Invalid token - please log in again."

    def to_json(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'active': self.active
        }

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = bcrypt.generate_password_hash(
            password, current_app.config.get('BCRYPT_LOG_ROUNDS')
        ).decode()