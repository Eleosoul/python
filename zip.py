fruits = ['aaple', 'banana', 'lime']
quantities = [100, 70, 50]

availabulity = [True, False, True, True]

fruit_qtys_zip = zip(fruits, quantities)
#
# print(fruit_qtys_zip)
#
# fruit_qtys_list = list(fruit_qtys_zip)
#
# print(fruit_qtys_list)

fruit_dict = dict(fruit_qtys_zip)

print(fruit_dict)