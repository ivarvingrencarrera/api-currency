from abc import ABC, abstractmethod

from src.domain.entity.currency import Currency
from src.domain.entity.exchange_rate import ExchangeRate


class CurrencyConverterService(ABC):
    @abstractmethod
    def convert(exchange_rates: ExchangeRate, from_currency: Currency, to_currency: Currency, amount: float) -> float:
        if amount <= 0:
            raise ValueError('Amount must be greater than zero')
        return round(amount / exchange_rates.rate, 2)
        
