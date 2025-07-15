num_one = 222
num_two = 222

# if num_one == num_two:
#     print("Равно")
# elif num_one > num_two:
#     print(f"{num_one} больше чем {num_two}")
# elif num_one < num_two:
#     print(f"{num_one} меньше чем {num_two}")
# else:
#     print('Ошибка')

if (num_one > 0 and
    num_two > 0 and
    isinstance(num_one, int) and
    isinstance(num_two, int)):
    print("Both positive")