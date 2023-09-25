from datetime import datetime
import csv


def clear_of_file():
    with open('memo.csv', 'w') as file:
        writer = csv.writer(file, delimiter=';')


def write_to_file(args, do="a+"):
    with open('memo.csv', do, newline='', encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(args)


def read_to_file():
    with open('memo.csv', 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=';', quotechar='"')
        a = []
        for row in enumerate(reader, start=1):
            a.append(row)
        return a


def data_for_new_note():
    header_note = input("Введите заголовок: ")
    body_note = input("Введите текст заметки: ")
    date_create_note = datetime.now().date().strftime('%d.%m.%Y')
    time_create_note = datetime.now().time().strftime('%H:%M')
    data_of_note = [header_note, body_note, date_create_note, time_create_note]
    return data_of_note


def sort_list_notes(array_data):
    temp = 0
    i = 1
    for i in range(len(array_data) - 1):
        for j in range(len(array_data) - i):
            if array_data[i][1][2].replace('.', '') > array_data[j + i][1][2].replace('.', ''):
                temp = array_data[j + i][1][2]
                array_data[j + i][1][2] = array_data[i][1][2]
                array_data[i][1][2] = temp
    return array_data


def search_note(array_data):
    print(
        "Поиск по ...\n" "1 - ID\n" "2 - Заголовку\n" "3 - Дате\n"
    )
    munu_search = int(input("Выбирите команду поиска: "))
    if munu_search == 1:
        search_element = input("Введите значение: ")
        find_note = []
        for id, i in array_data:
            if id == int(search_element):
                find_note.append(i)
        return find_note
    elif munu_search == 2:
        search_element = input("Введите значение: ")
        find_note = []
        for id, i in array_data:
            if i[0] == search_element:
                find_note.append(i)
        return find_note
    elif munu_search == 3:
        print("Формат ввода даты: день.месяц.год(пример:05.03.2000)")
        search_date = input("Введите значение: ")
        find_note = []
        for id, i in array_data:
            if i[2] == search_date:
                find_note.append(i)
        return find_note
    else:
        print("Введите корректный номер команды")


def print_note(array_data):
    if array_data == None:
        print("Такого значения в списке заметок нет")
    else:
        for i in array_data:
            print(
                f"\nЗаголовок: {i[0]}\nТекст заметки: {i[1]}\nДата создания: {i[2]}, Время создания: {i[3]}\n")


def delete_note(array_data):
    p = int(input("Введите номер ID: "))
    for i in array_data:
        if i[0] == p:
            array_data.remove(i)
    clear_of_file()
    if len(array_data) > 0:
        for id, i in array_data:
            write_to_file(i)
    print("Заметка успешно удалена")


def editing(array_data):
    id_note = int(input("Введите номер заметки для редактирования: "))
    for i in range(len(array_data)):
        if array_data[i][0] == id_note:
            array_data[i][1][0] = input("Введите заголовок: ")
            array_data[i][1][1] = input("Введите текст заметки: ")
            array_data[i][1][2] = datetime.now().date().strftime('%d-%m-%Y')
            array_data[i][1][3] = datetime.now().time().strftime('%H:%M')
    return array_data


flag = True
number_id = 0
while flag:
    print("\n1 - Создать заметку\n" "2 - Вывести весь список заметок\n" "3 - Редактировать заметку\n"
          "4 - Удалить заметку по ID\n" "5 - Найти заметку\n" "6 - Очистить список заметок\n" "0 - Выход из программы")
    number_menu = int(input("Введите номер команды: "))
    if number_menu == 1:
        write_to_file(data_for_new_note(), "a+")
        print("\nНовая заметка сохранена")
        continue
    elif number_menu == 2:
        list_note = sort_list_notes(read_to_file())
        for id, i in list_note:
            print(
                f"ID - {id}\nЗаголовок: {i[0]}, Текст заметки: {i[1]}, Дата создания: {i[2]}, Время создания: {i[3]}\n")
    elif number_menu == 3:
        correct_note = editing(read_to_file())
        clear_of_file()
        for id, i in correct_note:
            write_to_file(i)
        print("Заметка отредактирована")
    elif number_menu == 4:
        delete_note(read_to_file())
    elif number_menu == 5:
        print_note(search_note(read_to_file()))
    elif number_menu == 6:
        clear_of_file()
    elif number_menu == 0:
        flag = False
    else:
        print("Неверная команда")
