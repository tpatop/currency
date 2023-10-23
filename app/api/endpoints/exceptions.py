from fastapi import HTTPException
from fastapi.responses import JSONResponse
from main import app


@app.exception_handler(HTTPException)
async def custom_exception_handler(exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={'error': exc.detail}
    )
