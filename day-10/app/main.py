from fastapi import FastAPI
from routers.asset_router import router
from database.database import create_table, drop_table

create_table()
app = FastAPI()

app.include_router(router)