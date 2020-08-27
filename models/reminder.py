from models.base_model import BaseModel
from models.location import Location
import peewee as pw

class Reminder(BaseModel):
    location = pw.ForeignKeyField(Location,backref='reminders' ,null=False)
    item_name = pw.CharField(null=False)