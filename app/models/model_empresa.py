from sqlalchemy import Column, String, Integer, LargeBinary
from sqlmodel import SQLModel, Field
from typing import Optional

class Empresa(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    ruc: str = Field(sa_column=Column(String, unique=True, index=True, nullable=False))
    razonSocial: str
    correo: str
    direccion: str
    telefono: str
    paginaWeb: str
