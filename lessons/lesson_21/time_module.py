import time

if __name__ == '__main__':
    print(time.time())  # кількість секунд з якоїсь дати
    print(time.localtime())  # віддавати об'єєкт часу

    ct = time.localtime()

    print(ct.tm_year)
    print(ct.tm_mon)
    print(ct.tm_zone)
    print(type(ct))

    print(f'now is {ct.tm_hour}:{ct.tm_min}')
    print(f'{time.localtime().tm_sec}')

    cur_time_sec = time.time()
    time.sleep(3.5)  # почекав 3.5 секунди
    print(f'Diff was {time.time() - cur_time_sec}')
    print(f'{time.localtime().tm_sec}')

    # wait 10 seconds
    cur_time_sec = time.time()
    while time.time() - cur_time_sec < 10: # поки не пройде 10 секунд
        print('Still waiting...')
        time.sleep(0.5)
