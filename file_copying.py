import shutil # Подключаем модуль
import os #Подключаем модуль
import fnmatch #Подключаем модуль

#(копируемый файл, путь копирования)
shutil.copyfile(r'/test/py/test.txt', r'/test/py/new_test.txt')
#Проверка наличия файла в директории
os.path.exists('text.txt')
#Поиск среди файлов текущей папки по маске *.txt
for file in os.listdir('.'):
    if fnmatch.fnmatch(file, '*.txt'):
        print file