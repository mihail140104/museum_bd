# -------------------------------------------------------------
# Определяем REST API для создания и получения экспонатов музея
# -------------------------------------------------------------
from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import Session
import models
import crud
from db import get_session

app = FastAPI(title="Museum API")

# LOCATIONS (Музеи / локации)
@app.get("/locations", response_model=list[models.Location])
def get_locations(session: Session = Depends(get_session)):
    return crud.get_locations(session)

# COLLECTIONS (Коллекции)
@app.get("/collections", response_model=list[models.Collection])
def get_collections(session: Session = Depends(get_session)):
    return crud.get_collections(session)

# EMPLOYEES (Сотрудники)
@app.get("/employees", response_model=list[models.Employee])
def get_employees(session: Session = Depends(get_session)):
    return crud.get_employees(session)

# EXHIBITS (Экспонаты)
@app.get("/exhibits", response_model=list[models.Exhibit])
def get_exhibits(limit: int = 100, session: Session = Depends(get_session)):
    return crud.get_exhibits(session)

# TEMPORARY EXHIBITIONS (Временные выставки)
@app.get("/temporary-exhibitions", response_model=list[models.TemporaryExhibition])
def get_temp_exhibitions(session: Session = Depends(get_session)):
    return crud.get_temporary_exhibitions(session)

# TICKET TYPES (Виды билетов)
@app.get("/ticket-types", response_model=list[models.TicketType])
def get_ticket_types(session: Session = Depends(get_session)):
    return crud.get_ticket_types(session)

# TICKETS (Билеты)
@app.get("/tickets", response_model=list[models.Ticket])
def get_tickets(session: Session = Depends(get_session)):
    return crud.get_tickets(session)