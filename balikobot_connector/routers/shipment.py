from typing import List
from fastapi import APIRouter, HTTPException, Depends
from balikobot_connector import LOGGER_MAIN_NAME

import logging

real_name = LOGGER_MAIN_NAME + '.' +__name__
# -------- logging setting
internal_logger = logging.getLogger(real_name)


router = APIRouter()


@router.get("/shipments")
def active_shipments(
):
    """ displays all active shipments """
    internal_logger.debug('connect active_shipments')
    return {'message': 'active shipments list'}


@router.post("/shipments")
def create_shipments(
):
    """ add or update shipment """
    internal_logger.debug('connect create_shipments')
    return {'message': 'add new shipment'}
