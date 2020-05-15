documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
    {"type": "ins", "number": "12345", "nickname": "Евгений Пупкин"}
]

# полки
directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


def add():
    num = input('Введите номер: ')
    typ = input('Введите тип: ')
    nam = input('Введите имя владельца: ')
    directory = input('Введите номер полки, на котором он будет храниться: ')
    new_dict = {'type': typ, 'number': num, 'name': nam}

    for directory_1 in directories.keys():  # 1 2 3
        if directory in directory_1 == directory_1:
            print(f"Такая полка {directory} уже существует")
            break
    else:
        # directories[directory_1].append(str(num))
        directories[directory] = [num]
        documents.append(new_dict)
        print(f"Добавлено на полку {directory}")


def people():
    document_number = input("Введите номер документа: ")
    for document in documents:
        if document.get('number') == document_number:
            print(document.get('name'))
            break
    else:
        print("Такого человека нет в базе")


def shelf():
    num_racks = input('Введите номер документа: ')
    for key, value in directories.items():
        if num_racks in value == value:
            print('Номер стелажа', key)
            break
    else:
        print('такого документа нет')


def lists():
    print('Список всех документов:')
    for item in documents:
        print(item['type'], ',', item['number'], ',', item['name'])


def All_people():
    print('Список всех имён:')
    for i in documents:
        print(i['name'])


def main():
    while True:
        docs = input('_________________________________ \nВедите команду:\n\
p - команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;\n\
l - команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";\n\
s - команда, которая спросит номер документа и выведет номер полки, на которой он находится;\n\
a - команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца \n'
                     'и номер полки, на котором он будет храниться.\n\
n -  команда, которая выведет имена всех владельцев документа \n\
q - команда для выхода, \n->')

        if docs == 'p':
            people()
        elif docs == 's':
            shelf()
        elif docs == 'l':
            try:
                lists()
            except KeyError as error:
                print(f'Ошибка: неправильный ключ словаря: {error}, посмотрите документ внимательнее')
        elif docs == 'a':
            add()
        elif docs == 'n':
            try:
                All_people()
            except KeyError as error:
                print(f'Ошибка: неправильный ключ словаря: {error}, посмотрите документ внимательнее')
        elif docs != 'a' and docs != 'l' and docs != 's' and docs != 'a' and docs != 'n':
            break


main()
