# --------------
# Очистка таблиц
# --------------
from sqlmodel import SQLModel
from db import engine

print("Dropping all tables...")
SQLModel.metadata.drop_all(engine)
print("Creating all tables...")
SQLModel.metadata.create_all(engine)
print("Done.")
