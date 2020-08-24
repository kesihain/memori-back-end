from models.base_model import BaseModel
import peewee as pw
from playhouse.hybrid import hybrid_property
from werkzeug.security import generate_password_hash
from flask_login import UserMixin

class User(UserMixin,BaseModel):
    username = pw.CharField(unique=True, null=False)
    email = pw.CharField(unique=True, null=False)
    password_hash = pw.TextField(null=False)
    password = None

    def validate(self):
        # Email should be unique
        existing_user_email = User.get_or_none(User.email==self.email)
        if existing_user_email and existing_user_email.id != self.id:
            self.errors.append(f"User with email {self.email} already exists!")
        # Username should be unique
        existing_user_username = User.get_or_none(User.username==self.username)
        if existing_user_username and existing_user_username.id != self.id:
            self.errors.append(f"User with username {self.username} already exists!")

        # Password should be longer than 8 characters
        if self.password:
            if len(self.password) <= 8:
                self.errors.append("Password is less than 6 characters")
            else:
                self.password_hash = generate_password_hash(self.password)