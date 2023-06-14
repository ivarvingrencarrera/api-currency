import unittest
from datetime import datetime

from parameterized import parameterized

from src.domain.entity.currency import Currency
from src.domain.entity.exchange_rate import ExchangeRate
from src.domain.service.currency_converter_service import CurrencyConverterService


class CurrencyConverterServiceTests(unittest.TestCase):
    def setUp(self) -> None:
        self.currency_from = Currency(1, 'BRL', 986, 'Brazilian Real', 'R$')
        self.currency_to = Currency(2, 'EUR', 978, 'Euro', '€')
        self.exchange_rate = ExchangeRate(
            5687, self.currency_from.id, self.currency_to.id, datetime.now(), 4.76
        )

    @parameterized.expand([(100, 21.01), (200, 42.02)])
    def test_must_converter_the_value(self, input_: float, expected_output: float) -> None:
        output = CurrencyConverterService.convert(self.exchange_rate, input_)
        self.assertEqual(output, expected_output)

    @parameterized.expand([(-100), (0)])
    def test_must_not_converter_the_value_with_negative_or_zero_value(self, input_: float) -> None:
        with self.assertRaises(ValueError) as context:
            CurrencyConverterService.convert(self.exchange_rate, input_)
        self.assertEqual('value must be greater than zero', str(context.exception))

    @parameterized.expand(
        [
            (0.59, Currency(4, 'USD', 840, 'US Dollar', '$'), '$0,59'),
            (0.63, Currency(4, 'USD', 840, 'US Dollar', '$'), '$0,63'),
            (1.30, Currency(4, 'USD', 840, 'US Dollar', '$'), '$1,30'),
            (10.00, Currency(2, 'EUR', 978, 'Euro', '€'), '€10,00'),
            (100.00, Currency(2, 'EUR', 978, 'Euro', '€'), '€100,00'),
            (2000.00, Currency(3, 'INR', 356, 'Indian Rupee', '₹'), '₹2.000,00'),
            (200000.00, Currency(3, 'INR', 356, 'Indian Rupee', '₹'), '₹200.000,00'),
            (2000000.00, Currency(3, 'INR', 356, 'Indian Rupee', '₹'), '₹2.000.000,00'),
        ]
    )
    def test_must_format_the_value(self, value: float, currency: Currency, expected_output: str) -> None:
        output = CurrencyConverterService.format_currency(value, currency)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main()
