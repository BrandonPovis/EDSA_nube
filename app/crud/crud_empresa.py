from fastapi import FastAPI, HTTPException, Depends, UploadFile, File, Form, Path
from core.database import engine
from sqlalchemy.orm import Session
from models.model_empresa import Empresa
import base64


def create_empresa(db: Session, data: dict, logo: bytes = None):
    if db.query(Empresa).filter(Empresa.ruc == data["ruc"]).first():
        return None  # Ya existe

    nueva = Empresa(**data, logo=logo)
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva

def get_empresa(db : Session):
    empresas = db.query(Empresa).all()
    resultado = []

    for emp in empresas:
        logo_b64 = base64.b64encode(emp.logo).decode("utf-8") if emp.logo else None
        resultado.append({
            "id": emp.id,
            "razonSocial": emp.razonSocial,
            "ruc": emp.ruc,
            "correo": emp.correo,
            "direccion": emp.direccion,
            "telefono": emp.telefono,
            "paginaWeb": emp.paginaWeb,
            "logo": logo_b64
        })

    return resultado
