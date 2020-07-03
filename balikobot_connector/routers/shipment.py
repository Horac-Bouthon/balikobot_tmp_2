from typing import List
from fastapi import APIRouter, HTTPException, Depends
from schemas.shipment import ShipmentCreate, Shipment
from sql_factory.crud import get_shipments, create_shipment, update_shipment
from sql_factory.database import database, shipments_async
from sqlalchemy import select
from sqlalchemy.orm import Session
from sql_factory.database import SessionLocal, get_db

import logging
from conf import SETTING_CONTAINER
from conf.settings_wrapper import SettingsWrapper

# -------- logging setting
if not SETTING_CONTAINER:
    SETTING_CONTAINER = SettingsWrapper()
    SETTING_CONTAINER.read_data()
real_name = SETTING_CONTAINER.get_logger_name(__name__)
internal_logger = logging.getLogger(real_name)


router = APIRouter()


@router.get("/shipments", response_model=List[Shipment])
def active_shipments(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """ displays all active shipments """
    internal_logger.debug('connect active_shipments')
    items = get_shipments(db, skip=skip, limit=limit)
    return items


@router.post("/shipments", response_model=Shipment)
def create_shipments(
    obj_pack: ShipmentCreate,
    db: Session = Depends(get_db)
):
    """ add or update shipment """
    internal_logger.debug('connect create_shipments')
    return create_shipment(db, obj_pack)


# ---- async
@router.post(
    "/shipments_async",
    response_model=Shipment,
)
async def as_add_shipment(
    new_request: ShipmentCreate,
):
    """ add or update shipment (async)"""
    query = shipments_async.insert().values(
        original_id=new_request.original_id,
        is_active=True,
        state='N',
        is_test=new_request.is_test,
    )
    last_record_id = await database.execute(query)
    result = await database.fetch_one(select([shipments_async]).where(shipments_async.c.id == last_record_id))
    return result


@router.get("/shipments_async", response_model=List[Shipment])
async def as_read_shipments():
    """ displays all active shipments """
    result = await database.fetch_all(select([shipments_async]).where(shipments_async.c.is_active == True))
    return result
