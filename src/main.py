import os
import sys
import asyncio
sys.path.insert(1, os.path.join(sys.path[0], '..'))

# from src.queries.core import create_tables, insert_data_imperative, insert_data_declarative
from src.queries.orm import create_tables, insert_data, async_insert_data


async def main():
    create_tables()
    await async_insert_data()
    # insert_data()

asyncio.run(main())

# insert_data_imperative()
# insert_data_declarative()