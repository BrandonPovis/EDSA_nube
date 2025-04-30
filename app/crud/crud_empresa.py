from fastapi import FastAPI, HTTPException, Depends, UploadFile, File, Form, Path
from sqlalchemy.orm import Session
from models.model_empresa import Empresa
import requests
from dotenv import load_dotenv
import os


# Cargar variables de entorno
load_dotenv()

TOKEN_RUC = os.getenv("TOKEN_RUC")

def buscar_ruc(ruc: str):
    try:
        url = f"https://api.apis.net.pe/v1/ruc?numero={ruc}"
        headers = {
            "Authorization": f"Bearer {TOKEN_RUC}"
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




