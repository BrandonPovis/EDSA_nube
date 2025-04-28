from pydantic import BaseModel, Field
from typing import List, Optional

class SubPermiso(BaseModel):
    name: str = Field(..., example="Agregar operador")
    permission: str = Field(..., example="Solo Lectura")

class Modulo(BaseModel):
    name: str = Field(..., example="Planificación")
    sub: List[SubPermiso] = Field(..., example=[
        {"name": "Agregar operador", "permission": "Solo Lectura"},
        {"name": "Agregar conductor", "permission": "Administrador"}
    ])

class RolModulo(BaseModel):
    name: str = Field(..., example="Administrador")
    modules: List[Modulo] = Field(..., example=[
        {
            "name": "Planificación",
            "sub": [
                {"name": "Agregar operador", "permission": "Solo Lectura"},
                {"name": "Agregar conductor", "permission": "Administrador"}
            ]
        },
        {
            "name": "Programación",
            "sub": [
                {"name": "Carga masiva conductor", "permission": "Lectura y Escritura"},
                {"name": "Carga masiva cobrador", "permission": "Administrador"}
            ]
        }
    ])

    class Config:
        allow_population_by_field_name = True

# class Todo(BaseModel):
#     name: str
#     description: str
#     complete: bool