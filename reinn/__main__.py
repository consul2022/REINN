import uvicorn
from fastapi import FastAPI

from reinn.app.database import Base
from reinn.app.database import engine

from reinn.app.router import root_api_router


# Асинхронная функция для создания таблиц
async def create_tables():
    async with engine.begin() as conn:
        # Используем run_sync для выполнения синхронных операций
        await conn.run_sync(Base.metadata.create_all)


# Создание экземпляра приложения FastAPI
app = FastAPI(
    title="Reinn API",
    description="API for managing reinn processes",
    version="1.0.0",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Support Team",
        "url": "https://t.me/Slava_brave",
        "email": "lysenko-vyacheslav2008@yandex.ru",
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT"
    },
    openapi_tags=[
        {
            "name": "work-experience",
            "description": "Operations with products"
        },
    ]
)

app.include_router(root_api_router)

# Включение инициализации базы данных при запуске приложения
@app.on_event("startup")
async def on_startup():
    await create_tables()


# Запуск сервера
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)
