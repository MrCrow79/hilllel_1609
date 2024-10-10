# def print_first_n_records(n: int, lst: list):
#
#     # print(lst[:n])
#
#     return lst[:n]
#
#
# print(print_first_n_records(4, ['a', 'b', 'c', 'd', 'e', 'f'])


def print_first_n_records(n: int, lst: list):
    new_lst = []
    for k in lst[:n]:
        new_lst.append(k)
        # print(k)

    # return new_lst  # виходить з функції




# print(print_first_n_records(4, ['a', 'b', 'c', 'd', 'e', 'f'])
#
#       )

k = 10

def x_plus_y(x, y):
    # global k
    k =  x + y


print(k)
print(f'New numbers is {x_plus_y(1,2)}')
print(f'New numbers is {x_plus_y(3,4)}')
print(k)

