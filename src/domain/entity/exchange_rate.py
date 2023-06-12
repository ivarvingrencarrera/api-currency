from datetime import datetime


class ExchangeRate:
    def __init__(self, id: int, from_currency_id: int, to_currency_id: int, date: datetime, rate: float):
        self.id = id
        self.from_currency = from_currency_id
        self.to_currency = to_currency_id
        self.date = date
        self.rate = rate
