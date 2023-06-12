from datetime import date, datetime


class ExchangeRate:
    def __init__(self, id: int, from_currency_id: int, to_currency_id: int, date: datetime, rate: float):
        self.validate_rate(rate)
        self.validate_date(date)
        self.id = id
        self.from_currency = from_currency_id
        self.to_currency = to_currency_id
        self.date = date
        self.rate = rate

    @staticmethod
    def validate_rate(rate: float) -> None:
        if rate < 0:
            raise ValueError('Rate must not be negative')

    @staticmethod
    def validate_date(date_datetime: datetime) -> None:
        if date_datetime.date() != date.today():
            raise ValueError('The date is not the current date')
