from typing import Any

from src.application.repository.currency_repository import CurrencyRepository
from src.domain.entity.currency import Currency


class CurrencyRepositoryDatabase(CurrencyRepository):
    def __init__(self, database: Any) -> None:
        self.database = database

    def get_currency_by_code(self, code: str) -> Currency:
        currency = self.database.get_currency_by_code(code)
        return Currency(**currency)
