from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine
from products_db import Product

engine = create_engine('sqlite:///data.sqlite', echo=True)

db_session = scoped_session(sessionmaker(bind=engine))

def search1(code):
    for product_name, in db_session.query(Product.product_name).filter_by(product_code=code):#, used=0, special_design=0): 
        return product_name

def search2(code):
    for special_code, in db_session.query(Product.special_code).filter_by(special_code=code)[:1]: 
        return special_code

def search3(code):
    for product_name, in db_session.query(Product.product_name).filter_by(city_code=code)[:1]: 
        return product_name