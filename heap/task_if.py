def route_info(dict_val):
    if type(dict_val)  is not dict:
        return f"a dictionary is required, you entered: {type(dict_val)}"

    if dict_val.get('distance') and type(dict_val['distance']) is int:
        return f"Distance to you distanation in {dict_val['distance']}"

    if (dict_val.get('speed') and
        type(dict_val['speed']) is int and
        dict_val.get('time') and
        type(dict_val['time']) is int):
        return f"Distance to you distanation is {dict_val['speed'] * dict_val['time']}"

    return "No distance info is available"


my_dict = {
    'ome': 1
}

my_dict2 = {
    'distance': 24,
    'meter': 'Mm',
}

my_dict3 = {
    'time': 4,
    'speed': 25,
    'meter': "Km",
}

my_dict4 = {
    'distance': 2.5,
    'meter': 'Mm',
}

my_dict5 = {
    'time': 3.5,
    'speed': 25,
    'meter': "Km",
}


my_list = ['distance', 24]


print(route_info(my_dict))
print(route_info(my_dict2))
print(route_info(my_dict3))
print(route_info(my_dict4))
print(route_info(my_dict5))
print(route_info(my_list))