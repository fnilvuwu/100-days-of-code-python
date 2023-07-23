from peewee import *

db = PostgresqlDatabase('mydatabase', host='localhost', port=5432, user='postgres', password='postgres')
class MyUser (Model):
   name=TextField()
   city=TextField(constraints=[SQL("DEFAULT 'Mumbai'")])
   age=IntegerField()
   class Meta:
      database=db
      db_table='MyUser'

db.connect()
db.create_tables([MyUser])