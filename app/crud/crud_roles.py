from fastapi.responses import JSONResponse
from models.model_roles import RolModulo
from fastapi import HTTPException
from bson import ObjectId

def serialize_rolmodulo(rol: RolModulo) -> dict:
    return {
        "name": rol.name,
        "sub": [sub.model_dump() for sub in rol.sub]
    }




# def individual_serial(todo) -> dict:
#     return {
#         "id":str(todo["_id"]),
#         "name":todo["name"],
#         "description": todo["description"],
#         "complete": todo ["complete"]

#     }

# def list_serial(todos) -> list:
#     return [individual_serial(todo) for todo in todos] 

