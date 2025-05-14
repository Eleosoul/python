def my_fn(a, b):
    a = a + 1
    c = a + b
    print(f'a {id(a)}')
    print(f'b {id(b)}')
    return c

num_one = 10
num_two = 5

res = my_fn(num_one, num_two)
print(res)
print(num_one)

print('')

print(f'num_one a: {num_one}')
print(f'id: {id(num_one)}')
print('')
print(f'num_two b: {num_two}')
print(f'id: {id(num_two)}')
print('')

# a 4360580048
# b 4360579856
# 16
# 10
#
# num_one a: 10
# id: 4360580016

print('')

def increase_person_age(person):
    person['age'] += 1
    print(f'person {id(person)}')
    return person

person_one = {
	'name': 'Bob',
	'age': 21
}

print(f'person_one {id(person_one)}')

increase_person_age(person_one)
print(person_one['age']) # 22
