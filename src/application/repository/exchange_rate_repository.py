from abc import abstractmethod
from datetime import datetime

from src.domain.entity.exchange_rate import ExchangeRate


class ExchangeRateRepository:
    @abstractmethod
    async def find(self, currency_from_id: int, currency_to_id: int, date: datetime) -> ExchangeRate:
        pass   # pragma: no cover
