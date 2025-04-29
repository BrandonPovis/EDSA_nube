from pydantic import BaseModel
from fastapi import UploadFile, File, Form

class EmpresaID(BaseModel):
    id: int
    razonSocial: str 
    ruc: str 
    correo: str 
    direccion: str 
    telefono: str 
    paginaWeb: str

class Config:
    orm_mode = True