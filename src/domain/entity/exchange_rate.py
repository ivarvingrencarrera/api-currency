from datetime import date, datetime


class ExchangeRate:
    def __init__(self, id: int, currency_from_id: int, currency_to_id: int, date: datetime, rate: float):
        self.validate_rate(rate)
        self.validate_date(date)
        self.id = id
        self.currency_from = currency_from_id
        self.currency_to = currency_to_id
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
