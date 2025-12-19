# ---------------
# Создаем таблицы
# ---------------
from db import engine
from sqlmodel import SQLModel
import models

def init_tables():
    SQLModel.metadata.create_all(engine)
    print("Tables created (if not exist)")

if __name__ == '__main__':
    init_tables()