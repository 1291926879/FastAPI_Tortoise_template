from fastapi.responses import UJSONResponse
from fastapi.requests import Request


class APIException(Exception):
    def __init__(self, status_code, message: str = '', *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)

        self.message = message
        self.status_code = status_code


async def on_api_exception(request: Request, exception: APIException) -> UJSONResponse:
    response = (
        content={"error": exception.message},
        status_code=exception.status_code,
        )
    try:
        return UJSONResponse(response)
    except:
        from fastapi.responses import JSONResponse
        return JSONResponse(response)