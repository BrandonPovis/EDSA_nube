from fastapi import APIRouter, HTTPException, Depends, UploadFile, File, Form, Path
from crud.crud_empresa import create_empresa, get_empresa, buscar_ruc
from sqlalchemy.orm import Session
from core.database import get_db

router = APIRouter(prefix="/empresas", tags=["Empresas"])

@router.post("/")
async def crear_empresa(
    razonSocial: str = Form(...),
    ruc: str = Form(...),
    correo: str = Form(...),
    direccion: str = Form(...),
    telefono: str = Form(...),
    paginaWeb: str = Form(...),
    db: Session = Depends(get_db)
):

    data_dict = {
        "razonSocial": razonSocial,
        "ruc": ruc,
        "correo": correo,
        "direccion": direccion,
        "telefono": telefono,
        "paginaWeb": paginaWeb
    }

    empresa = create_empresa(db, data_dict)
    if not empresa:
        raise HTTPException(status_code=400, detail="El RUC ya está registrado")

    return {
        "message": "Empresa creada exitosamente",
        "id": empresa.id
    }


@router.get("/")  
async def get_empresas(db: Session = Depends(get_db)):
    return get_empresa(db)

@router.get("/GET RUC")
async def get_ruc_sunat(ruc: str):
    return buscar_ruc(ruc)
