# print("Технический комментарий: импортирован модуль Builder")

from git.sandtools import *                                         # свои функции, например fixput()


locs = []                                                           # в этот пустой список импортируется json-ка с локациями
with open("locs.json", "r") as file_locs:                           # каждая локация - словарь, и состоит из
     locs = json.load(file_locs)                                    # назания, заголовка, описания и словаря с переходами
                                                                    # переход - это пара ключ=имя_кнопки, значение=название_локации
while True:
    save_to_json(locs)
    print(tmp_create_loc)                                       # инструкции команд "создать", "редактировать", "меню"

    command = fixput("создать", "редактировать", "меню", "проверка")            # в command запишется введённая команда
    if command == "проверка":
        namelocs = []
        false_trans = 0
        for loc in locs:
            namelocs.append(loc[nameloc])
        for room in locs:
            for trans_name in room[links].keys():
                if trans_name not in namelocs:
                    false_trans += 1
                    print(f"В локации \"{room[nameloc]}\" переход \"{room[links][trans_name]}\" ведёт в несуществующую локацию \"{trans_name}\".")
        print(f"Найдено ошибок: {false_trans}")
        print()





    if command == "редактировать":                                  # итак мы решили редактировать имеющиеся локации
        while True:                                                 # закцикливаем ввод, пока не напишут "назад"
            save_to_json(locs)
            if locs == []:                                          # если список локаций пуст
                print(tmp_no_locs)                                  # сообщаем об этом юзеру: "нет локаций"
                break
            else:                                                   # но если нет
                print(tmp_loc_list)                             # юзер-инструкции "имя локи для редактирования"
                loclist = []                                    # создаём список для записи названий имеющихся локаций из словаря
                for location in locs:                           # пробегаемся по локациям-словарям из списка
                    print(location[nameloc])                    # чтобы вывести их названия
                    loclist.append(location[nameloc])           # и добавить в список loclist

                edit_loc = fixput()                             # юзер вводит имя локации для редактирования
                if edit_loc == "удалить все":
                    locs = []
                    print("Все локации удалены.")
                    continue

                if edit_loc != "назад":                         # и если он ввёл не "назад"
                    if edit_loc not in loclist:                 # смотрим, не отсутствует ли такая локация в loclist
                        print("Такой локации не существует.")   # цикл возвращает его ко вводу локации для редактирования
                    else:                                       # но если локация нашлась
                        for location in locs:                   # снова пробегаемся по списку локаций
                            if location[nameloc] == edit_loc:   # чтобы найти словарь соответствующий введённому имени локи
                                edit_loc = location             # и переназначить на него переменную

                        preview(edit_loc)
                        print(tmp_input_loc_name + tmp_empty_to_pass)               # здесь и далее юзер-инструкции по вводу
                        pass_if_empty(edit_loc[nameloc])                            # здесь и далее редактирование локации в locs

                        preview(edit_loc)
                        print(tmp_input_loc_title + tmp_empty_to_pass)
                        pass_if_empty(edit_loc[title])

                        preview(edit_loc)
                        print(tmp_input_loc_desc + tmp_empty_to_pass)
                        pass_if_empty(edit_loc[description])


                        print("Желаете изменить переходы? (да | нет)")
                        answer = fixput("да", "нет")
                        if answer == "нет":
                            print("Изменения сохранены.")
                            continue
                        while True:                             # редактирование переходов открывает новый цикл
                            print(tmp_transitions)              #
                            print(tmp_change_transition)        # доп юзер-инструкция для ред-я переходов
                            print()
                            print(f"Переходы в локации \"{edit_loc[nameloc]}\": {dict_to_format(edit_loc[links])}")
                            print(tmp_new_transition)

                            print_names(locs)
                            print(tmp_input_loc_button)        # здесь и далее юзер-инструкции по вводу
                            locbut = fixput()                   # временная переменная для ключа

                            print(tmp_input_button_name)
                            namebut = fixput()                     # временная переменная для значения

                            edit_loc[links][locbut] = namebut      # при отсутствии ключа создастся новый переход
                            print()
                            print(f"""Переходы в локации "{edit_loc[nameloc]}": {dict_to_format(edit_loc[links])}""")

                            print("Хотите изменить/добавить ещё один переход? (да | нет | удалить все переходы)")
                            answer = fixput("да", "нет", "удалить все переходы")
                            if answer == "да":
                                continue                        # перекидывает ко вводу названия перехода
                            if answer == "удалить все переходы":
                                print("""Переходы удалены. Вы сможете добавить, начав редактирование локации заново.""")
                                edit_loc[links] = {}
                                break
                            elif answer == "нет":
                                print("Изменения сохранены.")
                                break                           # перекидывает ко вводу названия локации для ред-я
                else:
                    break                                       # перекидывает к "создать", "ред-ть", "меню"

    if command == "меню":                                       # выводит из модуля (не завершено)
        break

    if command == "создать":                                    # повторяет функционал редатирования, с небольшими отличиями
        newloc = {nameloc: "", title: "", description: "", links: {}}   # сначала всё вводится в пустой словарь
        print(tmp_input_loc_data)                               # который затем добавляется в locs

        print(tmp_input_loc_name)
        newloc[nameloc] = fixput()
        preview(newloc)

        print(tmp_input_loc_title)
        newloc[title] = fixput()
        preview(newloc)

        print(tmp_input_loc_desc)
        newloc[description] = fixput()
        preview(newloc)

        while True:
            print(tmp_transitions)
            print_names(locs)
            print(tmp_input_loc_button)
            locbut = fixput()

            print(tmp_input_button_name)
            namebut = fixput()

            newloc[links][locbut] = namebut                        # который впоследствии добавляется в newloc
            preview(newloc)
            print("Хотите добавить ещё один переход? (да | нет | удалить все переходы)")
            answer = fixput("да", "нет", "удалить все переходы")
            if answer == "да":
                continue
            elif answer == "удалить все переходы":
                newloc[links] = {}
                print("""Переходы удалены. Вы сможете добавить позже, через меню "редактировать".""")
                break

            elif answer == "нет":
                break                                           # вывод из цикла добавления переходов
                                                                # проверка данных локации перед сохранением
        # preview(newloc)
        print(f"""Введите "да" чтобы, сохранить локацию, или "нет" для отмены.""")
        answer = fixput("да", "нет")
        if answer == "нет":
            print("Отменено.")
        elif answer == "да":
            locs.append(newloc)                                 # добавление локации в locs при подтверждении
            print(f"Локация \"" + newloc[nameloc] + "\" сохранена.")


# print(locs)


# Вы стоите в центре комнаты средневековой башни. Вас окружают прекрасно сохранившиеся, словно, не тронутые столетиями, предметы из прошлого. Кругая платформа музейного лифта издаёт предупредительный скрип: как только вы сойдёте с неё, она опустится и створки в полу задвинутся.



