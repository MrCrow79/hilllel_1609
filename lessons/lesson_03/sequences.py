# string
# list
# tuple
# dict

my_name = 'Denys ' # має 6 елементів 0,1,2,3,4,5,6(пробіл)
my_list = ['D', 'e', 'n', 'y', 's'] # має 5 елементів 0,1,2,3,4
my_typle = ('D', 'e', 'n', 'y', 's') # має 5 елементів 0,1,2,3,4
my_dict = {'D':1, 'e': 'asd'} # має 2 елементів,  ('D', 1), ('e', 'asd')

my_set = {1,2,4,3,4} # - має довжину, та 4 елемнети: 0,1,2,3

# len(obj) -  повертає довжину obj

# print(len(my_name))
# print(len(my_dict))
# print(len(my_set))


# # актуально для str, tuple, list
# print(my_name[0])  # "перший" елемент, рахуються з 0
# print(my_name[2])  # третій елемент
# print(my_list[-1])  # останній елемент
# print(my_typle[-2])  # передостанній елемент
# print(my_name[6])  # неіснуючий еемент - буде помилка

# slice - вирізати

print(my_name[1:5:1])   # syntax [start(включаючі):end(не включаючі):step]
print(my_name[1:5])   # syntax [start(включаючі):end(не включаючі)]
print(my_name[0:5:2])   # кожний 2й символ

my_list_10 = [1,2,3,4,5,6,7,8,9,0] # indexes: 0,1,2,3,4,5,6,7,8,9

# slices працють по індексах

print(my_list_10[6:])  # з індекса номер 6 до кінця
print(my_list_10[6:len(my_list_10)])  # [6:10]  [індекс 6: індекс 9]

print(my_list_10[:9])  # з першого до 9 == [0:9]
print(my_list_10[:9])  # з першого до 9

print(my_name[::2])  # еквівалент [0:len(my_name):1]
print(my_name[::2])  # еквівалент [0:len(my_name):2]

print(my_name[::-1])  # еквівалент [0:len(my_name):-1] з кінця в початок

# excel_data = open(...)  # взяти дані з excel документу
# excel_data = excel_data[1:]  # відкинути строку з іменами колонок

# user = db.get(...)  # отримали список юзерів по запиту
#
# # перевірка, що в списку user тільки 1 юзер
#
# user = user[0]

# неможна брати елемент по індексу в set, dict
# print(my_set[0])
# print(my_dict[0])


