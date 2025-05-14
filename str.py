# Практика строк

my_name = 'Alex'
print(my_name)
# Alex

greeting = "Hello from Almaty"
print(greeting)
# Hello from Almaty

#Тип строк

my_name = 'Alex'
# Alex

print(type(my_name))
# <class 'str'>

print(id(my_name))
# 5657676865

#Три пары ковычек для многострочной строки

info_msg = """Hello
From this mutli 
sting sting))
"""

print(info_msg)


# Узнать длину строки функция len()
my_name = 'Alexandr'
print(len(my_name))

# Так как строка это последовательность символов то можно вытащить каждый элемет как с упорядоченным списком
print(my_name[0])

# Можно получить диапазон индексов пример:
print(my_name[3:6])

# Методы строки
my_comment = "my fist short comment"

# Функция upper Принимает строку и возвращяет все в верхнем регистре
print(my_comment.upper())

# Функция replace заменяет символы или подстроки
print(my_comment.replace('short', 'long'))

# Функция count считает количество вхождений определенного элемента в списке или строке
print(my_comment.count('s'))

# Функция индекс подстоки или символа
print(my_comment.index('f'))

# Функция capitalaze возвращякт строку в которй будет с заглавной
print(my_comment.capitalize())

# Функция lower возвращяет сроку в нижнем регистре
print (my_comment.lower())