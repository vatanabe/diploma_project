from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine
from products_db import Product, Storage

engine = create_engine('sqlite:///blog.sqlite', echo=True)

db_session = scoped_session(sessionmaker(bind=engine))

def amount1(code):

    (prod_vendor,) = db_session.query(Product.prod_vendor)\
    .filter_by(product_code=code, special_design=0).first()
    return prod_vendor

if __name__ == "__main__":
    prod_vendor = amount1("I5")
    print(prod_vendor)
