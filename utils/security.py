import datetime
import time

import jwt
from fastapi import Depends
from passlib.context import CryptContext
from starlette.exceptions import HTTPException

from models.jwt_user import JWTUser
from utils.const import JWT_EXPIRATION_TIME_MINUTES, JWT_SECRET_KEY, JWT_ALGORITHM
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from starlette.status import HTTP_401_UNAUTHORIZED
pwd_context = CryptContext(schemes=["bcrypt"])
oauth_schema = OAuth2PasswordBearer(tokenUrl="/token")

jwt_user1 = {"username":"user1", "password":"$2b$12$s.KVKPI/Vhv/yRJSQr59ieXhLPSGMDIr1Q23n2mTQVXGbOIX/6TmC", "disabled":False, "role": "admin"}
fake_jwt_user1 = JWTUser(**jwt_user1);

def get_hashed_password(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password,hashed_password)


#hashed = "$2b$12$06r//4B7zus864XRBpnTuOOzcPJUam5nhSbot0kZpDJB15TNSZpQ2"
#print(get_hashed_password("mysecret"))
#print(verify_password("mysecret",hashed))


# Authenticate username and password to give JWT token
def authenticate_user(user:JWTUser):
    if fake_jwt_user1.username == user.username:
        if verify_password(user.password, fake_jwt_user1.password):
            user.role = "admin"
            return user
    return None

# Create access JWT token
def create_jwt_token(user:JWTUser):
    expiration = datetime.datetime.utcnow() + datetime.timedelta(minutes=JWT_EXPIRATION_TIME_MINUTES)
    jwt_payload = {"sub":user.username,"role":user.role,"exp":expiration}
    jwt_token = jwt.encode(jwt_payload, JWT_SECRET_KEY,algorithm=JWT_ALGORITHM)
    return jwt_token

# Check whether JWT token is correct
def check_jwt_token(token:str = Depends(oauth_schema)):
    try:
        jwt_payload = jwt.decode(token, JWT_SECRET_KEY,algorithms=JWT_ALGORITHM)
        username = jwt_payload.get("sub")
        role = jwt_payload.get("role")
        expiration = jwt_payload.get("exp")
        if time.time() < expiration:
                if fake_jwt_user1.username == username:
                    return final_checks(role)
    except Exception as e:
            raise HTTPException(status_code=HTTP_401_UNAUTHORIZED)
    raise HTTPException(status_code=HTTP_401_UNAUTHORIZED)

# Last checking and returning the final result
def final_checks( role:str):
    if role == "admin":
        return True
    else:
        raise HTTPException(status_code=HTTP_401_UNAUTHORIZED)

