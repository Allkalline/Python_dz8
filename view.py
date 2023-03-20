def get_op():
    op = int(input(" 1 - импорт. \n 2 - экспорт. \n 3 - выход. \n "))
    return op


def get_data():
    name = input('имя: ')
    surname = input('фамилия: ')
    telephone = input('телефон: ')
    data_str = name + " " + surname + " " + telephone + "\n"
    return data_str

def find_person():
    data_str = input('Введи параметр: ')
    return data_str

def ask2():
    return int(input('1 - изменить, 2 - удалить, 3 - назад: '))
