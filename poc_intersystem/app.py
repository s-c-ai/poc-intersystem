from fastapi import FastAPI

from poc_intersystem.routers import router

app = FastAPI()


@app.get('/healthcheck/')
def healthcheck():
    return {'status': 'ok'}


app.include_router(router)
