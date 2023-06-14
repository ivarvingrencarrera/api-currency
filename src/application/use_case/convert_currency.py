from datetime import datetime

from pydantic import BaseModel

from src.application.repository.currency_repository import CurrencyRepository
from src.application.repository.exchange_rate_repository import ExchangeRateRepository
from src.domain.entity.currency import Currency
from src.domain.entity.exchange_rate import ExchangeRate
from src.domain.service.currency_converter_service import CurrencyConverterService


class Input(BaseModel):
    currency_from: str
    currency_to: str
    date: datetime
    value: float


class Output(BaseModel):
    value: float
    currency_symbol: str
    formatted_value: str


class ConvertCurrency:
    def __init__(
        self,
        currency_repository: CurrencyRepository,
        exchange_rate_repository: ExchangeRateRepository,
    ) -> None:
        self.currency_repository = currency_repository
        self.exchange_rate_repository = exchange_rate_repository

    async def execute(self, input_: Input) -> Output:
        currency_from: Currency = await self.currency_repository.find_by_code(input_.currency_from)
        currency_to: Currency = await self.currency_repository.find_by_code(input_.currency_to)
        if currency_from == currency_to:
            value_converted = input_.value
        else:
            exchange_rate: ExchangeRate = await self.exchange_rate_repository.find(
                currency_from.id, currency_to.id, input_.date
            )
            value_converted = CurrencyConverterService.convert(exchange_rate, input_.value)
        formatted_value = CurrencyConverterService.format_currency(value_converted, currency_to)
        return Output(
            value=value_converted,
            currency_symbol=currency_to.symbol,
            formatted_value=formatted_value,
        )
