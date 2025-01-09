import psycopg2

conn = psycopg2.connect(
    dbname="test_db",
    user="test_user1",
    password="test_password",
    host="localhost",
    port="5433"
)