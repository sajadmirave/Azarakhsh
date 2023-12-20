from index import DB
from src.types import Varchar, NotNull,AutoIncrement,Integer
from src.columns import Column

db = DB()

# print(db.getAll('user'))
col = {
    "id":Column('id',Integer(),AutoIncrement()),
    "title":Column("title",Varchar(20),NotNull())
}
db.model("fruit",col)

fruits_data = ["apple","cucumber",'peach',"avacado","melon",'lemon','tomato','potato']

# for i in fruits_data:
#     db.insert('fruit',{
#         "title": i
#     })


print(db.getAll('fruit'))


db.close_connection()