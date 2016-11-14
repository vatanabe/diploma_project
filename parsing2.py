import os
import fnmatch
from collections import Counter
path = os.path.join("/", "projects", "test2")
#Путь указываем в составном виде, чтобы он подходил для разных ОС
for file in os.listdir(path):
    if fnmatch.fnmatch(file, 'MIN_DESIGN*'): #Поиск среди файлов текущей папки по маске
        full_path = os.path.join("/", path, file)
with open(full_path, 'r', encoding='utf-8') as myfile: #Чтение файла построчно
    lines = myfile.readlines() #Чтение файла построчно
    data_list = []
    for string in lines:
        data_list.append(string[27:43].rstrip())  #Извлекаем из каждой строки нужное значение и создаем список с этими значениями
    values_count2 = Counter(data_list) #Счётчик количества одинаковых значений