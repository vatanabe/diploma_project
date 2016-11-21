from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Boolean, Date
from sqlalchemy.orm import scoped_session, sessionmaker
from parsing1 import values_count1

engine = create_engine('sqlite:///data.sqlite')

db_session = scoped_session(sessionmaker(bind=engine))

for code in values_count1:
    product = Product
    product = product.query.filter_by(product_code=code, used=1).first()
    print(product)
    product_in_file = ProductInFile(product_id = product.id, reject_quantity = 0, produced_quantity = 0, 
    product_in_file_status = "processed")
    db_session.add(product_in_file)
    db_session.commit()