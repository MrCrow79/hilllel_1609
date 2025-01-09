# Використовуємо офіційний образ Python версії 3.11
FROM python:3.11

RUN pip install pytest

# Копіюємо файли з локальної директорії в контейнер
COPY . /app

# Задаємо робочу директорію контейнера
WORKDIR /app

# Встановлюємо залежності для тестування
RUN pip install --no-cache-dir  -r requirements.txt

# Виконуємо команду для запуску тестів під час створення контейнера
CMD ["pytest", "tests", "-m", "prime"]

# CMD ["python", "db_python_script.py"]