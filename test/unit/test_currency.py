import unittest

from src.domain.entity.currency import Currency


class CurrencyTests(unittest.TestCase):
    def setUp(self) -> None:
        self.blr_currency = Currency(1, 'BRL', 986, 'Brazilian Real', 'R$')
        self.eur_currency = Currency(2, 'EUR', 978, 'Euro', '€')
        self.inr_currency = Currency(3, 'INR', 356, 'Indian Rupee', '₹')
        self.usd_currency = Currency(4, 'USD', 840, 'US Dollar', '$')

    def test_currency_equality(self) -> None:
        self.assertTrue(self.blr_currency == self.blr_currency)
        self.assertTrue(self.eur_currency == self.eur_currency)
        self.assertFalse(self.inr_currency == self.usd_currency)
        self.assertFalse(self.usd_currency == self.blr_currency)

    def test_currency_string_representation(self) -> None:
        self.assertEqual(str(self.blr_currency), 'BRL - Brazilian Real')

if __name__ == '__main__':
    unittest.main()
