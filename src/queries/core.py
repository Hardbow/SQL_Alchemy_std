from sqlalchemy import text
from src.models import metadata_obj
from src.database import async_engine, sync_engine

import asyncio

async def basic_select_async():
    async with async_engine.connect() as conn:
        res = await conn.execute(text("select 11,12,13 union select 34,35,36"))
        print(f"{res.all()=}")


def create_tables():
    metadata_obj.create_all()

if __name__ == "__main__":
    asyncio.run(basic_select_async())