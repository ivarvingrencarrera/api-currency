from datetime import datetime

import pytest

from src.application.use_case.convert_currency import ConvertCurrency, Input, Output
from src.infrastructure.database.asyncpg_adapter import AsyncPGAdapter
from src.infrastructure.repository.currency_repository_database import CurrencyRepositoryDatabase
from src.infrastructure.repository.exchange_rate_repository_database import ExchangeRateRepositoryDatabase

connection = AsyncPGAdapter()
currency_repository = CurrencyRepositoryDatabase(connection)
exchange_rate_repository = ExchangeRateRepositoryDatabase(connection)


async def test_must_convert_currency_brl_to_usd() -> None:
    input_ = Input(
        from_currency='BRL',
        to_currency='USD',
        amount=529.99,
        date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    )
    currency_convert = ConvertCurrency(currency_repository, exchange_rate_repository)
    output = await currency_convert.execute(input_)
    output_expected = Output(amount=98.23, currency_symbol='$', formatted_amount='$98,23')
    assert output == output_expected


async def test_must_convert_currency_brl_to_eur() -> None:
    input_ = Input(
        from_currency='BRL',
        to_currency='EUR',
        amount=529.99,
        date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    )
    currency_convert = ConvertCurrency(currency_repository, exchange_rate_repository)
    output: Output = await currency_convert.execute(input_)
    assert output.currency_symbol == '€'
    assert output.formatted_amount == '€83,26'
    assert output.amount == 83.26


async def test_must_convert_currency_brl_to_inr() -> None:
    input_ = Input(
        from_currency='BRL',
        to_currency='INR',
        amount=529.99,
        date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    )
    currency_convert = ConvertCurrency(currency_repository, exchange_rate_repository)
    output = await currency_convert.execute(input_)
    assert output.currency_symbol == '₹'
    assert output.formatted_amount == '₹7.318,93'
    assert output.amount == 7318.93


async def test_must_convert_currency_brl_to_brl() -> None:
    input_ = Input(
        from_currency='BRL',
        to_currency='BRL',
        amount=529.99,
        date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    )
    currency_convert = ConvertCurrency(currency_repository, exchange_rate_repository)
    output = await currency_convert.execute(input_)
    output_expected = Output(amount=529.99, currency_symbol='R$', formatted_amount='R$529,99')
    assert output == output_expected


async def test_must_not_convert_currency_brl_to_yen() -> None:
    input_ = Input(
        from_currency='BRL',
        to_currency='YEN',
        amount=529.99,
        date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    )
    currency_convert = ConvertCurrency(currency_repository, exchange_rate_repository)
    with pytest.raises(ValueError) as context:
        await currency_convert.execute(input_)
    assert 'Currency with code YEN not found' in str(context.value)


async def test_must_not_convert_currency_brl_to_usd_with_negative_amount() -> None:
    input_ = Input(
        from_currency='BRL',
        to_currency='USD',
        amount=-529.99,
        date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    )
    currency_convert = ConvertCurrency(currency_repository, exchange_rate_repository)
    with pytest.raises(ValueError) as context:
        await currency_convert.execute(input_)
    assert 'Amount must be greater than zero' in str(context.value)


async def test_must_not_convert_currency_brl_to_usd_with_priceless_amount() -> None:
    input_ = Input(
        from_currency='BRL',
        to_currency='USD',
        amount=0,
        date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    )
    currency_convert = ConvertCurrency(currency_repository, exchange_rate_repository)
    with pytest.raises(ValueError) as context:
        await currency_convert.execute(input_)
    assert 'Amount must be greater than zero' in str(context.value)

async def test_must_not_convert_currency_brl_to_usd_when_not_exist() -> None:
    input_ = Input(
        from_currency='BRL',
        to_currency='USD',
        amount=0,
        date='2023-06-09 00:00:00',
    )
    currency_convert = ConvertCurrency(currency_repository, exchange_rate_repository)
    with pytest.raises(ValueError) as context:
        await currency_convert.execute(input_)
    assert 'No exchange rate found for the given currencies.' in str(context.value)
