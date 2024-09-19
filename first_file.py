print('Hello world')


# float -  числа з палваючою точкою, десятичні дроби
my_float = 15.5555

# string - строки
my_string = 'my Name'

# list - список, можна додавати/видаляти/міняти елементи
my_list = [1,2, 12.5, 'asd', [1, 'asd']]

# tuple - кортеж, незмінний
my_tuple = (1,2, 12.5, 'asd', [1, 'asd'])

# set - сет, множина, унікальні значення
my_set = {1, 2, 'asd'}

# dict - словник
my_dict = {'var_name': 'var_value', 'var_name2': 'var_value', 'third_value': [None, [{1: 2}]]}

# bool - логічне значення
my_bool = True # or False

# None
my_none = None

# =  це присвоювання, наприклад a = 10 означає що в а ми "покладемо" 10
# == це порівняння  a == b , це порівння чи а дорівнює б


# int - цілі числа
my_int = 14


# print(14)
# print(my_int)

my_int = 17
my_new_int = my_int  # my_new_int буде мати таку саму адресу що і my_int

# print(my_int)
# print(my_new_int)
#
# print(id(my_int))
# print(id(my_new_int))


my_int = 18

# print(my_int)
# print(my_new_int)
#
# print(id(my_int))
# print(id(my_new_int))

# if = якщо умова:

if my_int == 18:
    print('my_int = 18')
    if my_float == 5:
        print('my_float = 5')


print(my_int)
print('------------------')

# sum_2_numbers = 5 + 10
# diff = 55 - 17
# mult =  10 * 20
# div = 40 / 2
#
#
# print(sum_2_numbers)
# print(diff)
# print(mult)
# print(div)

#  case 1
# div = int(40 / 2)  # div = int(20.0); div = 20
# print(div)
#
# #  case 2
# div = 40 / 2  # div = 20.0
# div = int(div)  # div = int(20.0) == 20
# print(div)
#
# #  case 3
# div = 40 / 2  # div = 20.0
# div_int = int(div)  # div_int = int(20.0) = 20
# print(div_int)
#
# #  case 4
# div = 40 / 2  # div = 20.0
# print(int(div))
# print(div)

# case 1 == case 2
# case 3 - має 2 змінних в результаті
# case 4 має 1 змінну яка = 20.0

# print('Hello')
# print(20)  # -> print(str(20))  -> перетворить в строку
#
# print(None)
#
name = 'Denys'
surname = 'Merezhkin'

# print('Hello', name, surname, 6, 22.3, sep=' ')

full_name = name + surname

# print('Hello', name + surname)
# print('Hello', full_name)
# print('Hello', 6 + 15, my_int + my_float)
print('Hello', 6 + 15, int(my_int + my_float))
print('Hello', 6 + 15, my_int + my_float)


# snake_case - for variables
# CamelCase - для імен класів
# VARIABLES_NAME - константи капсом + _ між словами
# pep8 - правила синтаксису
# pythonic way

MY_NAME = 'denys'

# MyName = 'Serg'  # невірно
#
# myName = 'Alex2' # невірно
my_name, my_age = 'Denys', 33

copy_age, copy_name  = my_age, my_name

# print(my_name)
# print(my_age)
# # print(MyName)
# # print(myName)
# print(MY_NAME)

print('age', copy_age)
print('name', copy_name)

copy_age, copy_name  = copy_name, copy_age  # спосіб поміняти змінні місцями

print('age', copy_age)
print('name', copy_name)

