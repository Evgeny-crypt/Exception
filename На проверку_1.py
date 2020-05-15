def include(number):
    number = number.split(' ')

    g = ['-', '+', '/', '*']
    if '+' in number:
        f = int(number[1]) + int(number[2])
        print(f)
    elif '-' in number:
        f = int(number[1]) - int(number[2])
        print(f)
    elif '*' in number:
        f = int(number[1]) * int(number[2])
        print(f)
    elif '/' in number:
        f = int(number[1]) / int(number[2])
        print(f)
    else:
        assert g in number, "нет в списке <- (-, +, /, *) -> вводится в начало строки"


try:
    include(input('Введите число в формате + 2 3: '))
except AssertionError as error:
    print('Ошибка: ', error)
except ZeroDivisionError as error:
    print('Ошибка: Делить на ноль нельзя: ', error)
except ValueError as error:
    print('Ошибка: вводить только в польской записи (+ 2 2) и только цифры: ', error)
