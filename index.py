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
    def __init__(self,connection):
        self.connection = sqlite3.connect(connection) # create connection
        self.cursor = self.connection.cursor() 
        self.helper = Helper(self.cursor,self.connection)
        self.response = Response()

        # set config
        self.jsonResponse = False
        self.encryptData = False

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
        if json or self.jsonResponse:
            headers = self.helper.getColTitleFromTable(table) # get table titles 
            return self.response.json(data,headers) # response

        return data
    
    # get one
    def getOne(self,table,field,value,json=False):
        query = '''
            SELECT * FROM {}
            WHERE {} = ?
        '''.format(table,field)

        self.cursor.execute(query,(value,))
        data = self.cursor.fetchall()

        if json or self.jsonResponse:
            headers = self.helper.getColTitleFromTable(table)
            return self.response.json(data,headers)

        return data
    
    def exists(self,table,field,value):
        query = '''
            SELECT EXISTS(
             SELECT 1
             FROM {}
             WHERE {} = ?
            ) AS is_exists
        '''.format(table,field)

        # this return (0 or 1 ,) and in here we get first index 
        self.cursor.execute(query,(value,))
        result = self.cursor.fetchone()[0]

        # convert 0,1 to bool
        return bool(result) 

    def count(self,table):
        query = '''
            SELECT COUNT(*) FROM {}
        '''.format(table)

        self.cursor.execute(query)
        return self.cursor.fetchone()[0] # get first index and returned 
    
    def update(self, table, condition_data,updated_data):
        """
        Convert object to this
        title=new_value, title1=new_value0
        for query
        """
        set_clause = ", ".join(f"{key} = ?" for key in updated_data)
        values = list(updated_data.values()) # updated value
        condition_field = ', '.join(str(key) for key in condition_data)
        condition_value = list(condition_data.values())

        # condition
        # first of all check its multiple condition or not
        # @reutrn false when it has one condition
        # @reutrn true when it has multiple condition
        is_multiple = len(condition_data) != 1 

        match is_multiple:
            case True:
                return self.helper.updateWithMultipleCondition(table,set_clause,values,condition_data,condition_value)
            case False:
                return self.helper.updateWithOneCondition(table,set_clause,values,condition_field,condition_value)

    # delete record
    def delete(self,table,condition):
        key,value =  next(iter(condition.items()))

        query = f'''
            DELETE FROM {table} WHERE {key}= ?
        '''
        print(query)
        self.cursor.execute(query,(value,))
        self.connection.commit()

    def delete_table(self,table):
        query = f'''
            DROP TABLE {table}
        '''

        self.cursor.execute(query)
        self.connection.commit()

    def close_connection(self):
        return self.connection.close()

