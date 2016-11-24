import os
import shutil
import fnmatch
import time
from collections import Counter
from products_db import Action, InputFile, ProductInFile, Product
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker
from datetime import datetime
from parsing1 import values_count1
from parsing2 import values_count2
from parsing3 import data
from product_search import search1, search2, search3
from product_amount import amount1, amount2, amount3

path = os.path.join("/", "projects", "test")
#Путь указываем в составном виде, чтобы он подходил для рахных ОС

engine = create_engine('sqlite:///data.sqlite')

db_session = scoped_session(sessionmaker(bind=engine))

def get_filenames():
    filenames = []

    for file in os.listdir(path):
        if fnmatch.fnmatch(file, 'OMG*'):
            filenames.append(file)
        elif fnmatch.fnmatch(file, 'MIN_DESIGN*'):
            filenames.append(file)
        elif fnmatch.fnmatch(file, 'TOP_LOCAL_MIFARE*'):
            filenames.append(file)
    return filenames

def copy_file():
    for file in os.listdir(path):
        
        if fnmatch.fnmatch(file, 'OMG*'): #Поиск среди файлов текущей папки по маске
            full_path = os.path.join("/", path, file) #Создание полного пути копируемого файла
            new_path = os.path.join("/", "projects", "test2", file) #Создание полного пути нового копируемого файла
            shutil.copyfile(full_path, new_path) #Выполнение копирования файла
            path2 = os.path.join("/", "projects", "test2")
            
            #Путь указываем в составном виде, чтобы он подходил для рахных ОС
            for file in os.listdir(path2):
                if fnmatch.fnmatch(file, 'OMG*'): #Поиск среди файлов текущей папки по маске
                    full_path = os.path.join("/", path, file)
            
            with open(full_path, 'r') as myfile: #Чтение файла построчно
                lines = myfile.readlines() #Список, содержащий строки файла
                data = lines[1:-1] #Обрезаем шапку и последнюю строку
                data_list = []
                for string in data:
                    data_list.append(string[272:274]) #Извлекаем из каждой строки нужное значение и создаем список с этими значениями
                data_length = len(data_list)
                values_count1 = Counter(data_list) #Счётчик количества одинаковых значений
        
        elif fnmatch.fnmatch(file, 'MIN_DESIGN*'): #Поиск среди файлов текущей папки по маске
            full_path = os.path.join("/", path, file) #Создание полного пути копируемого файла
            new_path = os.path.join("/", "projects", "test2", file) #Создание полного пути нового копируемого файла
            shutil.copyfile(full_path, new_path) #Выполнение копирования файла
            path2 = os.path.join("/", "projects", "test2")
            #Путь указываем в составном виде, чтобы он подходил для разных ОС
            for file in os.listdir(path2):
                if fnmatch.fnmatch(file, 'MIN_DESIGN*'): #Поиск среди файлов текущей папки по маске
                    full_path = os.path.join("/", path, file)
            
            with open(full_path, 'r', encoding='utf-8') as myfile: #Чтение файла построчно
                lines = myfile.readlines() #Чтение файла построчно
                data_list = []
                for string in lines:
                    data_list.append(string[27:43].rstrip())  #Извлекаем из каждой строки нужное значение и создаем список с этими значениями
                values_count2 = Counter(data_list) #Счётчик количества одинаковых значений
        
        elif fnmatch.fnmatch(file, 'TOP_LOCAL_MIFARE*'): #Поиск среди файлов текущей папки по маске
            full_path = os.path.join("/", path, file) #Создание полного пути копируемого файла
            new_path = os.path.join("/", "projects", "test2", file) #Создание полного пути нового копируемого файла
            shutil.copyfile(full_path, new_path) #Выполнение копирования файла
            path2 = os.path.join("/", "projects", "test2")
        
        #Путь указываем в составном виде, чтобы он подходил для рахных ОС
        for file in os.listdir(path2):
            if fnmatch.fnmatch(file, 'TOP_LOCAL_MIFARE*'): #Поиск среди файлов текущей папки по маске
                full_path = os.path.join("/", path, file)
        
        with open(full_path, 'r') as myfile: #Чтение файла построчно
            lines = myfile.readlines()
            data = {}
            
            if fnmatch.fnmatch(file, '*ShChPR*'):
                count = len(lines)
                data = {'ShChPR': count}
            
            elif fnmatch.fnmatch(file, '*Barnaul*'):
                count = len(lines)
                data = {'ShChPR': count}
            
            elif fnmatch.fnmatch(file, '*UlanUde*'):
                count = len(lines)
                data = {'Barnaul': count}
            
            elif fnmatch.fnmatch(file, '*Zhigulyovsk*'):
                count = len(lines)
                data = {'Zhigulyovsk': count}
            
            elif fnmatch.fnmatch(file, '*Novosibirsk*'):
                count = len(lines)
                data = {'Novosibirsk': count}
            
            elif fnmatch.fnmatch(file, '*Tolyaytti_pp*'):
                count = len(lines)
                data = {'Tolyaytti_pp': count}
            
            elif fnmatch.fnmatch(file, '*Novoaltaisk_pp*'):
                count = len(lines)
                data = {'Novoaltaisk_pp': count}
            
            elif fnmatch.fnmatch(file, '*Orenburg_pp*'):
                count = len(lines)
                data = {'Orenburg_pp': count}

            elif fnmatch.fnmatch(file, '*Arhangelsk*'):
                count = len(lines)
                data = {'Arhangelsk': count}

def add_action(filenames):
    for filename in filenames:
        action = Action(action_datetime = datetime.now(), action_type  = "file_copy", input_file_name = filename, produced_by = 'bot')
        count = 0      
        for (input_file_name,) in db_session.query(Action.input_file_name):
            if input_file_name == filename:
                print("replay")
                count += 1  

            else:
                pass

        if count == 0:
            copy_file()
            db_session.add(action)
            db_session.commit()
            time.sleep(10)

        else:
            pass

def add_input_file(filenames):
    for filename in filenames:
        if "OMG" in filename:
            file_type = "OMG"
        elif "MIN" in filename:
            file_type = "MIN_DESIGN"
        elif "TOP_LOCAL" in filename:
            file_type = "TOP_LOCAL_MIFARE"

        if db_session.query(InputFile.input_file_name).filter(InputFile.input_file_name == filename).count() > 0:
            print("replay")    
        else:
            print("else")
            copy_file()
            input_file = InputFile(input_file_name = filename, input_file_type = file_type, action_file_time = datetime.now(), file_status = "started")
            db_session.add(input_file)
            db_session.commit()

            if "OMG" in filename:
                for code in values_count1:
                    product = Product
                    product = product.query.filter_by(product_code=code, used=1).first()
                    print(product)
                    input_quantity = values_count1[code]
                    product_in_file = ProductInFile(product_id = product.id, input_quantity = input_quantity, reject_quantity = 0, produced_quantity = input_quantity, 
                    product_in_file_status = "started", input_file_id = input_file.id)
                    db_session.add(product_in_file)
                    db_session.commit()

            elif "MIN_DESIGN" in filename:
                for code in values_count2:
                    product = Product
                    product = product.query.filter_by(special_code=code).first()
                    print(product)
                    input_quantity = values_count2[code]
                    product_in_file = ProductInFile(product_id = product.id, input_quantity = input_quantity, reject_quantity = 0, produced_quantity = input_quantity, 
                    product_in_file_status = "started", input_file_id = input_file.id)
                    db_session.add(product_in_file)
                    db_session.commit()

            elif "TOP_LOCAL_MIFARE" in filename:
                for code in data:
                    product = Product
                    product = product.query.filter_by(city_code=code).first()
                    print(product)
                    input_quantity = data[code]
                    product_in_file = ProductInFile(product_id = product.id, input_quantity = input_quantity, reject_quantity = 0, produced_quantity = input_quantity, 
                    product_in_file_status = "started", input_file_id = input_file.id)
                    db_session.add(product_in_file)
                    db_session.commit()


if __name__ == "__main__":
    while True:
        filenames = get_filenames()
        add_action(filenames)
        add_input_file(filenames)
        time.sleep(10)
