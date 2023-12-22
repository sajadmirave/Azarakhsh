import json

class Helper:
    def __init__(self,cursor,connection):
        self.cursor = cursor
        self.connection = connection

    """
    Get col title and type from dict

    Args:
        col title and type (dict) : The col defination for table
        user given the data like this:
            col_data = {
            "id":Column('id',Integer(),AutoIncrement()),
            "title":Column("title",Varchar(20),NotNull())
            }

    Returns:
        string: convert this to sql query like this
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title VARCHAR(20) NOT NULL
    """
    # get col title and type from dict
    def getColAsString(self, col):
        col = ', '.join(str(col) for col in col.values())
        return col

    # --------------------------------------------------------
    # --------------------------------------------------------
    # --------------------------------------------------------

    """
    Get column titles from a table definition string.

    Args:
        table_definition (str): The table definition string.

    Returns:
        list: A list of column titles.
    """ 
    def getColTitleFromTable(self,table):
        query = f"PRAGMA table_info({table})"
        self.cursor.execute(query)
        # column[1] = title of the col
        return [column[1] for column in self.cursor.fetchall()]

    # --------------------------------------------------------
    # --------------------------------------------------------
    # --------------------------------------------------------

    """
    Get col title from string

    Args:
        col defination (str) - The col defination string
        like this:
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title VARCHAR(20) NOT NULL
    
    Returns:
        list: A list of title
    """
    def getColTitleFromString(self,col):
        split_col = col.split(', ') # split long string
        col_title = [] # create empty array to put col title in here

        # get col title
        for i in split_col:
            # index[0] is title for example
            # title varchar 20 - the title is index[0]
            col_title.append(i.split()[0])

        return col_title



    # --------------------------------------------------------
    # --------------------------------------------------------
    # --------------------------------------------------------

    """
    when user create a table given the data like this:
    col_data = {
        "id":Column('id',Integer(),AutoIncrement()),
        "title":Column("title",Varchar(20),NotNull())
    }

    in here we check is table cols, going to update or not
    when its ready to update then update the col. 
    it means whne the col_data updated, the table cols will be update  

    in the end, when col_data is still the same as the previous col, nothing changes
    """
    def isColUpdated(self,table,col):
        # get col title from table
        existing_col = self.getColTitleFromTable(table)
        # first get col from string (dict) and then get title of each col
        new_col = self.getColTitleFromString(self.getColAsString(col))
        # check its new col or not and check this table exists or not
        """
        in this case True its old cols so nothing to change
        and whne its false its means cols going to update
        """
        is_match = new_col == existing_col
        print(f"is match = {is_match}")
        if is_match or not existing_col:
            return self.create_table(table,col)
        
        # check wich cols updated
        # Find items that are in list2 but not in list1
        last_item = list(set(existing_col) - set(new_col))[0] # last item - convert {'title'} to 'title'
        updated_item = list(set(new_col) - set(existing_col))[0] # updated item - convert {'title'} to 'title'

        col_query_details = self.getColAsString(col).split() # split query to an array : title varchar(20)
        updated_col_index = col_query_details.index(updated_item) # find where its new query
        updated_col_array = col_query_details[updated_col_index:] # find updated query in here and converted to array

        #extract updated column query from array
        updated_col_query = ' '.join(str(i) for i in updated_col_array) 

        print(f"change col 1: {last_item}")
        print(f"change col 2: {updated_item}")
        print("its time to update")

        # testing
        # drop last col
        query = '''
            ALTER TABLE {}
            DROP COLUMN {}
        '''.format(table,last_item)
        self.cursor.execute(query)


        query = '''
            ALTER TABLE {}
            ADD {}
        '''.format(table,updated_col_query)
        self.cursor.execute(query)

        # return self.update_table_cols(table,existing_col,new_col)

    # create table
    def create_table(self,table,col):
        columns = self.getColAsString(col) 
        query = '''
            CREATE TABLE IF NOT EXISTS {} (
                {}
            )
        '''.format(table,columns)
        print(query)
        self.cursor.execute(query)

    def update_table_cols(self,table,existing_col,new_cols):
        pass


    # update
    def updateWithMultipleCondition(self,table,set_clause,values,condition_data,condition_value):

        condition_field = [f'{key} = ?' for key in condition_data]
        condition_field_string = ', AND '.join(condition_field)

        query = f'''
            UPDATE {table}
            SET {set_clause}
            WHERE {condition_field_string}
        '''

        self.cursor.execute(query, values + condition_value)
        # Assuming you want to commit the changes to the database
        self.connection.commit()


    def updateWithOneCondition(self,table,set_clause,values,condition_field,condition_value):
        query = f'''
            UPDATE {table}
            SET {set_clause}
            WHERE {condition_field} = ?
        '''

        self.cursor.execute(query, values + condition_value)
        # Assuming you want to commit the changes to the database
        self.connection.commit()
