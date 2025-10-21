import os
import requests
from bs4 import BeautifulSoup
from pony import orm
from datetime import datetime

# initializing the db
db = orm.Database()

db.bind(provider='sqlite', filename=os.path.abspath('products.db'), create_db= True) # if the file doesn't exit, create_db= True will create it


#class for the db model
class Product(db.Entity):
    name= orm.Required(str)
    price =orm.Required(float)
    created_date = orm.Required(datetime) #timestamp that tells when I put a specific piece of data into the db


db.generate_mapping(create_tables=True)