# Azarakhsh
The sqlite3 python library helps you build your application without wasting time writing queries...

# Instalation
not published yet

----
# Documentation

### create table

```py
db = DB()

# create scema
col = {
    "id":Column('id',Integer(),AutoIncrement()),
    "title":Column("title",Varchar(20),NotNull())
}

# create model
db.model("fruit",col)
```
---
### insert data
call insert function

params:

* table name
* data dict
```py
db.insert('fruit',{
    "title": "apple"
})
```

or 

```py
data = {
    'title':'apple'
}

# saving data
db.insert('fruit',data)
```
---
### get all
get all data from table

```py
db.getAll('fruit')
```

response

```bash
[(1, 'banana'), (2, 'apple')]
```

if you want to get json response

```py
db.getAll('fruit',json=True)

# set globaly for all function
db.jsonResponse = True
```

response

```bash
[
  {
    "id": 1,
    "title": "banana"
  },
  {
    "id": 2,
    "title": "apple"
  }
]
```

---
### get one
get one record from table

* in here, we want to get apple as title from fruit table
```py
result = db.getOne(
    table='fruit',
    field='title',
    value='apple'
    )

print(result)
```

response

```bash
[
  {
    "id": 2,
    "title": "apple"
  }
]
```
---
### update


we have two choise
* update with one condition
* update with multiple condition

first i tell you update with one condition

update the apple🍏 to peach🍑
```py
# updated data
updated_data = {
    "title":"peach" 
}

# selected data
selected_data = {
    'title':'apple'
}

# update
"""
@Params:
    1: table name
    2: selected query(condition)
    3: updated data(new data)
"""
db.update('fruit',selected_data,updated_data)
```
---

## These features will be added in the future
* encrypt data
* count record
* delete
* relation between two table
* config your db
* choose password for your connection
* gui data preview (open in web)