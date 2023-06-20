from datetime import datetime

from src.application.use_case.convert_currency import ConvertCurrency
from src.application.use_case.convert_currency import Input as ConvertCurrencyInput
from src.application.use_case.convert_currency import Output as ConvertCurrencyOutput
from src.application.use_case.get_currency import GetCurrency
from src.application.use_case.get_currency import Input as GetCurrencyInput
from src.application.use_case.get_currency import Output as GetCurrencyOutput
from src.infrastructure.api.http_server import HttpServer


class RouterController:
    def __init__(
        self, http_server: HttpServer, convert_currency: ConvertCurrency, get_currency: GetCurrency
    ) -> None:
        self.http_server = http_server
        self.convert_currency = convert_currency
        self.get_currency = get_currency

        self.http_server.on('POST', '/currencies/converter', self.convert_currency_handler)
        self.http_server.on('GET', '/currencies/{currency}', self.get_currency_handler)
        self.http_server.on('GET', '/test', self.get_test)

    async def convert_currency_handler(self, _: dict, body: dict) -> ConvertCurrencyOutput:
        date = datetime.strptime(body['date'], '%Y-%m-%d')
        input_ = ConvertCurrencyInput(
            currency_from=body['currency_from'],
            currency_to=body['currency_to'],
            date=date,
            value=body['value'],
        )
        return await self.convert_currency.execute(input_)

    async def get_currency_handler(self, params: dict, _: dict) -> GetCurrencyOutput:
        input_ = GetCurrencyInput(currency=params['currency'])
        return await self.get_currency.execute(input_)

    async def get_test(self, _: dict, __: dict) -> set:
        return {'Hello man!!!'}
