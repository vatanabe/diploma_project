import csv
from products_db import Storage, db_session
import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Boolean

storage_list = []

with open('full_storage.csv', 'r', encoding='windows-1251') as f:
    fields = ['locker', 'locker_level', 'level_spot', 'product_type', \
    'product_quantity', 'action_id', 'product_id', 'out_of_balance']
    reader = csv.DictReader(f, fields, delimiter=';')
    next(reader)
    for row in reader:
        try:
            row['product_quantity'] = int(row['product_quantity'])
        except ValueError:
            row['product_quantity'] = 0
        try:
            row['action_id'] = int(row['action_id'])
        except ValueError:
            row['action_id'] = 0 
        try:
            row['product_id'] = int(row['product_id'])
        except ValueError:
            row['product_id'] = 0    
        if row['out_of_balance'] == 'yes':
            row['out_of_balance'] = bool(True)
        else:
            row['out_of_balance'] = bool(False)
        storage_list.append(row)


for a in storage_list:
    storage = Storage(a['locker'], a['locker_level'], a['level_spot'], \
    a['product_type'], a['product_quantity'], a['action_id'], a['product_id'], a['out_of_balance'])
    db_session.add(storage)

db_session.commit()
        
print(storage_list)
