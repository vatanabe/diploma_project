import os
import fnmatch
from collections import Counter
path = os.path.join("/", "projects", "test2")
#Путь указываем в составном виде, чтобы он подходил для рахных ОС
for file in os.listdir(path):
    if fnmatch.fnmatch(file, 'OMG*'): #Поиск среди файлов текущей папки по маске
        full_path = os.path.join("/", path, file)
with open(full_path, 'r') as myfile: #Чтение файла построчно
    lines = myfile.readlines()
    data = lines[1:-1]
    data_list = []
    for string in data:
        data_list.append(string[272:274])
    values_count = Counter(data_list)