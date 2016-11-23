from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine
from products_db import Product, Storage

engine = create_engine('sqlite:///data.sqlite')

db_session = scoped_session(sessionmaker(bind=engine))

def amount1(code):
    total_product_quantity = 0
    for (id, prod_chip, prod_vendor) in db_session.query(Product.id, Product.prod_chip, Product.prod_vendor).filter_by(product_code=code):
        for (product_quantity,) in db_session.query(Storage.product_quantity).filter_by(product_type='new', product_id=id, 
            chip=prod_chip, vendor=prod_vendor):
            total_product_quantity += product_quantity
    return total_product_quantity

def amount2(code):
    for (id, prod_chip, prod_vendor) in db_session.query(Product.id, Product.prod_chip, Product.prod_vendor).filter_by(special_code=code):
        for (product_quantity,) in db_session.query(Storage.product_quantity).filter_by(product_type='colored', product_id=id,
            chip=prod_chip, vendor=prod_vendor):
                return product_quantity
    return 0

def amount3(code):
    for (id,) in db_session.query(Product.id).filter_by(city_code=code):
        for (product_quantity,) in db_session.query(Storage.product_quantity).filter_by(product_type='colored', product_id=id):
            return product_quantity
    return 0