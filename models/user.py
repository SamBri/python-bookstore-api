from fastapi import Query
from pydantic import BaseModel
import enum

# role
class Role(enum.Enum):
    admin:str = "admin"
    personel:str = "personel"

# user model
class User(BaseModel):
    name: str
    password: str
    mail: str
    role: Role