from sqlalchemy import text, insert
from src.models import metadata_obj, WorkersOrm
from src.database import sync_engine, async_engine, session_factory, async_session_factory

def create_tables():
    sync_engine.echo = False
    metadata_obj.drop_all(sync_engine)
    metadata_obj.create_all(sync_engine)
    sync_engine.echo = True


def insert_data():
    with session_factory() as session:
        worker_bobr = WorkersOrm(username="bobr")
        worker_volk = WorkersOrm(username="volk")
        session.add_all([worker_volk, worker_bobr,])
        session.commit()


async def async_insert_data():
    async with async_session_factory() as session:
        worker_bobr = WorkersOrm(username="async_bobr")
        worker_volk = WorkersOrm(username="async_volk", id2='12345678-1234-5678-1234-567812345678')
        session.add_all([worker_volk, worker_bobr,])
        await session.commit()
