from abc import ABC, abstractmethod
from typing import Any


class Connection(ABC):
    @abstractmethod
    async def disconnect(self) -> None:
        pass

    @abstractmethod
    async def insert(self, query: str) -> None:
        pass

    @abstractmethod
    async def select(self, query: str, *params: Any) -> list:
        pass
