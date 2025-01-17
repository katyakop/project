from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from app.routes import router

app = FastAPI()

# Инициализация инструментатора
instrumentator = Instrumentator()
instrumentator.instrument(app).expose(app)

app.include_router(router)


