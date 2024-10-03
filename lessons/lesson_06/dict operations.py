import random

people = {
    'Den': 20,
    'Alex': 30,
    'Ivan': 33
}


# people.keys() = dict_keys type
# for name in people.keys():  # йдемо по ключам 'Den', 'Alex', 'Ivan'
#     print(name)
#
# # for name in list(people.keys()):  # ==> for name in ['Den', 'Alex', 'Ivan']
# #     print(name)
#
# for age in people.values():  # йдемо по значення 20, 30, 33
#     print(age)
#
# for age in list(people.values()):  # ==> for name in [20, 30, 33]
#     print(age)


dict_items = list(people.items())

print(dict_items)

for name, age in people.items():  # йдемо по значення tupl'am (Den, 20), (Alex, 30), (Ivan, 33)
    print(f'My name is {name}, I\'m {age} years old')



my_dict_2 = dict([
    (20, 30),
    (40, 50)
])
print(my_dict_2)

empty_dict = dict()

empty_dict.update(my_dict_2)
empty_dict.update(people)

print(empty_dict)


lst_cmp = [k**2 for k in range(10)]  # сворити список з квадратами числе від 0 до 9

print(lst_cmp)


dct_cmp = {number: number**2 for number in range(10, 20) if number != 13}  # словник число: квадрат числа
dct_cmp = {
    number: random.choice(list(people.keys()))  # random.choice(...) - випадкове значення з
           for number in range(10, 20) if number != 13  # 10, 11, 12, 14,..., 19
}   # словник число: випадкове ім'я

print(dct_cmp)