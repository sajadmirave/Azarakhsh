import os
import sys

# get current path
current_path = os.path.abspath(__file__)

# get root directory path
root = os.path.dirname(os.path.dirname(current_path))

sys.path.append(root)

from index import DB
from src.helper import Helper

class Model:
    # initilazing and helpers
    def __init__(self,connection,table,cols):
        self.db = DB(connection)
        self.helper = Helper(self.db.cursor,self.db.connection)
        self.table = table
        self.cols = cols
        self.fields = {}
        self.__create()
        self.jsonResponse = False

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

    def __get_cols_string_from_hex(self,data):
        result = [str(key) for key in data.keys()]

        return result
    
    def __get_field_title_from_string(self,data):
        field_title =[]

        for i in range(len(data)):
            field_title.append(data[i].split()[0])

        return field_title

    def __get_data_from_hex(self,data):
        return list(data.values())

    def __create_dict_data(self,keys,values):
        data = {}

        for i in range(len(keys)):
            data[keys[i]] = values[i]
        
        return data
    # ----------------------------------------------
    # querys
    def insert(self,data):
        key_list = self.__get_cols_string_from_hex(data)
        field_title = self.__get_field_title_from_string(key_list)
        value_list = self.__get_data_from_hex(data)

        data = self.__create_dict_data(field_title,value_list)
        self.db.insert(self.table,data)

    def getAll(self):
        return self.db.getAll(self.table,self.jsonResponse)
    
    def delete(self,data):
        key_list = self.__get_cols_string_from_hex(data)
        field_title = self.__get_field_title_from_string(key_list)
        value_list = self.__get_data_from_hex(data)

        data = self.__create_dict_data(field_title,value_list)
        self.db.delete(self.table,data)
        
    def delete_table(self):
        self.db.delete_table(self.table)