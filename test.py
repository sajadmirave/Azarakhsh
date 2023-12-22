from index import DB
from src.type import Varchar, NotNull,AutoIncrement,Integer
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


# print(db.getAll('fruit',json=True))
# result = db.getOne('fruit','title','apple')
# result = db.getOne(table='fruit',field='title',value='apple')
# print(result)

print(db.exists(table='fruit',field='title',value='apple')
)

db.close_connection()