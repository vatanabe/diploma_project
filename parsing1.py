# парсинг файла первого типа
import os
import fnmatch
from collections import Counter
path = os.path.join("/", "projects", "test2")
# Путь указываем в составном виде, чтобы он подходил для рахных ОС
for file in os.listdir(path):
    # Поиск среди файлов текущей папки по маске
    if fnmatch.fnmatch(file, 'OMG*'):
        full_path = os.path.join("/", path, file)
with open(full_path, 'r') as myfile:  # Чтение файла построчно
    lines = myfile.readlines()  # Список, содержащий строки файла
    data = lines[1:-1]  # Обрезаем шапку и последнюю строку
    data_list = []
    for string in data:
        # Извлекаем из каждой строки нужное значение и создаем список с
        # этими значениями
        data_list.append(string[272:274])
    data_length = len(data_list)
    # Счётчик количества одинаковых значений
    values_count1 = Counter(data_list)
