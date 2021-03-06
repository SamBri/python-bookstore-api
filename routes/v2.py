

from fastapi import FastAPI, Body, Header, File, APIRouter

#app_v2 = FastAPI(openapi_prefix="/v2")# fastapi object assigned to app
app_v2 = APIRouter()

# get user and passing query params
@app_v2.get("/user") # passing query params.
async def get_user_validation(password:str):
    return {"v2_query parameter":password}
