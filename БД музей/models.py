# -------------
# Список таблиц
# -------------
from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship

# Таблица с локациями
class Location(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    storage_conditions: Optional[str] = None
    city: Optional[str] = None
    address: Optional[str] = None
    country: Optional[str] = None

    collections: List["Collection"] = Relationship(back_populates="location")
    exhibits: List["Exhibit"] = Relationship(back_populates="location")
    employees: List["Employee"] = Relationship(back_populates="location")

# Таблица с сотрудниками
class Employee(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    full_name: str
    location_id: Optional[int] = Field(default=None, foreign_key="location.id")

    location: Optional[Location] = Relationship(back_populates="employees")
    collections: List["Collection"] = Relationship(back_populates="responsible")

# Таблица с коллекциями
class Collection(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    location_id: Optional[int] = Field(default=None, foreign_key="location.id")
    name: str
    responsible_id: Optional[int] = Field(default=None, foreign_key="employee.id")

    location: Optional[Location] = Relationship(back_populates="collections")
    responsible: Optional[Employee] = Relationship(back_populates="collections")
    exhibits: List["Exhibit"] = Relationship(back_populates="collection")

# Таблица с временными выставками
class TemporaryExhibition(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    city: Optional[str] = None
    address: Optional[str] = None
    country: Optional[str] = None

    exhibits: List["Exhibit"] = Relationship(back_populates="temporary_exhibition")

# Таблица с экспонатами
class Exhibit(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    collection_id: Optional[int] = Field(default=None, foreign_key="collection.id")
    location_id: Optional[int] = Field(default=None, foreign_key="location.id")
    temporary_exhibition_id: Optional[int] = Field(default=None, foreign_key="temporaryexhibition.id")
    storage_conditions: Optional[str] = None


    collection: Optional[Collection] = Relationship(back_populates="exhibits")
    location: Optional[Location] = Relationship(back_populates="exhibits")
    temporary_exhibition: Optional[TemporaryExhibition] = Relationship(back_populates="exhibits")

# Таблица с временными выставками
class TicketType(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    price: float

    tickets: List["Ticket"] = Relationship(back_populates="ticket_type")

# Таблица с билетами
class Ticket(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    location_id: Optional[int] = Field(default=None, foreign_key="location.id")
    ticket_type_id: Optional[int] = Field(default=None, foreign_key="tickettype.id")
    buyer_full_name: str
    visit_date: Optional[str] = None
    visit_time: Optional[str] = None

    location: Optional[Location] = Relationship()
    ticket_type: Optional[TicketType] = Relationship(back_populates="tickets")

