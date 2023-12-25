from index import DB
from src.type import Varchar, NotNull,AutoIncrement,Integer
from src.columns import Column


db = DB()

# print(db.getAll('user'))
# col = {
#     "id":Column('id',Integer(),AutoIncrement()),
#     "title":Column("title",Varchar(20),NotNull())
# }
# db.model("fruit",col)

# fruits_data = ["apple","cucumber",'peach',"avacado","melon",'lemon','tomato','potato']

# for i in fruits_data:
#     db.insert('fruit',{
#         "title": i
#     })


print(db.getAll('fruit',json=True))
# result = db.getOne('fruit','title','apple')
# result = db.getOne(table='fruit',field='title',value='apple')
# print(result)

# print(db.exists(table='fruit',field='title',value='apple')
# )

# print(db.count(table='fruit'))

# updated_data = {
#     "title":"new_banana"
# }

# condition = {
#     "title":"banana",
#     # "title1":"banana",
# }
# db.update('fruit',condition,updated_data)
# db.update(table='fruit',data=updated_data,condition_field='title',condition_value='apple')

# db.delete('fruit',{
#     'title':"tomato"
# })

db.close_connection()