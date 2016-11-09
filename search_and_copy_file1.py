import os
import shutil
import fnmatch
import time
from products_db import Action
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker
from datetime import datetime

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
        action = Action(datetime.now(), 0, filename, 0, 'product_id', 'reason', 'bot')      
        for (input_file_name,) in db_session.query(Action.input_file_name):
            if input_file_name != filename:
                copy_file()
                db_session.add(action)
                db_session.commit()
                time.sleep(10)
            else:
                print("replay")
                time.sleep(10)
                
while True:
    add_action()
    time.sleep(10)