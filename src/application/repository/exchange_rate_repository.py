from abc import abstractmethod
from datetime import datetime

from src.domain.entity.exchange_rate import ExchangeRate


class ExchangeRateRepository:
    @abstractmethod
    async def find(self, from_currency_id: int, to_currency_id: int, date: datetime) -> ExchangeRate:
        pass   # pragma: no cover
