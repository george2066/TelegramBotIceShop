import psycopg2

conn = psycopg2.connect(
    host='localhost',
    port=5432,
    database='postgres',
    user='postgres', # Укажите имя пользователя
    password='postgres' # Укажите пароль
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE users (
    id BIGINT PRIMARY KEY,
    is_waiter BOOL NULL DEFAULT FALSE
);
""")
conn.commit()