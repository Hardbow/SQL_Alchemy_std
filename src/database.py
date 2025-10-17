from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import URL, create_engine, text
from src.config import settings

import asyncio

print(settings, settings.DB_NAME, type(settings))

engine = create_engine(
    url=settings.DATABASE_URL_psycopg,
    # echo=True,
    # pool_size=5,
    # max_overflow=10
)
async_engine = create_async_engine(
    url=settings.DATABASE_URL_asyncpg
)

with engine.connect() as conn:
    # res = conn.execute(text("SELECT VERSION()"))
    res = conn.execute(text("select 1,2,3 union select 4,5,6"))
    print(f"{res.all()=}")
    print(f"{type(res.all())=}")

async def my_query():
    async with async_engine.connect() as conn:
        res = await conn.execute(text("select 11,12,13 union select 34,35,36"))
        print(f"{res.all()=}")

asyncio.run(my_query())