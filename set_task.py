#
#
# 1. Создать набор с несколькими элементами типа int
# 2. Добавить в него еще один элемент
# 3. Создать еще один набор с несколькими элементами, некоторые должны быть такие как и в первом наборе
# 4. Найти общие элементы в двух набрах и попестить их в новый набор
# 5. Конвертировать результат в список и вывести в тернимал

my_set = {14, 157, 77, 88, 120}

my_set.add(12)

other_set = {'abc', 14, 777, 77, 55, 12, 120}

new_set = list(my_set.intersection(other_set))

print(new_set)
print(type(new_set))