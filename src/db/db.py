from peewee import SqliteDatabase, ForeignKeyField, Model, DateField, FloatField, TextField, BooleanField, UUIDField, IntegerField
import uuid

db = SqliteDatabase('database.db')
        
def create_tables():
    with db:
        db.create_tables([PlanModel, ExpenseModel])

class BaseModel(Model):
    class Meta:
        database = db

class PlanModel(BaseModel):
    id = UUIDField(primary_key=True, default=uuid.uuid4)
    name = TextField()
    budget = IntegerField()
    start_date = DateField()
    end_date = DateField()
    save_percentage = IntegerField()
    need_percentage = IntegerField()
    is_active = BooleanField()
        
class ExpenseModel(BaseModel):
    id = UUIDField(primary_key=True, default=uuid.uuid4)
    name = TextField()
    amount = IntegerField()
    category = TextField()
    date = DateField()
    category_expand = TextField(null=True)
    note = TextField(null=True)
    plan = ForeignKeyField(PlanModel, backref='expenses')
