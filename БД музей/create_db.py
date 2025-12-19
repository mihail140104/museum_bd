# -------------------
# Создаем базу данных
# -------------------
from dotenv import load_dotenv
import os
import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

load_dotenv()

# Параметры для подключения
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "museumdb")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASS = os.getenv("DB_PASS", "12345")

# Функция создания БД
def create_database(dbname: str):
    conn = psycopg2.connect(dbname='postgres', user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()
    try:
        cur.execute(sql.SQL('CREATE DATABASE {}').format(sql.Identifier(dbname)))
        print(f"Database '{dbname}' created")
    except psycopg2.errors.DuplicateDatabase:
        print(f"Database '{dbname}' already exists")
    finally:
        cur.close()
        conn.close()

if __name__ == '__main__':
    create_database(DB_NAME)

