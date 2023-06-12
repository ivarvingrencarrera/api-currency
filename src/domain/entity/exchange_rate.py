from datetime import datetime


class ExchangeRate:
    def __init__(self, id: int, from_currency_id: int, to_currency_id: int, date: datetime, rate: float):
        self.validate_rate(rate)
        self.id = id
        self.from_currency = from_currency_id
        self.to_currency = to_currency_id
        self.date = date
        self.rate = rate

    @staticmethod
    def validate_rate(rate: float) -> None:
        if rate < 0:
            raise ValueError('Rate must not be negative')
