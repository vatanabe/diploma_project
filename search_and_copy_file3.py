import os
import shutil
import fnmatch
import time

path = os.path.join("/", "projects", "test")
#Путь указываем в составном виде, чтобы он подходил для рахных ОС

def copy_file():
    for file in os.listdir(path):
        if fnmatch.fnmatch(file, 'TOP_LOCAL_MIFARE*'): #Поиск среди файлов текущей папки по маске
            full_path = os.path.join("/", path, file) #Создание полного пути копируемого файла
            new_path = os.path.join("/", "projects", "test2", file) #Создание полного пути нового копируемого файла
            shutil.copyfile(full_path, new_path) #Выполнение копирования файла

while True:
    copy_file()
    time.sleep(5)