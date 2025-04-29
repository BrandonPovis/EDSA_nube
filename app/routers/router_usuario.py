from fastapi import APIRouter, Depends
from sqlmodel import Session
from core.database import get_db
from crud.crud_usuario import create_usuario, get_usuarios
from schemas.schema_usuario import UsuarioCreate, UsuarioRead

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

@router.post("/")
def registrar_usuario(data: UsuarioCreate, db: Session = Depends(get_db)):
    usuario_creado = create_usuario(db, data)
    return{
        "message": "Usuario creado exitosamente",
        "username": usuario_creado.username}


@router.get("/", response_model=list[UsuarioRead])
def listar_usuarios(db: Session = Depends(get_db)):
    return get_usuarios(db)

