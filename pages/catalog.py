import os 
import sys 
if os.path.abspath(os.getcwd()) not in sys.path:
    sys.path.append(os.path.abspath(os.getcwd()))

from utils.ui.catalog import CatalogUI
from features.catalog import Catalog
from utils.db import QueryDB


db = QueryDB("db")
product_table = db.table['product']
catalog = Catalog()
catalog.construct_from_table(product_table)

keep_catalog = True
while keep_catalog:
    os.system('clear')
    keep_catalog = CatalogUI(catalog).display()