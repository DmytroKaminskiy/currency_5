from typing import List

from fastapi import Depends, FastAPI, Request, HTTPException
from models import zoom_event_table
from schemas import ZoomEventCreate, ZoomEventRead

from os import environ

import databases

# берем параметры БД из переменных окружения
DB_USER = environ["DB_USER"]
DB_PASS = environ["DB_PASS"]
DB_HOST = environ["DB_HOST"]
DB_NAME = environ["DB_NAME"]
DB_PORT = environ.get("DB_PORT", "5432")
ZOOM_WEBHOOK_AUTHORIZATION_KEY = environ['ZOOM_WEBHOOK_AUTHORIZATION_KEY']

SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)
# создаем объект database, который будет использоваться для выполнения запросов
database = databases.Database(SQLALCHEMY_DATABASE_URL)


app = FastAPI()


@app.on_event("startup")
async def startup():
    # когда приложение запускается устанавливаем соединение с БД
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    # когда приложение останавливается разрываем соединение с БД
    await database.disconnect()


@app.get("/")
async def index_get():
    return {"message": "Hello World GET"}


@app.post("/zoom/webhook/")
async def zoom_webhook(
        zoom_event_data: ZoomEventCreate,
        request: Request,
):
    if request.headers['authorization'] != ZOOM_WEBHOOK_AUTHORIZATION_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")

    query = zoom_event_table.insert().values(zoom_event_data.dict())
    event_id = await database.execute(query)
    return {"event_id": event_id}


@app.get("/zoom/webhook/")
async def zoom_webhook_list(
        response_model=List[ZoomEventRead],
):
    # изменим роут таким образом, чтобы он брал данные из БД
    query = zoom_event_table.select()
    return await database.fetch_all(query)
