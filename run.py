from fastapi import FastAPI, Body,Header, File
from starlette.requests import Request

from routes.v1 import app_v1
from routes.v2 import app_v2
from utils.security import check_jwt_token

app = FastAPI() # fastapi object assigned to app
app.mount("/v1", app_v1)
app.mount("/v2", app_v2)

