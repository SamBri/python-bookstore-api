from typing import List

from pydantic import BaseModel


class Author(BaseModel):
    id: int
    name: str
    book: List[str]
