from fastapi import FastAPI
from api.v1.api import api_router
from core.config import config

app = FastAPI()
app.include_router(api_router, prefix=config.API_V1_STR)
