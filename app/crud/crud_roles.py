from fastapi import HTTPException
from core.database_NR import collection_name
from models.model_roles import RolModulo

# Helper para limpiar _id
def clean_mongo_document(doc: dict) -> dict:
    if "_id" in doc:
        del doc["_id"]
    return doc


# Crear rol
def create_role(role: RolModulo):
    if collection_name.find_one({"name": role.name}):
        raise ValueError("Ya existe un rol con ese nombre.")

    role_data = role.model_dump(by_alias=True)
    result = collection_name.insert_one(role_data)

    # Recuperar el rol insertado
    inserted_role = collection_name.find_one({"_id": result.inserted_id})

    # Eliminar el campo _id de la respuesta
    if inserted_role and "_id" in inserted_role:
        del inserted_role["_id"]
    return inserted_role


