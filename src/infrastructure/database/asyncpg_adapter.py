from collections import namedtuple
from typing import Any

import asyncpg

from src.config import DATABASE_URL
from src.infrastructure.database.connection import Connection


class AsyncPGAdapter(Connection):
    def __init__(self) -> None:
        self.connection: asyncpg = None

    async def connect(self) -> None:
        self.connection = await asyncpg.connect(DATABASE_URL)

    async def disconnect(self) -> None:
        await self.connection.close()

    async def insert(self, query: str, *params: str) -> None:
        await self.connect()
        try:
            await self.connection.execute(query, *params)
        finally:
            await self.disconnect()

    async def select(self, query: str, *params: Any) -> list:
        await self.connect()
        result = await self.connection.fetch(query, *params)
        if result == []:
            return []
        column_names = result[0].keys()
        NamedTuple = namedtuple('NamedTuple', column_names)   # type: ignore
        await self.disconnect()
        return [NamedTuple(*row.values()) for row in result]
