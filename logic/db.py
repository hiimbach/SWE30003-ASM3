from typing import List
from time import sleep
import os 

import pandas as pd 


class DBConnection():
    def __init__(self, db_path) -> None:
        self.__path = db_path
        
    def table(self, table_name: str):
        return pd.read_csv(os.path.join(self.__path, table_name + '.csv'))
    
    def update(self, table_name: str, data: pd.DataFrame):
        data.to_csv(os.path.join(self.__path, table_name + '.csv'), index=False)
    
    
class QueryDB():
    def __init__(self, db_path: str) -> None: 
        self.db_conn = DBConnection(db_path)
        
    def modify(self, table_name: str, query: str):
        print(query)
        
        table = self.db_conn.table(table_name)
        
        lcls = locals()
        exec(query, globals(), lcls)
        table = lcls['table']
        
        print(table)
        self.db_conn.update(table_name, table)

        
    def read(self, table_name: str, query: str):
        table = self.db_conn.table(table_name)
        result = None
        lcls = locals()
        exec(query, globals(), lcls)
        result = lcls['result']
        return result