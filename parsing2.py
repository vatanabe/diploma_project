# парсинг файла второго типа
import os
import fnmatch
from collections import Counter
path = os.path.join("/", "projects", "test2")
# Путь указываем в составном виде, чтобы он подходил для разных ОС
for file in os.listdir(path):
    # Поиск среди файлов текущей папки по маске
    if fnmatch.fnmatch(file, 'MIN_DESIGN*'):
        full_path = os.path.join("/", path, file)
with open(full_path, 'r', encoding='utf-8') as myfile:
    lines = myfile.readlines()  # Чтение файла построчно
    data_list = []
    for string in lines:
        # Извлекаем из каждой строки нужное значение и создаем список с
        # этими значениями
        data_list.append(string[27:43].rstrip())
        # Счётчик количества одинаковых значений
    values_count2 = Counter(data_list)
