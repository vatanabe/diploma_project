import os
import fnmatch

path = os.path.join("/", "projects", "test2")
#Путь указываем в составном виде, чтобы он подходил для рахных ОС
for file in os.listdir(path):
    if fnmatch.fnmatch(file, 'OMG*'): #Поиск среди файлов текущей папки по маске
        full_path = os.path.join("/", path, file)
with open(full_path, 'r') as myfile: #Чтение файла построчно
    lines = myfile.readlines()
    data = lines[1:-1]
    for string in data:
        print(string[272:274])