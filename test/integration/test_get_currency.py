from src.application.use_case.get_currency import GetCurrency, Input, Output
from src.infrastructure.database.asyncpg_adapter import AsyncPGAdapter
from src.infrastructure.repository.currency_repository_database import CurrencyRepositoryDatabase

connection = AsyncPGAdapter()
currency_repository = CurrencyRepositoryDatabase(connection)


async def test_get_currency_brl() -> None:
    input_ = Input(currency='BRL')
    get_currency = GetCurrency(currency_repository)
    output = await get_currency.execute(input_)
    output_expected = Output(code='BRL', name='Brazilian Real', symbol='R$')
    assert output == output_expected
