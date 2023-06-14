from collections.abc import AsyncGenerator

from httpx import AsyncClient
from pytest import fixture


@fixture
async def client() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(base_url='http://localhost:3004') as client:
        yield client
