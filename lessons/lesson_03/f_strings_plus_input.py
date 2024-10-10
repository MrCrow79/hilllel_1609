# alex_name = 'ALex'
# sofa_name = 'Sofa'
#
# number = 10
# age = 27
# was_in_uni = 5
#
# # if number == 10:
# #     print('The winner is ' + alex_name)
# #     print('The winner is', alex_name)
# #     print(f'The winner is {alex_name}')  # f-string
#
#
# my_text = f'My name is {sofa_name}\nmy age is {age}.\nI\'m working since {18 + was_in_uni} years'
#
# age = 50
# print(age)
# print(my_text)

# input()

user_age = 23

final_text_asd = (f'Your biography: \nI\'m'
              f'my age is {user_age}. I was born in {2024 - user_age}')

if __name__ == '__main__':

    user_age = int(input('Tell me your age: ')) # it is string

    final_text = (f'Your biography: \nI\'m {input("Tell me your name: ")}, '
                  f'my age is {user_age}. I was born in {2024 - user_age}')

    print(final_text)
