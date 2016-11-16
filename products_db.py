from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Boolean, Date
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///data.sqlite')

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

    def __repr__(self):
        return '<Product {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {}>' .format(
        self.product_bin,
        self.product_name,
        self.product_code,
        self.special_code,
        self.city_code,
        self.parent_id,
        self.used,
        self.special_design,
        self.contactless_interface,
        self.link_contactless,
        self.add_date,
        self.prod_chip,
        self.prod_vendor,
        self.front_side_image,
        self.front_side_print,
        self.back_side_image,
        self.back_side_print,
        self.city,
        self.images_pixels
        )


class Action(Base):
    __tablename__ = 'actions'
    id = Column(Integer, primary_key=True)
    action_datetime = Column(DateTime)
    action_type = Column(String(20))
    input_file_name = Column(String(50))
    quantity = Column(Integer)
    product_id = Column(Integer, ForeignKey('products.id'))
    reason = Column(String(50))
    produced_by = Column(String(20))
    product = relationship("Product", backref="actions")

    def __repr__(self):
        return '<Product {} {} {} {} {} {} {}>' .format(
        self.action_datetime,
        self.action_type,
        self.input_file_name,
        self.quantity,
        self.product_id,
        self.reasone,
        self.produced_by
        )


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
    product = relationship("Product", backref="storage")

    def __repr__(self):
        return '<Product {} {} {} {} {} {} {} {} {} {} {} {} {}>' .format(
        self.locker,
        self.locker_level,
        self.level_spot,
        self.active_spot,
        self.incoming,
        self.product_type,
        self.product_quantity,
        self.max_spot_quantity,
        self.action_id,
        self.product_id,
        self.out_of_balance,
        self.chip,
        self.vendor
        )

class InputFile(Base):
    __tablename__ = 'input_file'
    id = Column(Integer, primary_key=True)
    input_file_name = Column(String(50))
    input_file_type = Column(String(20))
    action_file_time = Column(DateTime)
    file_status = Column(String(20))
    products_in_file = relationship("ProductInFile", backref="input_file")

    def __repr__(self):
        return '<Product {} {} {} {} {}>' .format(
        self.input_file_name,
        self.input_file_type,
        self.action_file_time,
        self.file_status
        )

class ProductInFile(Base):
    __tablename__ = 'products_in_file'
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    input_quantity = Column(Integer)
    reject_quantity = Column(Integer)
    produced_quantity = Column(Integer)
    product_in_file_status = Column(String(20))
    input_file_id = Column(Integer, ForeignKey('input_file.id'))
    product = relationship("Product")

    def __repr__(self):
        return '<ProductInFile {} {} {} {} {} {}>' .format(
        self.product_id,
        self.input_quantity,
        self.reject_quantity,
        self.produced_quantity,
        self.product_in_file_status,
        self.input_file_id
        )


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)