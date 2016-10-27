import os
import fnmatch
from collections import Counter
path = os.path.join("/", "projects", "test2")
#Путь указываем в составном виде, чтобы он подходил для рахных ОС
for file in os.listdir(path):
    if fnmatch.fnmatch(file, 'OPT_LOCAL_MIFARE*'): #Поиск среди файлов текущей папки по маске
        full_path = os.path.join("/", path, file)
with open(full_path, 'r') as myfile: #Чтение файла построчно
    lines = myfile.readlines()
    if fnmatch.fnmatch(file, '*ShChPR*'):
        pass
        return len(lines)
    elif fnmatch.fnmatch(file, '*Barnaul*'):
        pass
        return len(lines)
    elif fnmatch.fnmatch(file, '*UlanUde*'):
        pass
        return len(lines)
    elif fnmatch.fnmatch(file, '*Zhigulyovsk*'):
        pass
        return len(lines)
    elif fnmatch.fnmatch(file, '*Novosibirsk*'):
        pass
        return len(lines)
    elif fnmatch.fnmatch(file, '*Tolyaytti_pp*'):
        pass
        return len(lines)
    elif fnmatch.fnmatch(file, '*Novoaltaisp_pp*'):
        pass
        return len(lines)
    elif fnmatch.fnmatch(file, '*Orenburg_pp*'):
        pass
        return len(lines)
    elif fnmatch.fnmatch(file, '*Arhangelsk*'):
        pass
        return len(lines)