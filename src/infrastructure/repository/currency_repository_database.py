from src.application.repository.currency_repository import CurrencyRepository
from src.domain.entity.currency import Currency
from src.infrastructure.database.connection import Connection


class CurrencyRepositoryDatabase(CurrencyRepository):
    def __init__(self, connection: Connection) -> None:
        self.connection = connection

    async def find_by_code(self, code: str) -> Currency:
        currency_query: str = 'SELECT * FROM converter.currency WHERE alphabetic_code = $1;'
        currency_data: list = await self.connection.select(currency_query, code)
        if not currency_data:
            raise ValueError(f'Currency with code {code} not found')
        currency = currency_data[0]
        return Currency(
            currency.id,
            currency.alphabetic_code,
            currency.numeric_code,
            currency.name,
            currency.symbol,
        )
