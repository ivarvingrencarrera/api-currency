from datetime import datetime

from pydantic import BaseModel

from src.application.repository.currency_repository import CurrencyRepository
from src.application.repository.exchange_rate_repository import ExchangeRateRepository
from src.domain.entity.currency import Currency
from src.domain.entity.exchange_rate import ExchangeRate
from src.domain.service.currency_converter_service import CurrencyConverterService


class Input(BaseModel):
    from_currency: str
    to_currency: str
    amount: float
    date: str


class Output(BaseModel):
    amount: float
    currency_symbol: str
    formatted_amount: str


class ConvertCurrency:
    def __init__(
        self,
        currency_repository: CurrencyRepository,
        exchange_rate_repository: ExchangeRateRepository,
    ) -> None:
        self.currency_repository = currency_repository
        self.exchange_rate_repository = exchange_rate_repository

    async def execute(self, input_: Input) -> Output:
        from_currency: Currency = await self.currency_repository.find_by_code(input_.from_currency)
        to_currency: Currency = await self.currency_repository.find_by_code(input_.to_currency)
        input_date = datetime.strptime(input_.date, '%Y-%m-%d %H:%M:%S')
        if from_currency == to_currency:
            amount_converted = input_.amount
        else:
            exchange_rate: ExchangeRate = await self.exchange_rate_repository.find(
                from_currency.id, to_currency.id, input_date
            )
            amount_converted = CurrencyConverterService.convert(exchange_rate, input_.amount)
        formatted_amount = CurrencyConverterService.format_currency(amount_converted, to_currency)
        return Output(
            amount=amount_converted,
            currency_symbol=to_currency.symbol,
            formatted_amount=formatted_amount,
        )
