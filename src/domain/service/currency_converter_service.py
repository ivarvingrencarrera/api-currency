from src.domain.entity.currency import Currency
from src.domain.entity.exchange_rate import ExchangeRate


class CurrencyConverterService:
    @staticmethod
    def convert(exchange_rate: ExchangeRate, amount: float) -> float:
        if amount <= 0:
            raise ValueError('Amount must be greater than zero')
        return round(amount / exchange_rate.rate, 2)

    @staticmethod
    def format_currency(amount: float, currency: Currency) -> str:
        integer_value, decimal_value = divmod(amount, 1)
        integer_formatted = f'{integer_value:,.0f}'.replace(',', '.')
        decimal_formatted = f'{int(min(decimal_value, 0.99) * 100):02d}'
        return f'{currency.symbol}{integer_formatted},{decimal_formatted}'
