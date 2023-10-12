import uvicorn
from fastapi import FastAPI

from api.endopoints.users import Router as uRouter
from api.endopoints.currency import Router as cuRouter


app = FastAPI()
app.include_router(uRouter, prefix='/auth')
app.include_router(cuRouter, prefix='/currency')


@app.get('/')
async def root():
    return {'message': 'This is root directory'}


if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1',
                port=8080, reload=True, workers=1)
