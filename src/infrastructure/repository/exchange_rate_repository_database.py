from datetime import datetime

from src.application.repository.exchange_rate_repository import ExchangeRateRepository
from src.domain.entity.exchange_rate import ExchangeRate
from src.infrastructure.database.connection import Connection


class ExchangeRateRepositoryDatabase(ExchangeRateRepository):
    def __init__(self, connection: Connection) -> None:
        self.connection = connection

    async def find(self, currency_from_id: int, currency_to_id: int, date: datetime) -> ExchangeRate:
        exchange_rate_query: str = ' \
            SELECT * FROM currency_exchange_rates.exchange_rate \
            WHERE currency_from_id = $1 AND currency_to_id = $2 AND DATE(date_rate) = $3;'
        exchange_rate_data: list = await self.connection.select(
            exchange_rate_query, currency_from_id, currency_to_id, date
        )
        if not exchange_rate_data:
            raise ValueError('No exchange rate found for the given currencies.')
        exchange_rate = exchange_rate_data[0]
        return ExchangeRate(
            exchange_rate.id,
            exchange_rate.currency_from_id,
            exchange_rate.currency_to_id,
            exchange_rate.date_rate,
            float(exchange_rate.rate),
        )
