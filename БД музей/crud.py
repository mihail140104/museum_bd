# --------------------------
# Функции для выборки данных
# --------------------------
from sqlmodel import Session, select
import models
from typing import List, Dict

# Возвращаем список музеев с работающими в них сотрудниками
def employees_grouped_by_location(session: Session) -> Dict[str, List[models.Employee]]:
    stmt = select(models.Employee).order_by(models.Employee.id)
    employees = session.exec(stmt).all()
    result = {}
    for e in employees:
        loc_name = e.location.name if e.location else None
        result.setdefault(loc_name, []).append(e)
    return result

# Функция, возвращающая все музеи
def list_museums(session: Session) -> List[models.Location]:
    statement = select(models.Location).order_by(models.Location.id)
    return session.exec(statement).all()

# Функция, возвращающая коллекции для конкретного музея
def collections_by_museum(session: Session, location_id: int) -> List[models.Collection]:
    statement = select(models.Collection).where(models.Collection.location_id == location_id).order_by(models.Collection.id)
    return session.exec(statement).all()

# Функция, возвращающая список сотрудников с информацией о локации.
def employees_with_locations(session: Session) -> List[Dict]:
    statement = select(models.Employee)
    employees = session.exec(statement).all()
    out = []
    for e in employees:
        loc = e.location
        out.append({
            "employee_id": e.id,
            "full_name": e.full_name,
            "location_id": loc.id if loc else None,
            "location_name": loc.name if loc else None
        })
    return out

# === Для API  === #

# Локации (музеи)
def get_locations(session):
    return session.exec(select(models.Location)).all()

# Коллекции
def get_collections(session):
    return session.exec(select(models.Collection)).all()

# Сотрудники
def get_employees(session):
    return session.exec(select(models.Employee)).all()

# Экспонаты
def get_exhibits(session):
    return session.exec(select(models.Exhibit)).all()

# Временные выставки
def get_temporary_exhibitions(session):
    return session.exec(select(models.TemporaryExhibition)).all()

# Виды билетов
def get_ticket_types(session):
    return session.exec(select(models.TicketType)).all()

# Билеты
def get_tickets(session):
    return session.exec(select(models.Ticket)).all()