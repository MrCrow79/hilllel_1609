import random
import time


# декоратор який буде друкувати скільки часу виконувала функція)
def time_checker(fn):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # старе виконання функції
        result = fn(*args, **kwargs)
        end_time = time.time()
        print(f'quantity is {end_time - start_time}')

        return result

    return wrapper


@time_checker
def send_request_to_db():
    print('sending request')
    # time.sleep(sec) - буде чекати sec секунд
    # random.choice(interable) - буде обирати одне значення з interable
    time.sleep(random.choice(range(5)))  # спати від 0 до 4 секунд


@time_checker
def send_request_to_api(url, is_need_to_check_schema=False):
    print(f'sending request to {url}')
    time.sleep(random.choice(range(5)))  # спати від 0 до 4 секунд
    return 42


for _ in range(5):
    print(send_request_to_db())


for _ in range(5):
    print(send_request_to_api('google_url', is_need_to_check_schema=True))
