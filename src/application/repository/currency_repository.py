from abc import abstractmethod

from src.domain.entity.currency import Currency


class CurrencyRepository:
    @abstractmethod
    def get_currency_by_code(self, code: str) -> Currency:
        pass # pragma: no cover
