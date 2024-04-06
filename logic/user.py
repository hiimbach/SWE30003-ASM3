import pandas as pd
from logic import QueryDB

class User:
    def __init__(self, user_id: int,
                 name: str,
                 age: int,
                 address: str,
                 phone: str,
                 email: str,
                 password: str,
                 role: str) -> None:
        self.user_id = user_id
        self.name = name
        self.age = age
        self.address = address
        self.phone = phone
        self.email = email
        self.password = password
        assert role in ['admin', 'customer']
        self.role = role
        
    def from_series(series: pd.Series) -> None:
        return User(series['user_id'],
                    series['name'],
                    series['age'],
                    series['address'],
                    series['phone'],
                    series['email'],
                    series['password'],
                    series['role'])
        
        
class UserManagement:
    def __init__(self) -> None:
        self.__query = QueryDB("db")
        
    def get_user_from_id(self, user_id: int) -> User:
        user_data = self.__query.read("account", f"result=table[table['user_id'] == {user_id}]")
        if len(user_data) > 0:
            return User.from_series(user_data.iloc[0])
        
    def get_current_user(self):
        with open("db/current_user.txt", "r") as f:
            info = f.read()
        if info == "":
            return None
        else:
            user_id = int(info)
            return self.get_user_from_id(user_id)
        
    def write_current_user(self, user_id: int) -> None:
        with open("db/current_user.txt", "w") as f:
            f.write(str(user_id))
        