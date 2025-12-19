# --------------------------------------------
# Заполняем таблицы минимальным набором данных
# --------------------------------------------
from sqlmodel import Session
from db import engine
import models

def _maybe_none(val):
    try:
        if int(val) == 0:
            return None
    except Exception:
        pass
    return val

def seed():
    with Session(engine) as session:
        # Заполняем локации
        locations = [
            models.Location(id=1, name="1 Российский музей", storage_conditions="в помещении", city="Москва", address="ул. Ведерникова д. 22", country="Россия"),
            models.Location(id=2, name="Павловский музей", storage_conditions="в помещении", city="Москва", address="ул. Пролетарская д. 17", country="Россия"),
            models.Location(id=3, name="Зеленогорский музей", storage_conditions="на улице", city="Зеленогорск", address="ул. Радужная д. 4", country="Россия"),
        ]
        for l in locations:
            session.merge(l)

        session.flush()

        # Заполняем сотрудников
        employees = [
            models.Employee(id=1, full_name="Горбачев Сергей Матвеевич", location_id=1, collection_id=1),
            models.Employee(id=2, full_name="Кирпичева Анна Андреевна", location_id=2, collection_id=2),
            models.Employee(id=3, full_name="Илонова Ирина Игоревна", location_id=1, collection_id=3),
            models.Employee(id=4, full_name="Харламов Андрей Викторович", location_id=3, collection_id=4),
            models.Employee(id=5, full_name="Падерин Николай Дмитриевич", location_id=1, collection_id=5),
        ]
        for e in employees:
            session.merge(e)

        session.flush()

        # Заполняем коллекции
        collections = [
            models.Collection(id=1, location_id=1, name="Современное искусство", responsible_id=1),
            models.Collection(id=2, location_id=2, name="Импрессионизм", responsible_id=2),
            models.Collection(id=3, location_id=1, name="Древнее искусство", responsible_id=3),
            models.Collection(id=4, location_id=3, name="Живопись 2000-х", responsible_id=4),
            models.Collection(id=5, location_id=2, name="Картины Айвазовского", responsible_id=5),
        ]
        for c in collections:
            session.merge(c)

        # Заполняем виды билетов
        ticket_types = [
            models.TicketType(id=1, name="Без гида", price=450.0),
            models.TicketType(id=2, name="Аудиогид", price=600.0),
            models.TicketType(id=3, name="Экскурсия", price=700.0),
        ]
        for t in ticket_types:
            session.merge(t)

        # Заполняем временные выставки
        te = models.TemporaryExhibition(
            id=34,
            name="Выставка СИСВС",
            city="Санкт-Петербург",
            address="ул. Новоизмайловский проспект д. 12",
            country="Россия"
        )
        session.merge(te)

        session.flush()

        # Заполняем экспонаты
        exhibits = [
            models.Exhibit(id=1, name="Статуя №29б", collection_id=1, location_id=1, temporary_exhibition_id=_maybe_none(0), storage_conditions="нет условий"),
            models.Exhibit(id=2, name="Картина №39", collection_id=2, location_id=2, temporary_exhibition_id=_maybe_none(0), storage_conditions="только в помещении"),
            models.Exhibit(id=3, name="Статуя №301", collection_id=4, location_id=3, temporary_exhibition_id=_maybe_none(0), storage_conditions="нет условий"),
            models.Exhibit(id=4, name="Меч №12", collection_id=3, location_id=1, temporary_exhibition_id=_maybe_none(0), storage_conditions="нет условий"),
            models.Exhibit(id=5, name="Картина №239", collection_id=5, location_id=2, temporary_exhibition_id=_maybe_none(0), storage_conditions="только в помещении"),
            models.Exhibit(id=6, name="Картина №22", collection_id=1, location_id=1, temporary_exhibition_id=_maybe_none(34), storage_conditions="нет условий"),
            models.Exhibit(id=7, name="Статуя №14", collection_id=3, location_id=1, temporary_exhibition_id=_maybe_none(34), storage_conditions="нет условий"),
            models.Exhibit(id=8, name="Украшения №21", collection_id=3, location_id=1, temporary_exhibition_id=_maybe_none(0), storage_conditions="только в помещении"),
            models.Exhibit(id=9, name="Картина №88", collection_id=4, location_id=3, temporary_exhibition_id=_maybe_none(0), storage_conditions="только в помещении"),
        ]
        for ex in exhibits:
            session.merge(ex)

        # Заполняем билеты
        tickets = [
            models.Ticket(id=1, location_id=2, ticket_type_id=1, buyer_full_name="Рогачев Михаил Алексеевич", visit_date="14.02.2026", visit_time="14:00"),
            models.Ticket(id=2, location_id=1, ticket_type_id=2, buyer_full_name="Боров Игорь Андреевич", visit_date="15.02.2026", visit_time="12:00"),
            models.Ticket(id=3, location_id=1, ticket_type_id=2, buyer_full_name="Борова Анна Сергеевна", visit_date="15.02.2026", visit_time="12:00"),
            models.Ticket(id=4, location_id=2, ticket_type_id=3, buyer_full_name="Головарь Елена Викторовна", visit_date="14.02.2026", visit_time="17:00"),
            models.Ticket(id=5, location_id=3, ticket_type_id=1, buyer_full_name="Шабанова Виктория Андреевич", visit_date="16.02.2026", visit_time="12:00"),
            models.Ticket(id=6, location_id=3, ticket_type_id=3, buyer_full_name="Косов Гордей Федорович", visit_date="15.02.2026", visit_time="14:00"),
            models.Ticket(id=7, location_id=3, ticket_type_id=3, buyer_full_name="Косова Ксения Михайловна", visit_date="15.02.2026", visit_time="14:00"),
            models.Ticket(id=8, location_id=1, ticket_type_id=1, buyer_full_name="Баранов Никита Игоревич", visit_date="16.02.2026", visit_time="16:00"),
        ]
        for tk in tickets:
            session.merge(tk)

        # Сохраняем
        session.commit()
        print("seed_data завершен успешно")

if __name__ == '__main__':
    seed()