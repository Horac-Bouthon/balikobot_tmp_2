from sqlalchemy.orm import Session

from . import models
from schemas import shipment as s_ship


def get_shipment(db: Session, orig_id: str):
    return db.query(models.Shipment).filter(models.Shipment.original_id == orig_id).first()


def get_shipments(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Shipment).filter(models.Shipment.is_active == True).offset(skip).limit(limit).all()


def create_shipment(db: Session, shipment: s_ship.ShipmentCreate):
    db_ship = models.Shipment(
        original_id=shipment.original_id,
        is_test=shipment.is_test,
    )
    db.add(db_ship)
    db.commit()
    db.refresh(db_ship)
    return db_ship


def update_shipment(db: Session, pack: s_ship.ShipmentCreate):
    db_obj = db.query(models.Shipment).filter(models.Shipment.original_id == pack.original_id).first()
    db_obj.state = pack.state
    db.commit()
    db.refresh(db_obj)
    return db_obj
