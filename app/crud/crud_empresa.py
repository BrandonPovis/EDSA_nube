from fastapi import FastAPI, HTTPException, Depends, UploadFile, File, Form, Path
from sqlalchemy.orm import Session
from models.model_empresa import Empresa
import requests


def create_empresa(db: Session, data: dict):
    if db.query(Empresa).filter(Empresa.ruc == data["ruc"]).first():
        return None 
    
    nueva = Empresa(**data)
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva

def get_empresa(db : Session):
    empresas = db.query(Empresa).all()
    resultado = []

    for emp in empresas:
        resultado.append({
            "razonSocial": emp.razonSocial,
            "ruc": emp.ruc,
            "correo": emp.correo,
            "direccion": emp.direccion,
            "telefono": emp.telefono,
            "paginaWeb": emp.paginaWeb,
        })

    return resultado



TOKEN = "https://dniruc.apisperu.com/api/v1/ruc/20131312955?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6InBvdmlzYnJheWFuQGdtYWlsLmNvbSJ9.sfT2jmtM9t-Rz9pME4c2UjPwkYR9czl0831ZJmh-xD0"

def buscar_ruc(ruc: str):
    try:
        url = f"https://api.apis.net.pe/v1/ruc?numero={ruc}"
        headers = {
            "Authorization": f"Bearer {TOKEN}"
        }

        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            raise HTTPException(status_code=400, detail="No se pudo consultar el RUC")

        data = response.json()

        return {
            "ruc": data.get("numeroDocumento"),
            "razon_social": data.get("nombre"),
            "estado": data.get("estado"),
            "direccion": data.get("direccion")
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno: {str(e)}")

