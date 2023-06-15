from pydantic import BaseModel

from src.application.repository.currency_repository import CurrencyRepository
from src.domain.entity.currency import Currency


class Input(BaseModel):
    currency: str


class Output(BaseModel):
    code: str
    name: str
    symbol: str


class GetCurrency:
    def __init__(self, currency_repository: CurrencyRepository) -> None:
        self.currency_repository = currency_repository

    async def execute(self, input_: Input) -> Output:
        currency: Currency = await self.currency_repository.find_by_code(input_.currency)
        return Output(code=currency.alphabetic_code, name=currency.name, symbol=currency.symbol)
