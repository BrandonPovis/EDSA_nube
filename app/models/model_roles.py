from pydantic import BaseModel
from typing import List

class SubPermiso(BaseModel):
    name: str
    permission: str

class RolModulo(BaseModel):
    name: str
    sub: List[SubPermiso]  


# class Todo(BaseModel):
#     name: str
#     description: str
#     complete: bool