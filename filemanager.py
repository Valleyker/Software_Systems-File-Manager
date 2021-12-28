import os
import sys
import shutil

path = "C:/Users/user/MP/workdir"
os.chdir(path)  # Переместимся в папку workDir, тем самым сделаем ее основной


def makeDir(dirName):  # Создание папки
    os.mkdir(path + "/" + dirName)
    print("make dir " + path + "/" + dirName)


def removeDir(dirName):  # Удаление папки
    os.rmdir(path + "/" + dirName)
    print("remove dir " + path + "/" + dirName)


def makeFile(fileName):  # Создание файла
    filepath = 'C:/Users/204489/Downloads/workdir' + "/" + fileName
    f = open(filepath, "a")
    print("make file " + path + "/" + fileName)
    f.close()


def removeFile(fileName):  # Удаление файла
    filepath = 'C:/Users/204489/Downloads/workdir' + "/" + fileName
    os.remove(filepath)
    print("remove file " + path + "/" + fileName)


def renameFile(fileName, newFileName):  # Переименование
    os.rename(path + "/" + fileName, path + "/" + newFileName)
    print("rename file " + path + "/" + fileName)


def textFile(fileName):  # Заполнение файла
    filepath = 'C:/Users/204489/Downloads/workdir' + "/" + fileName
    f = open(filepath, "w")
    text = str(input())
    f.write(text)
    f.close()


def readFile(fileName):  # Просмотр содержимого текстового файла
    filepath = 'C:/Users/204489/Downloads/workdir' + "/" + fileName
    f = open(filepath, "r")
    file_contents = f.read()
    print(file_contents)
    f.close()


def сhangeDir(dirName):  # Перемещение пользователя
    os.chdir(dirName)
    print(os.getcwd())


def movingFiles(fileName, dirName):  # Перемещение файла в другую папку
    filepath = path + "/" + dirName + "/" + fileName
    os.replace(fileName, filepath)


def copyFile(fileName, copyPath):  # Копирование файла в другую папку
    copyPath = path + "/" + copyPath
    shutil.copy(path + '/' + fileName, copyPath)


while True:

    print("")
    print("1. Создание папки")
    print("2. Удаление папки")
    print("3. Создание файла")
    print("4. Удаление файла")
    print("5. Переименование")
    print("6. Запись текста в файл")
    print("7. Просмотр содержимого текстового файла")
    print("8. Изменить расположение ползователя")
    print("9. Перемещение файла в другую папку")
    print("10. Копирование файла в другую папку")
    print("11. Выход")
    print("")

    command = input("Введите номер команды: ")
    command = command.split()
    if command[0] == "1":
        x = input("Введите название папки ")
        command.append(x)
        makeDir(command[1])
    elif command[0] == "2":
        x = input("Введите название папки ")
        command.append(x)
        removeDir(command[1])
    elif command[0] == "3":
        x = input("Введите название файла ")
        command.append(x)
        makeFile(command[1])
    elif command[0] == "4":
        x = input("Введите название файла ")
        command.append(x)
        removeFile(command[1])
    elif command[0] == "5":
        x = input("Введите название файла ")
        command.append(x)
        x2 = input("Введите новое название файла ")
        command.append(x2)
        renameFile(command[1], command[2])
    elif command[0] == "6":
        x = input("Введите название файла ")
        command.append(x)
        textFile(command[1])
    elif command[0] == "7":
        x = input("Введите название файла ")
        command.append(x)
        readFile(command[1])
    elif command[0] == "8":
        x = input("Введите название папки ")
        command.append(x)
        pathChange(command[1])
    elif command[0] == "9":
        x = input("Введите название файла ")
        command.append(x)
        x2 = input("Введите название папки ")
        command.append(x2)
        movingFiles(command[1], command[2])
    elif command[0] == "10":
        x = input("Введите название файла ")
        command.append(x)
        x2 = input("Введите название папки ")
        command.append(x2)
        copyFile(command[1], command[2])
    elif command[0] == "11":  # Выход
        sys.exit()
