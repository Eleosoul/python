from copy import deepcopy

number1 = 10
number2 = 10
number3 = 10

print(id(number1))
print(id(number2))
print(id(number3))

print('')
tuple1 = (1, 2, 3)
tuple2 = (1, 2, 3)

print(id(tuple1))
print(id(tuple2))

print("")
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = [1, 2, 3]


for lst in [list1, list2, list3]:
    print(id(lst), lst)

list3.append(4)
print('')

for lst in [list1, list2, list3]:
    print(id(lst), lst)

print('')

dict1 = {
    'name': 'alex'
}

dict2 = dict1

dict3 = dict2.copy()

for dic in [dict1, dict2, dict3]:
    print(id(dic), dic)

print('')

info = {
    'id': 1,
    'reviews': [1, 2, 3]
}

info_c = info.copy()
info_deep_c = deepcopy(info)

print(id(info), info, info['reviews'], id(info['reviews']))
print(id(info_c), info_c, info_c['reviews'], id(info_c['reviews']))
print(id(info_deep_c), info_deep_c, info_deep_c['reviews'], id(info_deep_c['reviews']))
