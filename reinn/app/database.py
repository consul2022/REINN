# Асинхронный движок

from ..config.application import settings
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = f"postgresql+asyncpg://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_HOST}/{settings.DB_NAME}"
engine = create_async_engine(DATABASE_URL, echo=True)

# Асинхронная сессия
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=AsyncSession
)

Base = declarative_base()
# Функция для получения асинхронной сессии
async def get_db():
    async with SessionLocal() as session:
        yield session