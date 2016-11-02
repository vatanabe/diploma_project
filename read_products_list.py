import csv
from products_db import Product, db_session
import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Boolean

prod_list = []

with open('products_list.csv', 'r', encoding='windows-1251') as f:
    fields = ['product_bin', 'product_name', 'product_code', 'special_code', \
    'city_code', 'parent_id', 'used', 'special_design', 'contactless_interface', \
    'link_contactless', 'add_date', 'prod_chip', 'prod_vendor', 'front_side_image', \
    'front_side_print', 'back_side_image', 'back_side_print', 'city', 'images_pixels']
    reader = csv.DictReader(f, fields, delimiter=';')
    next(reader)
    for row in reader:
        try:
            row['parent_id'] = int(row['parent_id'])
        except ValueError:
            row['parent_id'] = 0
        if row['used'] == 'used':
            row['used'] = bool(True)
        else:
            row['used'] = bool(False)
        if row['special_design'] == 'yes':
            row['special_design'] = bool(True)
        else:
            row['special_design'] = bool(False)
        if row['contactless_interface'] == 'yes':
            row['contactless_interface'] = bool(True)
        else:
            row['contactless_interface'] = bool(False)
        if row['link_contactless'] == 'yes':
            row['link_contactless'] = bool(True)
        else:
            row['link_contactless'] = bool(False)
        if  row['add_date'] != '':
            row['add_date'] = datetime.datetime.strptime(row['add_date'], '%d.%m.%Y')
        else:
            row['add_date'] = None
        prod_list.append(row)


for a in prod_list:
    products = Product(a['product_bin'], a['product_name'], a['product_code'], \
    a['special_code'], a['city_code'], a['parent_id'], a['used'], a['special_design'], \
    a['contactless_interface'], a['link_contactless'], a['add_date'], a['prod_chip'], \
    a['prod_vendor'], a['front_side_image'], a['front_side_print'], a['back_side_image'], \
    a['back_side_print'], a['city'], a['images_pixels'])
    db_session.add(products)

db_session.commit()
        
print(prod_list)
