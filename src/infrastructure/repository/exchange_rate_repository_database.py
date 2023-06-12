from typing import Any

from src.application.repository.exchange_rate_repository import ExchangeRateRepository
from src.domain.entity.exchange_rate import ExchangeRate


class ExchangeRateRepositoryDatabase(ExchangeRateRepository):
    def __init__(self, database: Any) -> None:
        self.database = database

    def get_rate(self, from_currency_id: int, to_currency_id: int, date: str) -> ExchangeRate:
        return self.database.get_exchange_rate(from_currency_id, to_currency_id, date)
