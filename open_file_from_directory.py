import os

path = os.path.join("/", "example", "text.txt")
#Путь указываем в составном виде, чтобы он подходил для рахных ОС
with open(path, "r") as myfile: 
#Указать путь к файлу и режим работы с файлом
    print myfile.read()
    # обработка файла