from collections.abc import Callable

import uvicorn
import uvloop
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import ORJSONResponse
from fastapi.routing import APIRouter

from src.infrastructure.api.http_server import HttpServer


class FastAPIAdapter(HttpServer):
    def __init__(self) -> None:
        self.app = FastAPI(default_response_class=ORJSONResponse)
        self.router = APIRouter()

    def on(self, method: str, url: str, callback: Callable) -> None:
        async def route_handler(request: Request) -> dict:
            try:
                params = request.path_params
                body = {} if request.method == 'GET' else await request.json()
                return await callback(params, body)
            except ValueError as e:
                raise HTTPException(status_code=422, detail=str(e)) from e

        self.router.add_api_route(url, route_handler, methods=[method])

    def listen(self, port: int) -> None:
        self.app.include_router(self.router)
        uvloop.install()
        uvicorn.run(self.app, host='127.0.0.1', port=port, loop='uvloop')
