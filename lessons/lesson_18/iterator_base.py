
#iter()
#next()

list_of_number1 = [11,12,13,14,15]
list_of_number2 = [21,22,23,24,25]

# for el in list_of_number:
#     print(el)

iter_obj = iter(list_of_number1)
iter_obj2 = iter(list_of_number2)

# print(next(iter_obj))  # 0
# print(next(iter_obj))  # 1
# print(next(iter_obj))  # 2
# print(next(iter_obj2))  # 0  # iter_obj2.__next__()
# print(next(iter_obj2))  # 1
# print(next(iter_obj2))  # 2
# print(next(iter_obj))  # 3
# print(next(iter_obj2))  # 3
# print(next(iter_obj))  # 4
# print(next(iter_obj2))  # 4

# try:
#     while True:
#         print(next(iter_obj))
# except StopIteration:
#     pass