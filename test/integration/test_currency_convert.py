from datetime import datetime

import pytest

from src.application.repository.currency_repository import CurrencyRepository
from src.application.repository.exchange_rate_repository import ExchangeRateRepository
from src.application.use_case.convert_currency import ConvertCurrency, Input, Output
from src.domain.entity.currency import Currency
from src.domain.entity.exchange_rate import ExchangeRate


@pytest.fixture
def currency_repository() -> CurrencyRepository:
    class CurrencyRepositoryMock(CurrencyRepository):
        def get_currency_by_code(self, code: str) -> Currency:
            if code == 'USD':
                return Currency(1, 'USD', 840, 'US Dollar', '$')
            if code == 'BRL':
                return Currency(2, 'BRL', 986, 'Brazilian Real', 'R$')
            if code == 'EUR':
                return Currency(3, 'EUR', 978, 'Euro', '€')
            if code == 'INR':
                return Currency(4, 'INR', 356, 'Indian Rupee', '₹')
            raise ValueError(f'Currency with code {code} not found')

    return CurrencyRepositoryMock()


@pytest.fixture
def exchange_rate_repository() -> ExchangeRateRepository:
    class ExchangeRateRepositoryMock(ExchangeRateRepository):
        def get_rate(self, from_currency_id: int, to_currency_id: int, date: str) -> ExchangeRate:
            if from_currency_id == 2:
                if to_currency_id == 1:
                    return ExchangeRate(5687, 2, 1, datetime.now(), 5.395398554413112)
                if to_currency_id == 3:
                    return ExchangeRate(5688, 2, 3, datetime.now(), 6.365481623828969)
                if to_currency_id == 4:
                    return ExchangeRate(5689, 2, 4, datetime.now(), 0.0724135905111813)
            raise ValueError('No exchange rate found for the given currencies.')

    return ExchangeRateRepositoryMock()


def test_must_convert_currency_brl_to_usd(
    currency_repository: CurrencyRepository, exchange_rate_repository: ExchangeRateRepository
) -> None:
    input_ = Input(
        from_currency='BRL',
        to_currency='USD',
        amount=529.99,
        date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    )
    currency_convert = ConvertCurrency(currency_repository, exchange_rate_repository)
    output = currency_convert.execute(input_)
    output_expected = Output(amount=98.23, currency_symbol='$', formatted_amount='$98,23')
    assert output == output_expected