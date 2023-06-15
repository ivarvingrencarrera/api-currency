import os
from collections.abc import AsyncGenerator

from asgi_lifespan import LifespanManager
from httpx import AsyncClient
from pytest import fixture

os.environ['ENV'] = 'testing'

from src.main_api import app


@fixture
async def client() -> AsyncGenerator[AsyncClient, None]:
    async with LifespanManager(app) as manager:
        async with AsyncClient(app=manager.app, base_url='http://test') as client:
            yield client
