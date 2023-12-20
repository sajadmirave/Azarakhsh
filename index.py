import sqlite3
from src.types import Varchar, NotNull,AutoIncrement,Integer
from src.columns import Column
from src.helper import Helper
# check auth
# create token
# encryption
# Author - Mr Fucking Le


class DB:
    def __init__(self):
        self.connection = sqlite3.connect('app.db') # create connection
        self.cursor = self.connection.cursor() 
        self.helper = Helper(self.cursor)

    # create table
    # @param dict col - give the columns structure for table
    def model(self,table,col):
        existing_col = self.helper.isColUpdated(table,col)
            # self.cursor.execute(query)


    # get existing column
    # def get_exists_col(self,table,col):
        

    # update table cols
    def update_table_cols(self, table_name, new_columns, existing_columns):
        pass




    def insert(self,table,col):
        col_key = ', '.join(list(col.keys())) # get all col keys
        col_values = ', '.join(['?' for _ in col.values()]) # replace data with ? to secure query  

        query = f'''
            INSERT INTO {table} ({col_key}) 
            VALUES ({col_values});
        '''

        values = tuple(col.values()) # get columns value
        self.cursor.execute(query,values)
        self.connection.commit()

    def getAll(self,table,withHeaders = False):
        query = f'''
            SELECT * FROM {table} 
        '''

        self.cursor.execute(query)
        data =  self.cursor.fetchall()

        if withHeaders:
            headers = self.helper.getColTitleFromTable(table)
            return self.helper.convertDataToJson(data,headers)

        return data

        
        
        

    def close_connection(self):
        return self.connection.close()

