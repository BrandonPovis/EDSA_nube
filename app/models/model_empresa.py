from sqlalchemy import Column, String, Integer, LargeBinary
from sqlmodel import SQLModel, Field
from typing import Optional

class Empresa(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    razonSocial: str
    ruc: str
    correo: str
    direccion: str
    telefono: str
    paginaWeb: str
    logo: Optional[bytes] = Field(default=None, sa_column=Column(LargeBinary, nullable=True))
