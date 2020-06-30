from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# from elentos_balikobot.views import add
# from elentos_balikobot.sql_app import models
# from elentos_balikobot.sql_app.database import engine, database

app = FastAPI()


# app.include_router(
#     add.router,
# )

#models.Base.metadata.create_all()

app.mount("/static", StaticFiles(directory="./balikobot_connector/static"), name="static")
template = Jinja2Templates(directory="./balikobot_connector/templates")

"""
@app.on_event("startup")
async def startup():
    await database.connect()
    return


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
    return
"""
