from typing import List

from pydantic import BaseModel


class ShipmentBase(BaseModel):
    original_id: str


class ShipmentCreate(ShipmentBase):
    is_test: bool = True


class Shipment(ShipmentBase):
    id: int
    is_active: bool
    state: str
    is_test: bool

    class Config:
        orm_mode = True


class ShipmentClose(ShipmentBase):
    pass
