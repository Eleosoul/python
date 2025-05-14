# Задача 1
#  1. Создать словарь с несколькими ключами, значения которых должны быти типа str
#  2. Создать новый словарь на основании существующего, значение которых должны быть все в верхнем регистре и вывести новый словарь в терминал
#
# Задача 2
# 1. Создать список со значениями типа строка
# 2. Из этого списка создать новый список в котором останутся только строки длина которых больше 3 и новый список вывести в терминал

some_dict = {
    'name': 'Alexander',
    'last_name': 'Ovcharov',
    'middle_name': 'Dmitrievich'
}

upper_case_dict = {k: v.upper() for k, v in some_dict.items()}

print(upper_case_dict)


some_list = ['alex', '02', 'ovcharov', 'car', 'orange', 'people']

filter_list = [item for item in some_list if len(item) > 3]

print(filter_list)


