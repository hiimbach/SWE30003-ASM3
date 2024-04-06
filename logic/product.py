import pandas as pd

class Product:
    def __init__(self, 
                 name: str, 
                 price: float, 
                 amount: int, 
                 category: str, 
                 description: str) -> None:
        
        self.name = name
        self.price = price
        self.amount = amount
        self.category = category
        self.description = description
        
    
    def from_series(series: pd.Series):
        return Product(series['name'], 
                       series['price'], 
                       series['amount'], 
                       series['category'], 
                       series['description'])
        
    