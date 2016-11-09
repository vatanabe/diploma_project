from products_db import Action
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker
from datetime import datetime

engine = create_engine('sqlite:///data.sqlite', echo=True)

db_session = scoped_session(sessionmaker(bind=engine))

action = Action(datetime.now(), 0, 'input_file_name',
    0, 'product_id', 'reason', 'bot')

def add_action():   
    db_session.add(action)
    db_session.commit()
    
add_action()