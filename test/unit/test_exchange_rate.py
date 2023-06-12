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
        exchange_rate = ExchangeRate(self.id, self.from_currency_id, self.to_currency_id, self.date, self.rate)
        self.assertEqual(exchange_rate.rate, 0.85)

    def test_must_not_create_exchange_rate_with_negative_rate(self) -> None:
        with self.assertRaises(ValueError) as context:
            ExchangeRate(self.id, self.from_currency_id, self.to_currency_id, self.date, -0.85)
            self.assertTrue('Rate must not be negative' in str(context.exception))


if __name__ == '__main__':
    unittest.main()
