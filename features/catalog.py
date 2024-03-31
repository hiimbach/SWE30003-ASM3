from features.product import Product
from utils.db import Table

class Catalog:
    def __init__(self) -> None:
        self.products = []
        
    def add_product(self, product: Product):
        self.products.append(product)
        
    def construct_from_table(self, table: Table):
        for i in range(table.length()):
            row = table.get_row(i)
            self.add_product(Product(row[0], row[1], row[2], row[3], row[4]))    