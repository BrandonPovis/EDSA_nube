from fastapi import APIRouter, HTTPException, Depends, UploadFile, File, Form, Path
from contextlib import asynccontextmanager
from crud.crud_empresa import create_empresa
from sqlalchemy.orm import Session
from schemas.schema_empresa import EmpresaID
from crud import crud_empresa
from core.database import get_db
from models.model_empresa import Empresa

router = APIRouter(prefix="/empresas", tags=["Empresas"])

@router.post("/empresas/")
async def crear_empresa(
    razonSocial: str = Form(...),
    ruc: str = Form(...),
    correo: str = Form(...),
    direccion: str = Form(...),
    telefono: str = Form(...),
    paginaWeb: str = Form(...),
    logo: UploadFile = File(None),
    db: Session = Depends(get_db)
):
    logo_data = await logo.read() if logo else None

    data_dict = {
        "razonSocial": razonSocial,
        "ruc": ruc,
        "correo": correo,
        "direccion": direccion,
        "telefono": telefono,
        "paginaWeb": paginaWeb
    }

    empresa = crud_empresa.create_empresa(db, data_dict, logo_data)
    if not empresa:
        raise HTTPException(status_code=400, detail="El RUC ya está registrado")

    return {
        "message": "Empresa creada exitosamente",
        "id": empresa.id
    }



@router.get("/empresas/")  
async def get_empresas(db: Session = Depends(get_db)):
    return crud_empresa.get_empresa(db)