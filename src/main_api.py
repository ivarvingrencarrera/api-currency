import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

from src import config
from src.application.use_case.convert_currency import ConvertCurrency
from src.application.use_case.get_currency import GetCurrency
from src.infrastructure.api.fastapi_adapter import FastAPIAdapter
from src.infrastructure.api.router_controller import RouterController
from src.infrastructure.database.asyncpg_adapter import AsyncPGAdapter
from src.infrastructure.repository.currency_repository_database import CurrencyRepositoryDatabase
from src.infrastructure.repository.exchange_rate_repository_database import ExchangeRateRepositoryDatabase

connection = AsyncPGAdapter()
currency_repository = CurrencyRepositoryDatabase(connection)
exchange_rate_repository = ExchangeRateRepositoryDatabase(connection)
convert_currency = ConvertCurrency(currency_repository, exchange_rate_repository)
get_currency = GetCurrency(currency_repository)
http_server = FastAPIAdapter(config.DEBUG)
RouterController(http_server, convert_currency, get_currency)
app = http_server.app
if not config.TESTING:
    http_server.listen(5000, '127.0.0.1')
