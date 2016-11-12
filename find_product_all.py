from sqlalchemy.orm import scoped_session, sessionmaker, load_only
from sqlalchemy import create_engine
from products_db import Product, Storage

engine = create_engine('sqlite:///blog.sqlite', echo=True)

db_session = scoped_session(sessionmaker(bind=engine))

def find_in_db(what_to_fitd, code):

    product = db_session.query(Product).options(load_only(what_to_fitd))\
    .filter_by(product_code=code, special_design=0).first()
    return product

if __name__ == "__main__":
    prod_vendor = find_in_db("prod_vendor", "I5")
    print(prod_vendor.prod_vendor)
