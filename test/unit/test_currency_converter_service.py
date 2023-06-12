import unittest
from datetime import datetime

from parameterized import parameterized

from src.domain.entity.currency import Currency
from src.domain.entity.exchange_rate import ExchangeRate
from src.domain.service.currency_converter_service import CurrencyConverterService


class CurrencyConverterServiceTests(unittest.TestCase):
    def setUp(self) -> None:
        self.from_currency = Currency(1, 'BRL', 986, 'Brazilian Real', 'R$')
        self.to_currency = Currency(2, 'EUR', 978, 'Euro', '€')
        self.exchange_rate = ExchangeRate(5687, self.from_currency.id, self.to_currency.id, datetime.now(), 4.76)

    @parameterized.expand([(100, 21.01), (200, 42.02)])
    def test_must_converter_the_amount(self, input_: float, expected_output: float) -> None:
        output = CurrencyConverterService.convert(self.exchange_rate, self.from_currency, self.to_currency, input_)
        self.assertEqual(output, expected_output)

    @parameterized.expand([(-100), (0)])
    def test_must_not_converter_the_amount_with_negative_or_zero_amount(self, input_: float) -> None:
        with self.assertRaises(ValueError) as context:
            CurrencyConverterService.convert(self.exchange_rate, self.from_currency, self.to_currency, input_)
        self.assertEqual('Amount must be greater than zero', str(context.exception))

if __name__ == '__main__':
    unittest.main()
