from pydantic import BaseModel

# user model
class JWTUser(BaseModel):
    username: str
    password: str
    disabled: bool = False
    role: str = None
