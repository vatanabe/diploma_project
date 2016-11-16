import os
import shutil
import fnmatch
import time
from products_db import Action, InputFile, ProductInFile
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker
from datetime import datetime
from parsing1 import values_count1
from product_search import search1, search2, search3
from product_amount import amount1, amount2, amount3

path = os.path.join("/", "projects", "test")
#Путь указываем в составном виде, чтобы он подходил для рахных ОС

engine = create_engine('sqlite:///data.sqlite', echo=True)

db_session = scoped_session(sessionmaker(bind=engine))

filenames = []

for file in os.listdir(path):
    if fnmatch.fnmatch(file, 'OMG*'):
        filenames.append(file)

def copy_file():
    for file in os.listdir(path):
        if fnmatch.fnmatch(file, 'OMG*'): #Поиск среди файлов текущей папки по маске
            full_path = os.path.join("/", path, file) #Создание полного пути копируемого файла
            new_path = os.path.join("/", "projects", "test2", file) #Создание полного пути нового копируемого файла
            shutil.copyfile(full_path, new_path) #Выполнение копирования файла

def add_action():
    for filename in filenames:
        action = Action(action_datetime = datetime.now(), action_type  = "file_copy", input_file_name = filename, produced_by = 'bot')
        count = 0      
        for (input_file_name,) in db_session.query(Action.input_file_name):
            if input_file_name == filename:
                print("replay")
                count += 1     
            else:
                print("else")
        if count == 0:
            copy_file()
            db_session.add(action)
            db_session.commit()
            time.sleep(10)
        else:
            print("else2")

def add_input_file():
    for filename in filenames:
        if "OMG" in filename:
            file_type = "OMG"
        elif "MIN" in filename:
            file_type = "MIN_DESIGN"
        elif "TOP_LOCAL" in filename:
            file_type = "TOP_LOCAL_MIFARE"
        input_file = InputFile(input_file_name = filename, input_file_type = file_type, action_file_time = datetime.now(), file_status = "started")
        count = 0      
        for (input_file_name,) in db_session.query(InputFile.input_file_name):
            if input_file_name == filename:
                print("replay")
                count += 1     
            else:
                print("else")
        if count == 0:
            copy_file()
            db_session.add(input_file)
            db_session.commit()
            time.sleep(10)
        else:
            print("else2")

def add_product_in_input_file():
    for name in values_count1:

    product_in_file = ProductInFile(product_id = "???", input_quantity, reject_quantity = 0, produced_quantity = 0, 
        product_in_file_status = "started", input_file_id = '???')
    db_session.add(product_in_file)
    db_session.commit()

while True:
    add_action()
    add_input_file()
    time.sleep(10)
