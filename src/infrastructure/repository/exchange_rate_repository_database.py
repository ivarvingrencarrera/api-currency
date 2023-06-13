from datetime import datetime

from src.application.repository.exchange_rate_repository import ExchangeRateRepository
from src.domain.entity.exchange_rate import ExchangeRate
from src.infrastructure.database.connection import Connection


class ExchangeRateRepositoryDatabase(ExchangeRateRepository):
    def __init__(self, connection: Connection) -> None:
        self.connection = connection

    async def find(self, from_currency_id: int, to_currency_id: int, date: datetime) -> ExchangeRate:
        exchange_rate_query: str = ' \
            SELECT * FROM converter.exchange_rate \
            WHERE from_currency_id = $1 AND to_currency_id = $2 AND DATE(date_rate) = $3;'
        exchange_rate_data: list = await self.connection.select(
            exchange_rate_query, from_currency_id, to_currency_id, date
        )
        if not exchange_rate_data:
            raise ValueError('No exchange rate found for the given currencies.')
        exchange_rate = exchange_rate_data[0]
        return ExchangeRate(
            exchange_rate.id,
            exchange_rate.from_currency_id,
            exchange_rate.to_currency_id,
            exchange_rate.date_rate,
            float(exchange_rate.rate),
        )
