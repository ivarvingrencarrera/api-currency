from src.domain.entity.currency import Currency
from src.domain.entity.exchange_rate import ExchangeRate


class CurrencyConverterService:
    @staticmethod
    def convert(exchange_rate: ExchangeRate, value: float) -> float:
        if value <= 0:
            raise ValueError('value must be greater than zero')
        return round(value / exchange_rate.rate, 2)

    @staticmethod
    def format_currency(value: float, currency: Currency) -> str:
        integer_value, decimal_value = divmod(value, 1)
        integer_formatted = f'{integer_value:,.0f}'.replace(',', '.')
        decimal_formatted = f'{int(min(decimal_value, 0.99) * 100):02d}'
        return f'{currency.symbol}{integer_formatted},{decimal_formatted}'
