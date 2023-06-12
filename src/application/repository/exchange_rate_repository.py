from abc import abstractmethod

from src.domain.entity.exchange_rate import ExchangeRate


class ExchangeRateRepository:
    @abstractmethod
    def get_rate(self, from_currency_id: int, to_currency_id: int, date: str) -> ExchangeRate:
        pass # pragma: no cover
