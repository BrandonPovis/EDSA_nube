from sqlmodel import Session
from models.model_usuario import Usuario
from schemas.schema_usuario import UsuarioCreate

def create_usuario(db: Session, data: UsuarioCreate) -> Usuario:
    nuevo_usuario = Usuario(**data.model_dump())
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return nuevo_usuario


def get_usuarios(db: Session) -> list[Usuario]:
    return db.session.exec(Usuario).all()

