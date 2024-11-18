# yield

import time

def do_some_stuf(counter):
    for _ in range(counter):
        print('Sending request to server....')
        time.sleep(2)  #  чекати 2 секунди
        print('end')

        yield 'request was successfull'



get_obj = do_some_stuf(5)

print('starting...')

# for user_result in do_some_stuf(3):
#     print(user_result)


all_kvadrats = (k**2 for k in range(10))

all_kvadrats_list = [k**2 for k in range(10)]

print(all_kvadrats)
for k in all_kvadrats:
    print(k)