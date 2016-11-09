from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Boolean, Date
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///blog.sqlite')

db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    product_bin = Column(String(8))
    product_name = Column(String(50), unique=True)
    product_code = Column(String(2))
    special_code = Column(String(12))
    city_code = Column(String(20))
    parent_id = Column(Integer, ForeignKey('products.id'))
    used = Column(Boolean)
    special_design = Column(Boolean)
    contactless_interface = Column(Boolean)
    link_contactless = Column(Boolean)
    add_date = Column(Date)
    prod_chip = Column(String(20))
    prod_vendor = Column(String(20))
    front_side_image = Column(String(50))
    front_side_print = Column(String(50))
    back_side_image = Column(String(50))
    back_side_print = Column(String(50))
    city = Column(String(20))
    images_pixels = Column(String(9))

    

    def __init__(self, product_bin=None ,product_name=None, product_code=None, special_code=None, \
        city_code=None, parent_id=None, used=None, special_design=None, contactless_interface=None, \
        link_contactless=None, add_date=None, prod_chip=None, prod_vendor=None,front_side_image=None, \
        front_side_print=None, back_side_image=None, back_side_print=None, city=None, images_pixels=None):
        self.product_bin = product_bin
        self.product_name = product_name
        self.product_code = product_code
        self.special_code = special_code
        self.city_code = city_code
        self.parent_id = parent_id
        self.used = used
        self.special_design = special_design
        self.contactless_interface = contactless_interface
        self.link_contactless = link_contactless
        self.add_date = add_date
        self.prod_chip = prod_chip
        self.prod_vendor = prod_vendor
        self.front_side_image = front_side_image
        self.front_side_print = front_side_print
        self.back_side_image = back_side_image
        self.back_side_print = back_side_print
        self.city = city
        self.images_pixels = images_pixels


    def __repr__(self):
        return '<Product {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {}>' .format(\
            self.product_bin, self.product_name, self.product_code , self.special_code, \
            self.city_code, self.parent_id, self.used, self.special_design, \
            self.contactless_interface, self.link_contactless, self.add_date, \
            self.prod_chip, self.prod_vendor, self.front_side_image, self.front_side_print, \
            self.back_side_image, self.back_side_print, self.city, self.images_pixels)


class Action(Base):
    __tablename__ = 'actions'
    id = Column(Integer, primary_key=True)
    action_datetime = Column(DateTime)
    action_type = Column(Integer)
    input_file_name = Column(String(40))
    quantity = Column(Integer)
    product_id = Column(Integer, ForeignKey('products.id'))
    reason = Column(String(50))
    produced_by = Column(String(20))


    def __init__(self, action_datetime=None, action_type=None, input_file_name=None, quantity=None, \
        product_id=None, reasone=None, produced_by=None):
        self.action_datetime = action_datetime
        self.action_type = action_type
        self.input_file_name = input_file_name
        self.quantity = quantity
        self.product_id = product_id
        self.reasone = reasone
        self.produced_by = produced_by

    def __repr__(self):
        return '<Product {} {} {} {} {} {} {}>' .format(\
        self.action_datetime, self.action_type, self.input_file_name, self.quantity, \
        self.product_id, self.reasone, self.produced_by)


class Storage(Base):
    __tablename__ = 'storage'
    id = Column(Integer, primary_key=True)
    locker = Column(String(2))
    locker_level = Column(String(2))
    level_spot = Column(String(1))
    active_spot = Column(Boolean)
    incoming = Column(Boolean)
    product_type = Column(String(20))
    product_quantity = Column(Integer)
    max_spot_quantity = Column(Integer)
    action_id = Column(Integer, ForeignKey('actions.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    out_of_balance = Column(Boolean)
    chip = Column(String(20))
    vendor = Column(String(20))


    def __init__(self, locker=None, locker_level=None, level_spot=None, active_spot=None, \
        incoming=None, product_type=None, product_quantity=None, max_spot_quantity=None, \
        action_id=None, product_id=None, out_of_balance=None, chip=None, vendor=None):
        self.locker = locker
        self.locker_level = locker_level
        self.level_spot = level_spot
        self.active_spot = active_spot
        self.incoming = incoming
        self.product_type = product_type
        self.product_quantity = product_quantity
        self.max_spot_quantity = max_spot_quantity
        self.action_id = action_id
        self.product_id = product_id
        self.out_of_balance = out_of_balance
        self.chip = chip
        self.vendor = vendor

    def __repr__(self):
        return '<Product {} {} {} {} {} {} {} {} {} {} {} {} {}>' .format(\
        self.locker, self.locker_level, self.level_spot, self.active_spot, self.incoming, \
        self.product_type, self.product_quantity, self.max_spot_quantity, self.action_id, \
        self.product_id, self.out_of_balance, self.chip, self.vendor)

#new
#white
#colored
#colored_reject
#perso_reject
#input_reject
#demo
#test
#pre_perso



if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)