# НЕ СОВСЕМ ПОНЯТНА НЕОБХОДИМОСТЬ

# from fastapi import HTTPException, Request
# from fastapi.responses import JSONResponse
# from main import app


# class CustomException(HTTPException):
#     def __init__(self, detail: str,
#                  status_code: int = 400):
#         super().__init__(status_code=status_code, detail=detail)


# @app.exception_handler(CustomException)
# async def custom_exception_handler(request: Request,
#                                    exc: CustomException):
#     return JSONResponse(
#         status_code=exc.status_code,
#         content={'error': exc.detail}
#     )
