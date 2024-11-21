# Параметризований декоратор для встановлення максимальної кількості повторних спроб


def retry(max_retries, type_of_error):
    def decorator(func):
        def wrapper(*args, **kwargs):
            retries = 0
            while retries < max_retries:
                try:
                    # Спроба виклику функції, яку декоруємо
                    return func(*args, **kwargs)
                except type_of_error as e:
                    # Обробка помилки та вивід повідомлення про спробу
                    print(f"Помилка: {e}. Повторна спроба {retries + 1}/{max_retries}")
                    retries += 1
            # Викидаємо виняток, якщо досягнуто максимальну кількість спроб
            raise Exception("Досягнуто максимальну кількість спроб")
        return wrapper
    return decorator



# Параметризоване застосування декоратора
@retry(max_retries=3, type_of_error=ConnectionError)
def connect_to_server():
    # Спроба з'єднатися з сервером
    raise ConnectionError("Не вдалося підключитися до сервера")

# Параметризоване застосування декоратора
@retry(max_retries=3, type_of_error=AssertionError)
def connect_to_server2():
    # Спроба з'єднатися з сервером
    raise ConnectionError("Не вдалося підключитися до сервера. Second try")

# Виклик функції
connect_to_server2()
connect_to_server()