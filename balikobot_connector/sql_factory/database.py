import databases
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import logging
from conf import SETTING_CONTAINER
from conf.settings_wrapper import SettingsWrapper
# -------- logging setting
if not SETTING_CONTAINER:
    SETTING_CONTAINER = SettingsWrapper()
    SETTING_CONTAINER.read_data()
real_name = SETTING_CONTAINER.get_logger_name(__name__)
internal_logger = logging.getLogger(real_name)

SQLALCHEMY_DATABASE_URL = SETTING_CONTAINER.settings_local['SQLALCHEMY_DATABASE_URL']

database = databases.Database(SQLALCHEMY_DATABASE_URL)

if SETTING_CONTAINER.settings_local['SQLALCHEMY_DATABASE_TYPE'] == "SQLITE":
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL,
        connect_args={'check_same_thread': False}
    )
else:
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL,
    )
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base(bind=engine)

metadata = sqlalchemy.MetaData(
    engine,
    reflect=True,
)

try:
    shipments_async = metadata.tables["shipments"]
except:
    internal_logger.warning('Workaround...')
    shipments_async = None


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
