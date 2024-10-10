class RoiErrors(Exception):

    def __init__(self, message):
        super().__init__(message)

def get_data_from_db(company_id):

    return [company_id, f'Google {company_id}', 0.7] # Id, name, ROI


def test_check_company():

    db_data = get_data_from_db(20)

    if db_data[2] < 0.8:
        raise RoiErrors('ROI Data < 0.8')

# test_check_company()




class TooLargeValueError(Exception):
    def __init__(self, value, limit):
        self.value = value
        self.limit = limit
        message = f"Значення {value} перевищує ліміт {limit}"
        super().__init__(message)

# Приклад використання власного виключення
try:
    limit = 100
    user_input = int(input("Введіть число: "))

    if user_input > limit:
        raise TooLargeValueError(user_input, limit)
    else:
        print("Дякую! Ви ввели припустиме значення.")
except TooLargeValueError as e:
    print(f"Помилка: {e}")
except ValueError:
    print("Помилка: Будь ласка, введіть ціле число.")