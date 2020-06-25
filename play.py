from git.sandtools import *

locs = []
with open("locs.json", "r") as file_locs:
     locs = json.load(file_locs)

if locs == []:
    print("Нечего начинать: нет ни одной локации. Стартовая локация должна называться \"старт\". Возврат в меню.")
if locs != []:
    print("""Вы начинаете игру. Для возврата в меню, введите "в меню".""")

def moving(room):
    print(f"""
{room[title]}
{room[description]}

Введите действие:""")
    trans = room[links]
    for button in trans.values():
        print(button)

    way = fixput(*trans.values(), "в меню")
    for namelocs, buttons in trans.items():
        if way == "в меню":
            return "в меню"
        elif way == buttons:
            return namelocs


way = "старт"
lastname = ""
while way != "в меню" and locs != []:
    no_loc = True
    for room in locs:
        if room[nameloc] == way:
            lastname = way
            way = moving(room)
            no_loc = False
            break
    if way != "в меню" and no_loc:
        print("Ошибка: там нет контента. Вы остаётесь в текущей локации. Попробуйте другой переход или сообщите о проблеме автору истории.")
        way = lastname



