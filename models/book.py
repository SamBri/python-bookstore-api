from fastapi.openapi.models import Schema
from pydantic import BaseModel

from models.author import Author
from utils.const import SCHEMA_DESCRIPTION


class Book(BaseModel):
    isbn: str = Schema(description=SCHEMA_DESCRIPTION)
    name: str
    author: Author
    year: int = Schema(lt=1900, gt=2100)

