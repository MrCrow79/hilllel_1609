import os

def is_dev():
    # cur_env = os.getenv('CURRENT_ENV')  # поверен знаечення з системи, або None якщо в системі нема CURRENT_ENV
    #
    # if cur_env ==  'DEV':
    #     return True
    # else:
    #     return False
    return os.getenv('CURRENT_ENV') == 'DEV'   # True if CURRENT_ENV == dev else False

