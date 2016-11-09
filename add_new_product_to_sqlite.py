import csv
from products_db import Product, Storage, Action, db_session
import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Boolean


def add_new_product_to_sqlite(product_bin, product_name, product_code, special_code, \
    city_code, parent_id, used, special_design, contactless_interface, link_contactless, \
    add_date, prod_chip, prod_vendor, front_side_image, front_side_print, back_side_image, \
    back_side_print, city, images_pixels):
    try:
        parent_id = int(parent_id)
    except ValueError:
        parent_id = 0
    if used == 'used':
        used = True
    else:
        used = False
    if special_design == 'yes':
        special_design = True
    else:
        special_design = False
    if contactless_interface == 'yes':
        contactless_interface = True
    else:
        contactless_interface = False
    if link_contactless == 'yes':
        link_contactless = True
    else:
        link_contactless = False
    if  add_date != '':
        add_date = datetime.datetime.strptime(add_date, '%d.%m.%Y')
    else:
        add_date = None

    product = Product(product_bin, product_name, product_code, \
    special_code, city_code, parent_id, used, special_design, \
    contactless_interface, link_contactless, add_date, prod_chip, \
    prod_vendor, front_side_image, front_side_print, back_side_image, \
    back_side_print, city, images_pixels)
    db_session.add(product)


   
    action_datetime = datetime.datetime.now()
    action_type = 1
    produced_by = 'Волков'

    action = Action(action_datetime=action_datetime, action_type=action_type, 
          produced_by=produced_by, product=product)
    db_session.add(action)

    db_session.commit()


def add_quantity_to_storage(locker, locker_level, level_spot, active_spot, incoming, product_type, \
    product_quantity, max_spot_quantity, action_id, product_id, out_of_balance, chip, vendor):
    if active_spot == 'yes':
        active_spot = True
    else:
        active_spot = False
    if incoming == 'yes':
        incoming = True
    else:
        incoming = False
    try:
        product_quantity = int(product_quantity)
    except ValueError:
        product_quantity = 0
    try:
        max_spot_quantity = int(max_spot_quantity)
    except ValueError:
        max_spot_quantity = 0
    try:
        action_id = int(action_id)
    except ValueError:
        action_id = 0 
    try:
        product_id = int(product_id)
    except ValueError:
        product_id = 0    
    if out_of_balance == 'yes':
        out_of_balance = True
    else:
        out_of_balance = False

    storage = Storage(locker, locker_level, level_spot, active_spot, incoming, \
    product_type, product_quantity,  max_spot_quantity, action_id, product_id, \
    out_of_balance, chip, vendor)
    db_session.add(storage)




    db_session.commit()

if __name__ == "__main__":

    #pass
#    add_new_product_to_sqlite('10235611', 'rip_strong_with_wow3_sp11', 'D8', 'I_TRY_TO_ADD_NEW3', '', \
 #       '43', 'used', 'yes', 'yes', 'yes', '05.11.2016', 'Nope_heipful_89', 'that_boy', '', '', '', '', \
 #       'Moscow', '')

    add_new_product_to_sqlite('10235611', 'rip_strong_with_wow3_sp12', 'D8', 'I_TRY_TO_ADD_NEW4', '', '43', 'used', 'yes', 'yes', 'yes', '05.11.2016', 'Nope_heipful_89', 'that_boy', '', '', '', '', 'Moscow', '')

#    add_quantity_to_storage('1', '1', '1', 'yes', 'yes', 'colored', '3000', '3000', '', '51', \
#        '', 'Abraham48_07BB', 'my_Frend')

