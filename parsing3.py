import os
import fnmatch
from collections import Counter
path = os.path.join("/", "projects", "test2")
#Путь указываем в составном виде, чтобы он подходил для рахных ОС
for file in os.listdir(path):
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