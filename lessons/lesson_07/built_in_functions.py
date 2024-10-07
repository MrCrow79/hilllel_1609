# print(all([True, True, False]))
# print(all([True, True]))


def is_even(number):
    return number % 2 == 0  # True or False

# print(is_even(5))
# print(is_even(10))

result = [is_even(num) for num in [2,4,6]]

result_2 = []
for num in [2,4,7]:
    loc_res = is_even(num)  # loc_res = True або loc_res = number % 2 == 0
    result_2.append(loc_res)

# print(result)
# print(result_2)
#
# print(all(result))
# print(all(result_2))

# print(all([1,2,3]))  # => all([bool(1), bool(2), bool(3)]) => True
# print(all([0,2,3]))  # => all([bool(0), bool(2), bool(3)]) => False , бо bool(0) це False

# ----
# print(any([0,0,False, '']))
#
# # ------
# for k in enumerate(['den', 'alex']):
#     print(k)
# # -------
# for k in enumerate(['den', 'alex'], start=15):
#     print(k)
# # -------
# for ind, name in enumerate(['den', 'alex'], start=0):
#     print(f'Name {name} has index {ind}')

# filter

my_descr = 'My   name  is   Den  '.split(' ')  # => list

print(my_descr)

print([k for k in my_descr if len(k)])  # прибере всі порожні строки

res = []

for k in my_descr:
    if len(k): # ==> if len(k) is True
        res.append(k)
print(res)

print(filter(len, my_descr))
print(list(filter(len, my_descr)))

# print([num for num in range(20) if is_even(num)])  # всі парні з 0 до 19
#
# print(list(filter(is_even, range(20))))


