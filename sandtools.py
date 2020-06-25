"""
sandtools хранит список функций, использующихся в других модулях проекта.

"""

from git.templates import *
import json

def decorator_fixput(func):
    def inner(*args):
        """
        Функция fixput (fixed input) служит для чтения команд конструктора локаций.
        Командой не может быть пустая строка, или значение, отличающееся от ожидаемого.
        Ожидаемые команды передаются аргументами *args
        При вводе неверной команды, fixput просит пользователя попробовать снова, объяснив его ошибку.
        fixput подходит для ввода названий: пустая строка не принимается.
        """
        buffer = func()
        while buffer == "":
            print(tmp_empty_input)
            buffer = func()
        if args != ():
            while buffer not in args:
                print(tmp_choose_command, args)
                buffer = func()
        return buffer
    return inner

fixput = decorator_fixput(input)



def dict_to_format(dict):
    """Преобразование содержимого в словаря в форматированную строку. ';' разделяет пары, а '--' разделяет ключ со значением."""
    return "; ".join(list(" -- ".join(couple) for couple in list(map(list, dict.items()))))


def preview(newloc):
    print(f"""Предварительный просмотр:
    {nameloc} {newloc[nameloc]}
    {title} {newloc[title]}
    {description} {newloc[description]}
    {links} {dict_to_format(newloc[links])}""")


def print_names(locs):
    print("Все локации в игре:")
    for location in locs:
        print(location[nameloc], end=" | ")
    print()


def pass_if_empty(some_loc):
    answer = input()
    if answer != "":
        some_loc = answer


def save_to_json(locs):
    with open("locs.json", "w") as file_locs:
        json.dump(locs, file_locs, indent=5, sort_keys=True, ensure_ascii = False)


    # старая функция, использовавшаясь для проверки на пустой ввод.
# def if_no_empty(buffer):
#     while buffer == "":
#         print(empty_input)
#         buffer = input()
#     else:
#         return buffer