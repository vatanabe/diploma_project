from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine
from products_db import Product, ProductInFile, InputFile
import os
import fnmatch

engine = create_engine('sqlite:///data.sqlite')

db_session = scoped_session(sessionmaker(bind=engine))
#поиск по коду продукта из файла первого вида
def search1(code):
    for (product_name,) in db_session.query(Product.product_name).filter_by(product_code=code, used=1):#, special_design=0): 
        return product_name
#поиск по коду спецдизайна из файла второго типа
def search2(code):
    for (product_name,) in db_session.query(Product.product_name).filter_by(special_code=code): 
        return product_name
#поиск по коду спецдизайна из файла третьего типа
def search3(code):
    for (product_name,) in db_session.query(Product.product_name).filter_by(city_code=code): 
        return product_name
#поиск id в таблице текущих работ по коду продукта (необходимо дополнить поиск по id файла в работе)
def search4(product_name, file_id):
    for (id,) in db_session.query(Product.id).filter_by(product_name=product_name):
        for (id,) in db_session.query(ProductInFile.id).filter_by(product_id=id, input_file_id=file_id):
            return id
#поиск значения статуса продукта в текущих работах для изменения цвета строки (подтверждение) (необходимо дополнить поиск по id файла в работе)
def change_color(product_name, file_id):
    for (id,) in db_session.query(Product.id).filter_by(product_name=product_name):
        for (product_in_file_status,) in db_session.query(ProductInFile.product_in_file_status).filter_by(product_id=id, input_file_id=file_id):
            return product_in_file_status
#поиск стартового количества продукта для производства
def start_quantity(product_name, file_id):
    for (id,) in db_session.query(Product.id).filter_by(product_name=product_name):
        for (input_quantity,) in db_session.query(ProductInFile.input_quantity).filter_by(product_id=id, input_file_id=file_id):
            return input_quantity
#поиск количества выполненнго продукта в текущих работах (необходимо дополнить поиск по id файла в работе)
def produced_quantity(product_name, file_id):
    for (id,) in db_session.query(Product.id).filter_by(product_name=product_name):
        for (produced_quantity,) in db_session.query(ProductInFile.produced_quantity).filter_by(product_id=id, input_file_id=file_id):
            return produced_quantity
#поиск количества бракованного продукта в текущих работах (необходимо дополнить поиск по id файла в работе)
def reject_quantity(product_name, file_id):
    for (id,) in db_session.query(Product.id).filter_by(product_name=product_name):
        for (reject_quantity,) in db_session.query(ProductInFile.reject_quantity).filter_by(product_id=id, input_file_id=file_id):
            return reject_quantity
#функция поиска названия файла в папке для отображения его на странице текущей работы (бесполезная??)
def file_search():
    path = os.path.join("/", "projects", "test2")
    #Путь указываем в составном виде, чтобы он подходил для рахных ОС
    for file in os.listdir(path):
        if fnmatch.fnmatch(file, 'OMG*'):  #Поиск среди файлов текущей папки по маске
            filename = file
            return filename
#поиск названий файлов, которые в работе
def started_files():
    filenames = []
    for (input_file_name,) in db_session.query(InputFile.input_file_name).filter_by(file_status='started'):
        if input_file_name not in filenames:
            filenames.append(input_file_name)
    return filenames
#поиск id файлов, которые в работе
def started_ids(filename):
    for (id,) in db_session.query(InputFile.id).filter_by(input_file_name=filename):
        return id
#создание адреса страницы для id
def href_id(digit):
    href = str(digit)
    return str(href)
#создание корня адреса страницы для определённого типа файла
def href_root(filename):
    if 'OMG' in filename:
        href = '/omg/'
    elif 'MIN_DESIGN' in filename:
        href = '/md/'
    elif 'TOP_LOCAL_MIFARE' in filename:
        href = '/mif/'
    return str(href)
#создание списка продуктов в работе
def started_products(file_id):
    started_products = []
    for (product_id,) in db_session.query(ProductInFile.product_id).filter_by(input_file_id=file_id):
        for (product_name,) in db_session.query(Product.product_name).filter_by(id=product_id):
            started_products.append(product_name)
    return started_products
