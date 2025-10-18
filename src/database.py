from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import URL, create_engine, text
from src.config import settings

import asyncio

sync_engine = create_engine(
    url=settings.DATABASE_URL_psycopg,
    echo=True,
    # pool_size=5,
    # max_overflow=10
)
async_engine = create_async_engine(
    url=settings.DATABASE_URL_asyncpg
)


async def basic_select_sync():
    with sync_engine.connect() as conn:
        # res = conn.execute(text("SELECT VERSION()"))
        res = conn.execute(text("select 1,2,3 union select 4,5,6"))
        print(f"{res.all()=}")
        print(f"{type(res.all())=}")


async def basic_select_async():
    print(settings, settings.DB_NAME, type(settings))
    async with async_engine.connect() as conn:
        res = await conn.execute(text("select 11,12,13 union select 34,35,36"))
        print(f"{res.all()=}")


if __name__ == "__main__":
    asyncio.run(basic_select_async())
