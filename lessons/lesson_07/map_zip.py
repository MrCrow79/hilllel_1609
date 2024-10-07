my_descr = 'My   name  is   Den  '.split(' ')  # => list
print(my_descr)
#
# print(list(map(len, my_descr)))  # => print([len(k) for k in my_descr])
#
# print(list(filter(len, my_descr)))

# print(pow(2, 5))
#
# base_numbers = [2, 4, 6, 8, 10]
# powers = [1, 2, 3, 4, 5]
# numbers_powers = list(map(pow, base_numbers, powers))
#
# print(numbers_powers)  # [2, 16, 216, 4096, 100000]

# len_of_elements = list(map(len, my_descr))
#
# print(list(zip(range(100), my_descr, len_of_elements)))