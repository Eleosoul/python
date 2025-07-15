# 1. Создать функцию под названием `merge_list_to_dict`
# 2. У функции должно быть 2 параметра
# 3. Функция должна объединять два списка
# 4. Конвертировать объект zip в словарь и верните его из функции
# 5. Вызвать функцию передав есть два списка в качестве аргументов
# 6. Вывести результат в терминал


def merge_list_to_dict(list1, list2):
    zip_list = zip(list1, list2)
    zip_to_dict = dict(zip_list)
    return zip_to_dict

my_list = ['one', 'two', 'three']
other_list = ['1', '2', '3']

result_merge = merge_list_to_dict(my_list, other_list)

print(result_merge)

def get_posts_info(name, posts_qty):
    info = f"{name} wrote {posts_qty} posts"
    return info
info = get_posts_info(name='Bogdan', posts_qty=25)

