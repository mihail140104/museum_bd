# ----------------------------------------
# Тестируем наши функции для вывода данных
# ----------------------------------------
from db import engine
from sqlmodel import Session
import crud

def main():
    with Session(engine) as session:
        print("\n=== Список музеев и работающих в них работников ===")
        grouped = crud.employees_grouped_by_location(session)
        for loc, emps in grouped.items():
            print(f"{loc}: {[e.full_name for e in emps]}")

        print("=== Информация о музеях ===")
        museums = crud.list_museums(session)
        for m in museums:
            print(f"{m.id}: {m.name} ({m.city}, {m.address})")

        print("\n=== Коллекции в музее с id=1 (1 Российский музей)===")
        collections = crud.collections_by_museum(session, 1)
        for c in collections:
            print(f"{c.id}: {c.name} (location_id={c.location_id})")

        print("\n=== Список работников и их рабочих мест ===")
        emps = crud.employees_with_locations(session)
        for e in emps:
            print(f"{e['employee_id']}: {e['full_name']} — {e['location_name']} (id={e['location_id']})")

if __name__ == "__main__":
    main()
