import os
import shutil
# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

def make_dir(path):
    try:
        os.mkdir(path)
    except FileExistsError:
        print('Такая директория уже существует')

def rem_dir(path):
    os.removedirs(path)

[make_dir('dir_{}'.format(i)) for i in range(1, 10)]
[rem_dir('dir_{}'.format(i)) for i in range(1, 10)]

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
def list_dir():
    print([i for i in os.listdir() if os.path.isdir(i)])


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

# shutil.copy("D:\\test.txt", "D:\\test2.txt")

# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющей работать с папками текущей директории.
# Утилита должна иметь меню выбора действий,
# 1. Перейти в папку
# 2. Просмотреть текущую папку
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано / удалено / перешел",
# "Невозможно создать / удалить / перейти"

# Для решения данной задачи используйте алгоритм из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

#from easy import make_dir, rem_dir, list_dir
def change_dir(file):
    os.chdir(file)

answer = ''
while answer != 'q':
    answer = input("Давайте поработаем? (Y/N/n/q)")
    if answer == 'Y':
        print("Что желаете сделать? ")
        print(" [1] - перейти в папку")
        print(" [2] - посмотреть текущую папку")
        print(" [3] - удалить папку")
        print(" [4] - создать папку")
        do = int(input("Укажите номер действия: "))

        if do == 1:
            change_dir()

        elif do == 2:
            list_dir()

        elif do == 3:
            rem_dir()

        elif do == 4:
            make_dir()


        else:
            pass

    elif answer == 'N':
        print("До свидания!")
    else:
        print("Неизвестный ответ")