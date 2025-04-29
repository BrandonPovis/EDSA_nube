from sqlmodel import SQLModel

class UsuarioCreate(SQLModel):
    username: str
    password: str
    nombre_completo: str
    empresa: str
    correo: str
    celular: str
    rol: str
    admin: bool

class UsuarioRead(SQLModel):
    id: int
    username: str
    nombre_completo: str
    empresa: str
    correo: str
    celular: str
    rol: str
