from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine
from products_db import Product, ProductInFile

engine = create_engine('sqlite:///data.sqlite')

db_session = scoped_session(sessionmaker(bind=engine))

def search1(code):
    for (product_name,) in db_session.query(Product.product_name).filter_by(product_code=code, used=1):#, special_design=0): 
        return product_name

def search2(code):
    for (product_name,) in db_session.query(Product.product_name).filter_by(special_code=code): 
        return product_name

def search3(code):
    for (product_name,) in db_session.query(Product.product_name).filter_by(city_code=code): 
        return product_name

def search4(code):
    for (id,) in db_session.query(Product.id).filter_by(product_code=code):
        for (id,) in db_session.query(ProductInFile.id).filter_by(product_id=id):
            return id

def change_color(code):
    for (id,) in db_session.query(Product.id).filter_by(product_code=code):
        for (product_in_file_status,) in db_session.query(ProductInFile.product_in_file_status).filter_by(product_id=id):
            return product_in_file_status
