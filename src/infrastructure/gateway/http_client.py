from abc import ABC, abstractmethod
from typing import Any


class HttpClient(ABC):
    @abstractmethod
    async def get(self, url: str, body: dict) -> Any:
        pass    # pragma: no cover

    @abstractmethod
    async def post(self, url: str, body: dict) -> Any:
        pass    # pragma: no cover
