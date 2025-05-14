my_range = range(5)

print(my_range)
print(type(my_range))
print(my_range[0])

for n in my_range:
    print(f"Бросок номер: {n + 1}")

for n in range(12, 25, 5):
    print(n)

print(list(range(12, 15)))

print(my_range.index(4))
print(my_range.count(22))

my_list = []
other_range = range(10)

for n in other_range:
    my_list.append(n)

print(my_list)