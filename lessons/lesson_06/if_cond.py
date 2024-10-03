
# my_age = 20
#
# if my_age == 20:  # True
#     print('You are 20')
#
#
# card_number = 1111222233334441
# cvv = 124
#
# if card_number == 1111222233334444 and cvv == 123:  # => if True and False: => if False:
#     print('Trx is completed')
# elif card_number != 1111222233334444:
#     print('You put wrong card number')
# elif cvv != 123:
#     print('You put wrong cvv')
# else:
#     print('Trx is canceled')


# if True:
#     print('True')

if False:  # не буде працювати
    print('False')

print(bool([]))  #  false

# false буде для
bool([])
bool(dict())
bool(tuple())
bool(set())
bool(False)
bool(0)
bool(0.0)
bool('')

# if []:
#     print('Empt list')
#
#
# response = []
# if not response:  # => if not False: => if True:
#     print('Empty response ')
#
# if not bool(response):  # => if not bool([]): => if not False: => if True:
#     print('Empty response ')

card_number = 1111222233334444
cvv = 122

need_details = False
has_money = True

# if card_number == 1111222233334444 and cvv == 123:  # => if True and False: => if False:
if card_number == 1111222233334444 and cvv == 123 and has_money:  # => if True and False: => if False:
    print('Trx is completed')

else:
    print('Trx is canceled')

    if not has_money:
        print('You have no money')

    else:
        if need_details:

            if card_number != 1111222233334444:
                print('You put wrong card number')

            if cvv != 123:
                print('You put wrong cvv')

        else:

            if card_number != 1111222233334444 or cvv != 123:
                print('smth goes wrong')

print('Done')