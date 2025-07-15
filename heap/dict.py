# Практика
my_disk = {}




print(id(my_disk))
print(type(my_disk))

my_disk['brand'] = 'Apple'
my_disk['price'] = 80

print(my_disk)

print(my_disk.__doc__ )
print(my_disk.items())
print(my_disk.keys())
print(my_disk.popitem()) # не рекомендуется использовать так как словарь не упорядоченный лучше использовать del

print(my_disk.get('alex', 'hdd'))
# print(my_disk.clear())

# копирование

new_disk = my_disk.copy()

print(my_disk)
print(new_disk)


# Конвертация других значений в словарь

my_list = [['first', 0], ['Second', True]]

my_dict = dict(my_list)

print(my_dict)



