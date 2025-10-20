import uuid

from sqlalchemy import Table, Column, Integer, String, UUID, MetaData
from sqlalchemy.orm import Mapped, mapped_column
from src.database import Base


class WorkersOrm(Base):
    __tablename__ = "workers"
    id: Mapped[int] = mapped_column(primary_key=True)
    id2: Mapped[uuid.UUID] = mapped_column()
    username: Mapped[str]







metadata_obj = MetaData()


worker_table = Table(
    "workers",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("id2", UUID),
    Column("username", String)
)

print(dir(metadata_obj))
print(metadata_obj.tables)