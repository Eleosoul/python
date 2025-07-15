users = [
    {
	    'user_id': 134,
	    'user_name': 'Alice'
    },
    {
	    'user_id': 831,
	    'user_name': 'Bob'
    }
]

# чтобы вывести имя Bob нужно
print(users[1]['user_name'])

# Можно использовать переменные

my_fruit = 'apple'
other_fruit = 'banaba'
new_fruit = 'lime'

all_fruits = [my_fruit, other_fruit, new_fruit]

print(all_fruits)

my_nums = [10, 50, 0, 5, 5, 100]

other_nums = my_nums.copy()

print(my_nums.count(5))
my_nums.append(15)
print(my_nums)

my_nums.insert(3, 45)

print(my_nums)

my_nums.clear()

print(my_nums)

print(my_nums.extend('abc'))
print(my_nums)

print(id(my_nums))
my_nums2 = my_nums.copy()
print(id(my_nums2))