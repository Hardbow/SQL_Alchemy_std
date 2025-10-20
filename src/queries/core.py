from sqlalchemy import text, insert
from src.models import metadata_obj
from src.database import async_engine, sync_engine
from src.models import worker_table

import asyncio


async def basic_select_async():
    async with async_engine.connect() as conn:
        res = await conn.execute(text("select 11,12,13 union select 34,35,36"))
        print(f"{res.all()=}")


def create_tables():
    sync_engine.echo = False
    metadata_obj.drop_all(sync_engine)
    metadata_obj.create_all(sync_engine)
    sync_engine.echo = True


def insert_data_imperative():
    with sync_engine.connect() as conn:
        stmt = """INSERT INTO workers (username) VALUES
        ('Bobr'),
        ('Volk');"""
        conn.execute(text(stmt))
        conn.commit()


def insert_data_declarative():
    with sync_engine.connect() as conn:
        stmt = insert(worker_table).values(
            [
                {"username": "Jhon"},
                {"username": "Silver"}
            ]
        )
        conn.execute(stmt)
        conn.commit()


if __name__ == "__main__":
    asyncio.run(basic_select_async())
