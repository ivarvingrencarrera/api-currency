from datetime import datetime

import pytest

from src.application.use_case.convert_currency import ConvertCurrency, Input, Output
from src.infrastructure.database.asyncpg_adapter import AsyncPGAdapter
from src.infrastructure.repository.currency_repository_database import CurrencyRepositoryDatabase
from src.infrastructure.repository.exchange_rate_repository_database import ExchangeRateRepositoryDatabase

connection = AsyncPGAdapter()
currency_repository = CurrencyRepositoryDatabase(connection)
exchange_rate_repository = ExchangeRateRepositoryDatabase(connection)

date_str = datetime.now().strftime('%Y-%m-%d')
date = datetime.strptime(date_str, '%Y-%m-%d')
value = 529.99


async def test_must_convert_currency_brl_to_usd() -> None:
    input_ = Input(
        currency_from='BRL',
        currency_to='USD',
        value=529.99,
        date=date,
    )
    currency_convert = ConvertCurrency(currency_repository, exchange_rate_repository)
    output = await currency_convert.execute(input_)
    output_expected = Output(value=98.23, currency_symbol='$', formatted_value='$98,23')
    assert output == output_expected


async def test_must_convert_currency_brl_to_eur() -> None:
    input_ = Input(currency_from='BRL', currency_to='EUR', date=date, value=value)
    currency_convert = ConvertCurrency(currency_repository, exchange_rate_repository)
    output: Output = await currency_convert.execute(input_)
    assert output.currency_symbol == '€'
    assert output.formatted_value == '€83,26'
    assert output.value == 83.26


async def test_must_convert_currency_brl_to_inr() -> None:
    input_ = Input(currency_from='BRL', currency_to='INR', date=date, value=value)
    currency_convert = ConvertCurrency(currency_repository, exchange_rate_repository)
    output = await currency_convert.execute(input_)
    assert output.currency_symbol == '₹'
    assert output.formatted_value == '₹7.318,93'
    assert output.value == 7318.93


async def test_must_convert_currency_brl_to_brl() -> None:
    input_ = Input(currency_from='BRL', currency_to='BRL', value=value, date=date)
    currency_convert = ConvertCurrency(currency_repository, exchange_rate_repository)
    output = await currency_convert.execute(input_)
    output_expected = Output(value=529.99, currency_symbol='R$', formatted_value='R$529,99')
    assert output == output_expected


async def test_must_not_convert_currency_brl_to_yen() -> None:
    input_ = Input(currency_from='BRL', currency_to='YEN', value=value, date=date)
    currency_convert = ConvertCurrency(currency_repository, exchange_rate_repository)
    with pytest.raises(ValueError) as context:
        await currency_convert.execute(input_)
    assert 'Currency with code YEN not found' in str(context.value)


async def test_must_not_convert_currency_brl_to_usd_with_negative_value() -> None:
    input_ = Input(currency_from='BRL', currency_to='USD', value=-value, date=date)
    currency_convert = ConvertCurrency(currency_repository, exchange_rate_repository)
    with pytest.raises(ValueError) as context:
        await currency_convert.execute(input_)
    assert 'value must be greater than zero' in str(context.value)


async def test_must_not_convert_currency_brl_to_usd_with_priceless_value() -> None:
    input_ = Input(currency_from='BRL', currency_to='USD', value=0, date=date)
    currency_convert = ConvertCurrency(currency_repository, exchange_rate_repository)
    with pytest.raises(ValueError) as context:
        await currency_convert.execute(input_)
    assert 'value must be greater than zero' in str(context.value)


async def test_must_not_convert_currency_brl_to_usd_when_data_not_exist() -> None:
    date_str = '2023-06-09'
    date = datetime.strptime(date_str, '%Y-%m-%d')
    input_ = Input(currency_from='BRL', currency_to='USD', value=0, date=date)
    currency_convert = ConvertCurrency(currency_repository, exchange_rate_repository)
    with pytest.raises(ValueError) as context:
        await currency_convert.execute(input_)
    assert 'No exchange rate found for the given currencies.' in str(context.value)
