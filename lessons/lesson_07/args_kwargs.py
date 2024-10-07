

# args, kwargs

# def sum_all_elements(num_1, num_2, num_3):
#
#     return sum([num_1, num_2, num_3])
#
#
# print(sum_all_elements(1,2,3))  # ==> print(6)


def sum_all_elements(double_arg, *numbers, ignore_num=5, **kwargs):  # всі агрументи в функції будуть представлені як numbers = (агрументів,)

    print('double_arg:', double_arg)
    print('Numbers:', numbers)  # tuple
    print('ignore_num:', ignore_num)
    print('kwargs:', kwargs)  # dict

    new_numbers = [k for k in numbers if k != ignore_num]  # викидуємо ignore_num

    for i_number in kwargs.get('additional_ignore', []):  # або list additional_ignore або порожній список
        new_numbers = [k for k in numbers if k != i_number] # викидуємо кожний з additional_ignore


    numbers_sum = sum(new_numbers)
    numbers_sum = double_arg*2 + numbers_sum


    if kwargs.get('double_all'):
        return numbers_sum * 2
    return numbers_sum


# print(sum_all_elements(1,2,3, *[4,5,6], 7,
#                        my_param=20, double_all='asd', ignore_num=7,
#                        additional_ignore=[1,2,3,4,5]))


my_params = {'ignore_num': 7, 'additional_ignore': [1,2,3,4], 'double_all': True, 'asd': 123}
#
print(sum_all_elements(1,2,3, *[4,5,6], 7,
                       my_param=20, double_all='asd', ignore_num=7,
                       additional_ignore=[1,2,3,4,5]))

print(sum_all_elements(1,2,3, *[4,5,6], 7,
                       **my_params))


# print(sum_all_elements(1,2,3, *[4,5,6], 7, ignore_num=7))


# list_of_range_numbers = list(range(124, 135)) # list

# print(sum_all_elements( *list_of_range_numbers,1,2,3, *[5,55,555], ignore_num=5))

