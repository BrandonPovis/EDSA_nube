from fastapi import HTTPException
from core.database_NR import collection_name
from models.model_roles import RolModulo

# Helper para limpiar _id
def clean_mongo_document(doc: dict) -> dict:
    if "_id" in doc:
        del doc["_id"]
    return doc


# Crear rol
def create_or_update_role(role: RolModulo):
    role_data = role.model_dump(by_alias=True)

    # Reemplaza el documento si ya existe uno con el mismo nombre, o lo inserta si no existe
    collection_name.replace_one(
        {"name": role.name},  # Filtro por nombre
        role_data,            # Documento nuevo
        upsert=True           # Crea si no existe
    )

    # Recuperar el documento actualizado/insertado
    updated_role = collection_name.find_one({"name": role.name})

    # Eliminar el campo _id si no lo necesitas
    if updated_role and "_id" in updated_role:
        del updated_role["_id"]

    return updated_role
