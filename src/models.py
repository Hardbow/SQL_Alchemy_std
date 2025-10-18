from sqlalchemy import Table, Column, Integer, String, UUID, MetaData

metadata_obj = MetaData()
print(metadata_obj)

worker_table = Table(
    "workers",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("id2", UUID),
    Column("username", String)
)

print(metadata_obj.info)