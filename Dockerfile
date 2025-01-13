# Використовуємо офіційний образ Python версії 3.11
FROM python:3.11

# Копіюємо файли з локальної директорії в контейнер
COPY . /app

# Задаємо робочу директорію контейнера
WORKDIR /app
RUN pip install psycopg2

CMD ["python", "db_python_script.py"]