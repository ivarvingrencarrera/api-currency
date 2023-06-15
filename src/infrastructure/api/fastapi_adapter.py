from collections.abc import Callable
from typing import Any

import uvicorn
import uvloop
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import ORJSONResponse

from src.infrastructure.api.http_server import HttpServer


class FastAPIAdapter(HttpServer):
    def __init__(self, debug: bool) -> None:
        self.app = FastAPI(title='API Currency', debug=debug, default_response_class=ORJSONResponse)

    def on(self, method: str, url: str, callback: Callable) -> None:
        async def route_handler(request: Request) -> Any:
            try:
                params = request.path_params
                body = {} if request.method == 'GET' else await request.json()
                return await callback(params, body)
            except ValueError as e:
                raise HTTPException(status_code=422, detail=str(e)) from e

        self.app.add_api_route(url, route_handler, methods=[method])

    def listen(self, port: int) -> None:
        uvloop.install()
        uvicorn.run(self.app, host='127.0.0.1', port=port, loop='uvloop')
