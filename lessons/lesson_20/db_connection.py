import psycopg2

# Параметри підключення
# База даних повинна існувати на зазначеному хості, та юзер повинен мати право на читання цього запису
dbname = 'new_db'
user = 'den'
password = 'den'
host = '127.0.0.1'
port = '5432'

# Спроба підключитись до бази даних
try:
    connection = None
    connection = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port
    )
    print("Connected to the database successfully!")

    # Для виконання запитів ви можете створити курсор
    cursor = connection.cursor()

    # Для виконання SQL запитів ви можете викликати метод execute() курсора
    # Тут можна виконати будь який запит на мові SQL, і він виконається в БД
    cursor.execute("SELECT version();")

    # Отримання результатів запиту
    record = cursor.fetchall()
    print("You are connected to - ", record)

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)

finally:
    # Закриваємо підключення
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")