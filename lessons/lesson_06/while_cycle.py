import random  # бібліотека для випадкових значень



# while bool or condition
#
# while True:  # вічний цикл
#     number = random.random()  # повертае випадоке число від 0 до 1
#
#     print(number)
#     if number > 0.5:
#         break


tries = 5

while tries > 0:
    number = random.random()
    print(number)
    if number <= 0.5:
        tries -= 1
    else:
        print('Found')
        break
print('Done')

# request_1 = None
# request_2 = None
#
# timer = 60

# request_1.send()
# while timer > 0:
#     response = request_2.get_reponse()
#     if response is None:
#         time.sleep(1)
#         timer = timer - 1
#     else:
#         break


# x = 10
# while x > 0:
#     # do stth

