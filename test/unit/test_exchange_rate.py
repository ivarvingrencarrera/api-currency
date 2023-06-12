import unittest
from datetime import datetime

from src.domain.entity.exchange_rate import ExchangeRate


class ExchangeRateTests(unittest.TestCase):
    def setUp(self) -> None:
        self.id = 5687
        self.from_currency_id = 1
        self.to_currency_id = 2
        self.date = datetime.now()
        self.rate = 0.85

    def test_must_create_exchange_rate(self) -> None:
        exchange_rate = ExchangeRate(5687, 1, 2, self.date, self.rate)
        self.assertEqual(exchange_rate.rate, 0.85)


if __name__ == '__main__':
    unittest.main()
