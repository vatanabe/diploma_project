import csv
from products_db import Storage, db_session
import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Boolean

storage_list = []

with open('full_storage_on_level.csv', 'r', encoding='windows-1251') as f:
    fields = ['locker', 'locker_level', 'level_spot', 'active_spot', 'incoming', 'product_type', \
    'product_quantity', 'max_spot_quantity', 'action_id', 'product_id', 'out_of_balance', 'chip', 'vendor']
    reader = csv.DictReader(f, fields, delimiter=';')
    next(reader)
    for row in reader:
        if row['active_spot'] == 'yes':
            row['active_spot'] = bool(True)
        else:
            row['active_spot'] = bool(False)
        if row['incoming'] == 'yes':
            row['incoming'] = bool(True)
        else:
            row['incoming'] = bool(False)
        try:
            row['product_quantity'] = int(row['product_quantity'])
        except ValueError:
            row['product_quantity'] = 0
        try:
            row['max_spot_quantity'] = int(row['max_spot_quantity'])
        except ValueError:
            row['max_spot_quantity'] = 0
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
    storage = Storage(a['locker'], a['locker_level'], a['level_spot'], a['active_spot'], a['incoming'], \
    a['product_type'], a['product_quantity'],  a['max_spot_quantity'], a['action_id'], a['product_id'], \
    a['out_of_balance'], a['chip'], a['vendor'])
    db_session.add(storage)

db_session.commit()
        
print(storage_list)
