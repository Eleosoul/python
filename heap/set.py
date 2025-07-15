my_set = {'abc', 'd', 'f', 'y'}
other_set = {'a', 'f', 'd'}

print(my_set.intersection(other_set))
print(other_set.intersection(my_set))
print(my_set.intersection('abcd'))

print(my_set.union(other_set))

print(other_set.issubset(my_set))
print(my_set.issubset(other_set))
print(my_set.issuperset(other_set))

print(my_set.difference(other_set))

print(my_set.discard('d'))
print(my_set)

my_set2 = my_set.copy()
print(my_set2)

my_set.add('t')
my_set2.add('l')

print(my_set.symmetric_difference(my_set2))

a = my_set
b = my_set2
print("_______")
print(a)
print(b)

print((a | b) - (a & b))


print(my_set & my_set2)