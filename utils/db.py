from typing import List
import os 

import pandas as pd 


class DBConnection():
    def __init__(self, db_path) -> None:
        self.__path = db_path
        self.__table_names = self.__tables()
        self.__table_dict = self.__create_table_dict()
        
    def __tables(self):
        files = os.listdir(self.__path)
        return list(map(lambda x: x[:-4], files))
        
    def __create_table_dict(self):
        tables = {}
        for table in self.__table_names:
            path = os.path.join(self.__path, table+".csv")
            if os.path.isfile(path):
                tables[table] = Table(path)        
                    
        return tables
    
    def table_dict(self):
        return self.__table_dict
    
    def table_names(self):
        return self.__table_names
    
    
class Table():
    def __init__(self, db_path: str) -> None:
        self.__db_path = db_path
        self.__db = pd.read_csv(db_path)
        
    def length(self):
        return len(self.__db)
    
    def update_table(self):
        self.__db.to_csv(self.__db_path, index=False)
    
    def add_row(self, row: List):
        self.__db.loc[self.length()] = row
        self.update_table()
        
    def delete_row(self, idx: int):
        self.__db.drop(idx, inplace=True)
        self.__db.reset_index(drop=True, inplace=True)
        self.update_table()
        
    def modify_row(self, idx: int, row: List):
        self.__db.loc[idx] = row
        self.update_table()
        
    def get_row(self, idx: int):
        return self.__db.loc[idx].tolist()
        

class QueryDB():
    def __init__(self, db_path: str) -> None: 
        db_connection = DBConnection(db_path)
        self.table = db_connection.table_dict()
        self.table_names = db_connection.table_names()
        
    def query(self, op_type: str, table_name: str, *kwargs):
        if op_type == 'add':
            self.table_dict[table_name].add_row(*kwargs)
        elif op_type == 'delete':
            self.table_dict[table_name].delete_row(*kwargs)
        elif op_type == 'modify':
            self.table_dict[table_name].modify_row(*kwargs)
        else:
            raise ValueError("Invalid operation type.")
        
        