from sqlmodel import SQLModel, Field
from typing import Optional
from sqlalchemy import Column, Boolean, String

class Usuario(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(sa_column=Column(String, unique=True, nullable=False))
    password: str
    nombre_completo: str
    empresa: str
    correo: str
    celular: str
    rol: str
    admin: bool = Field(default=False)
