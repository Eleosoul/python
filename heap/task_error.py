my_dict = {
    'image_id': 443434,
    'image_title': 'Ocean',
    'image': '232323cc3c34'
}

my_dict2 = {
    'image': '232323cc3c34',
    'colors': 'RGB'
}

def image_info(dict):
    if ('image_id' and 'image_title') not in dict:
        raise TypeError("A key is needed 'image_ids' and 'image_title'")
    return print(f"Image {dict['image_title']} has id {dict['image_id']}")

image_info(my_dict)
image_info(my_dict2)


my_dict = {
    'image_id': 443434,
    'image_title': 'Ocean',
    'image': '232323cc3c34'
}

my_dict2 = {
    'image': '232323cc3c34',
    'colors': 'RGB'
}


def image_info(info_dict):
    # проверка должна быть отдельной для каждого ключа
    if 'image_id' not in info_dict or 'image_title' not in info_dict:
        raise TypeError("Ожидаются ключи 'image_id' и 'image_title'")

    return f"Image '{info_dict['image_title']}' has id {info_dict['image_id']}"


# Обработка ошибок через try-except
try:
    print(image_info(my_dict))
except TypeError as e:
    print(f"Ошибка: {e}")

try:
    print(image_info(my_dict2))
except TypeError as e:
    print(f"Ошибка: {e}")

