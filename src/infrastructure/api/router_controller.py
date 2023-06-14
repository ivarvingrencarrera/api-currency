from datetime import datetime

from src.application.use_case.convert_currency import ConvertCurrency, Input, Output
from src.infrastructure.api.http_server import HttpServer


class RouterController:
    def __init__(self, http_server: HttpServer, convert_currency: ConvertCurrency) -> None:
        self.http_server = http_server
        self.convert_currency = convert_currency

        self.http_server.on('POST', '/currencies/converter', self.convert_currency_handler)

    async def convert_currency_handler(self, _: dict, body: dict) -> Output:
        date = datetime.strptime(body['date'], '%Y-%m-%d')
        input_ = Input(
            currency_from=body['currency_from'],
            currency_to=body['currency_to'],
            date=date,
            value=body['value'],
        )
        return await self.convert_currency.execute(input_)
