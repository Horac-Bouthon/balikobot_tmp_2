from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.logger import logger as fastapi_logger


from conf import SETTING_CONTAINER
from conf.settings_wrapper import SettingsWrapper
SETTING_CONTAINER = SettingsWrapper()
SETTING_CONTAINER.read_data()
LOGGER_MAIN_NAME = SETTING_CONTAINER.settings_local['LOGGER_NAME']

from routers import shipment
from sql_factory import models
from sql_factory.database import engine, database

import logging
from datetime import datetime
from logger_wrapper.logger_wrapper import LoggerWrapper

# ------ logger section
lw = LoggerWrapper()
logger = logging.getLogger(LOGGER_MAIN_NAME)
logger = lw.set_logger(
    logger=logger,
    log_ex=SETTING_CONTAINER.settings_local['LOGGER_FILE'],
    verbose=False,
    log_level=SETTING_CONTAINER.settings_local['LOG_LEVEL'],
    console=False,
)
uvicorn_access_logger = logging.getLogger('uvicorn.access')
add_hnd = lw.create_tech_handler(
    log_file=SETTING_CONTAINER.settings_local['LTECH_FILE'],
    log_level=SETTING_CONTAINER.settings_local['LTECH_LEVEL'],
)
uvicorn_access_logger.addHandler(add_hnd)
fastapi_logger.addHandler(add_hnd)

if __name__ != 'main':
    fastapi_logger.setLevel(add_hnd.level)
    uvicorn_access_logger.setLevel(add_hnd.level)
else:
    fastapi_logger.setLevel(logging.DEBUG)
    uvicorn_access_logger.setLevel(logging.INFO)

logger.info("Server started at {}".format(datetime.now()))

# ---- routers section
app = FastAPI()


app.include_router(
     shipment.router,
 )

models.Base.metadata.create_all()

app.mount("/static", StaticFiles(directory="./static"), name="static")
template = Jinja2Templates(directory="./templates")


# ---- events section
@app.on_event("startup")
async def startup():
    await database.connect()
    return


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
    return
