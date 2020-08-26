from models.base_model import BaseModel
from models.user import User
import peewee as pw

class Location(BaseModel):
    user = pw.ForeignKeyField(User,backref=locations ,null=False)
    name = pw.CharField(null=False)
    full_address = pw.CharField(null=False)