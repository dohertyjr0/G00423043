from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.database import engine, get_db
from app.models import Base, EquipmentDB
from app.schemas import EquipmentCreate, EquipmentRead

Base.metadata.create_all(bind = engine)
app = FastAPI(title="equipment")

@app.get("/health")
def health():
    return{"status": "ok"}

@app.post("/requests/equipment", response_model = EquipmentRead, status_code = status.HTTP_201_CREATED)
def add_equipment(new_equipment: EquipmentCreate, db: Session = Depends(get_db)):
    db_equipment = EquipmentDB(**new_equipment.model_dump())
    db.add(db_equipment)

    #validated
    try:
        db.commit()
        db.refresh(db_equipment)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            409,
            "Equipment already exists"
        )
    return db_equipment

@app.get("/requests/equipment", response_model = list[EquipmentRead])
def get_all_equipment(db: Session = Depends(get_db)):
    query = select(EquipmentDB).order_by(EquipmentDB.id)
    if EquipmentDB is None:
        return []
    return db.execute(query).scalars().all()

@app.get("/requests/equipment/priority/{priority}")
def get_priority(priority: int, db: Session = Depends(get_db)):
    db_equipment = db.get(EquipmentDB, priority)
    query = select(EquipmentDB).order_by(EquipmentDB.priority)
    if db_equipment is True:
        return EquipmentDB.priority
    elif db_equipment is None:
        return []
    return db.execute(query).scalars().all()








