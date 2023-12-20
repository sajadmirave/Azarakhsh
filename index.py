import sqlite3
from src.type import Varchar, NotNull,AutoIncrement,Integer
from src.columns import Column
from src.helper import Helper
from src.response import Response
# check auth
# create token
# encryption
# Author - Mr Fucking Le


class DB:
    def __init__(self,config):
        self.connection = sqlite3.connect('app.db') # create connection
        self.cursor = self.connection.cursor() 
        self.config = config
        self.helper = Helper(self.cursor)
        self.response = Response()

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

    def getAll(self,table,json = False):
        query = f'''
            SELECT * FROM {table} 
        '''

        self.cursor.execute(query)
        data =  self.cursor.fetchall()

        # when user choose response with json then we convert simple data to json
        if json:
            headers = self.helper.getColTitleFromTable(table) # get table titles 
            return self.response.json(data,headers) # response

        return data
    
    # get one
    def getOne(self,table,field,value,json=True):
        query = '''
            SELECT * FROM {}
            WHERE {} = ?
        '''.format(table,field)

        self.cursor.execute(query,(value,))
        data = self.cursor.fetchall()

        if json and data is not None:
            headers = self.helper.getColTitleFromTable(table)
            return self.response.json(data,headers)

        return data
    
    def close_connection(self):
        return self.connection.close()

