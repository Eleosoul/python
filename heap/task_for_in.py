# Задача 1
# 1. создать функцию `dict_to_list` которая будет конвертировать словарь в список кортежей
# 2. функция должна принимать словарь а возвращять список кортежей в каждом кортеже должны быть пары `(key, value)` из словаря
# 3. если значение ключа это целое число то его нужно умножить на 2 перед добавлением в кортеж
#
# Задача 2
# 1. Создать функцию `filter_list` которая будет фильтровать список
# 2. У функции должно быть два параметра список и тип значения
# 3. Функция должна вернуть новый список в котором останутся только значения того типа который был передан в вызове функции вторым аргументом


def dict_to_list(dict_val):
    if not isinstance(dict_val, dict):
        return f"A dictionary is required, you entered: {type(dict_val)}"

    my_list = []
    for k, v in dict_val.items():
        if type(v) == int:
            my_list.append((k, v * 2))
        else:
            my_list.append((k, v))

    return my_list

def filter_list(list_val, type_val):
    my_list = []
    for i in list_val:
        if type(i) == type_val:
            my_list.append(i)

    return my_list





my_dict = {
    'number': 1,
    'name': 'Joe',
    'is_admin': True,
    'full_access': False,
    'id': 25,
    'distance': 13.5,
}

template_list = [23, 56, 'hew', 'hex', True, 23.5, 4545.454, (1, 2), {'hello': 'world'}]

hello = 1

print(dict_to_list(my_dict))
print(filter_list(template_list, int))
print(filter_list(template_list, bool))
print(filter_list(template_list, str))
print(filter_list(template_list, dict))
print(filter_list(template_list, tuple))

