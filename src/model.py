import os
import sys

# get current path
current_path = os.path.abspath(__file__)

# get root directory path
root = os.path.dirname(os.path.dirname(current_path))

sys.path.append(root)

from index import DB

class Model:
    def __init__(self,connection,table,cols):
        self.db = DB(connection)
        self.table = table
        self.cols = cols
        self.fields = {}
        self.__create()

    def __create(self):
        # create property for fields
        self.__create_fields()
        self.__create_table()

    def __create_fields(self):
        for key,name in self.cols.items():
            setattr(self,key,name)
            self.fields[key] = name

    def __create_table(self):
        self.db.model(self.table,self.cols)
