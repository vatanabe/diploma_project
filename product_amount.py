from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine
from products_db import Product, Storage

engine = create_engine('sqlite:///data.sqlite', echo=True)

db_session = scoped_session(sessionmaker(bind=engine))

def amount1(code):
    for (id,) in db_session.query(Product.id).filter_by(product_code=code):#, used=0, special_design=0): 
        for product_id, in db_session.query(Storage.product_id).filter_by(product_id=id):
            print(id)

def amount2(code):
    for (id,), (prod_chip,), (prod_vendor,) in db_session.query(Product.id, Product.prod_chip, Product.prod_vendor).filter_by(special_code=code):
        for (product_quantity,) in db_session.query(Storage.product_quantity).filter_by(product_type='colored', product_id=id, chip=prod_chip, vendor=prod_vendor):
            return product_quantity
    return 0

def amount3(code):
    for product_name, in db_session.query(Product.product_name).filter_by(city_code=code)[:1]: 
        return product_name