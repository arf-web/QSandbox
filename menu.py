from git.sandtools import *
import os


print("""Добро пожаловать в конструктор интерактивных рассказов QBox!
Чтобы выбрать действие, введите комнаду и нажмите ENTER.""")

while True:
    print("""Для начала игры введите "начать";
Чтобы перейти в конструктор локаций - "конструктор".""")
    answer = fixput("начать", "конструктор", "выход")
    if answer == "конструктор":
        os.system('python3 builder.py')
    if answer == "начать":
        os.system('python3 play.py')
    if answer == "выход":
        print("Ещё увидимся!")
        exit(0)