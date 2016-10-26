from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///blog.sqlite')

db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    product_name = Column(String(50), unique=True)
    product_code = Column(String(2))
    special_code = Column(String(12), unique=True)
    contactless_interface = Column(Boolean)
    link_contactless = Column(Boolean)
    chip = Column(String(20))
    vendor = Column(String(20))
    add_date = Column(DateTime)
    front_side_image = Column(String(50))
    front_side_print = Column(String(50))
    back_side_image = Column(String(50))
    back_side_print = Column(String(50))
    city = Column(String(20))
    images_pixels = Column(String(9))

    

    def __init__(self, product_name=None, product_code=None, special_code=None, \
        contactless_interface=None, link_contactless=None, chip=None, \
        vendor=None, add_date=None, front_side_image=None, front_side_print=None, \
        back_side_imager=None, back_side_print=None, city=None, images_pixels=None):
        self.product_name = product_name
        self.product_code = product_code
        self.special_code = special_code
        self.contactless_interface = contactless_interface
        self.link_contactless = link_contactless
        self.chip = chip
        self.vendor = vendor
        self.add_date = add_date
        self.front_side_image = front_side_image
        self.front_side_print = front_side_print
        self.back_side_image = back_side_image
        self.back_side_print = back_side_print
        self.city = city
        self.images_pixels = images_pixels


    def __repr__(self):
        return '<Product {} {} {} {} {} {} {} {} {} {} {} {} {} {}>' .format(\
            self.product_name, self.product_code , self.special_code, \
            self.contactless_interface, self.link_contactless, self.chip, \
            self.vendor, self.add_date, self.front_side_image, self.front_side_prin, \
            self.back_side_image, self.back_side_print, self.city, self.images_pixels)


class Action(Base):
    __tablename__ = 'actions'
    id = Column(Integer, primary_key=True)
    action_date = Column(DateTime)
    quantity = Column(Integer)
    action_type = Column(Integer)
    product_id = Column(Integer, ForeignKey('products.id'))
    reason = Column(String(50))
    produced_by = Column(String(20))


    def __init__(self, action_date=None, quantity=None, action_type=None, \
        product_id_frome=None, product_id_to=None, reasone=None, produced_by=None):
        self.action_date = action_date
        self.quantity = quantity
        self.action_type = acion_type
        self.product_id = product_id
        self.reasone = reasone
        self.produced_by = produced_by

    def __repr__(self):
        return '<Product {} {} {} {} {} {}>' .format(\
        self.action_date, self.quantity, self.action_type, \
        self.product_id, self.reasone, self.produced_by)


class Storage(Base):
    __tablename__ = 'storage'
    id = Column(Integer, primary_key=True)
    locker = Column(String(2))
    locker_level = Column(String(2))
    level_spot = Column(String(1))
    product_type = Column(String(20))
    product_quantity = Column(Integer)
    action_id = Column(Integer, ForeignKey('actions.id'))
    product_id = Column(Integer, ForeignKey('products.id'))


    def __init__(self, locker=None, locker_level=None, level_spot=None, \
        product_type=None, product_quantity=None, action_id=None, product_id=None):
        self.locker = locker
        self.locker_level = locker_level
        self.level_spot = level_spot
        self.product_type = product_type
        self.product_quantity = product_quantity
        self.action_id = action_id
        self.product_id = product_id

    def __repr__(self):
        return '<Product {} {} {} {} {} {} {}>' .format(\
        self.locker, self.locker_level, self.level_spot, \
        self.product_type, self.product_quantity, self.action_id, self.product_id)




if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)