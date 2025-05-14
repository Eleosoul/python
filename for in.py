

for el in [1, 'anc', True, None]:
    print(type(el))
    print(el)

my_dict = {
	'x': 10,
	'y': True,
	'z': 'abc'
}

print('----')

for key in my_dict:
    print(type(key))
    print(key, my_dict[key])

print('----')
my_object = {
	'x': 10,
	'y': True
}

for item in my_object.items():
    key, value = item
    print(key, value)

