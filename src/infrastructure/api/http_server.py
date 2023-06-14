from abc import ABC, abstractmethod
from collections.abc import Callable


class HttpServer(ABC):
    @abstractmethod
    def on(self, method: str, url: str, callback: Callable) -> None:
        pass    # pragma: no cover

    @abstractmethod
    def listen(self, port: int) -> None:
        pass    # pragma: no cover
