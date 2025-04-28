from fastapi import APIRouter,HTTPException
from models.model_roles import RolModulo
from core.database_NR import collection_name
from crud import crud_roles


router = APIRouter(prefix="/roles", tags=["Roles"])


@router.post("/")
def crear_rol(role: RolModulo):
    if collection_name.find_one({"name": role.name}):
        raise ValueError("Ya existe un rol con ese nombre.")
    crud_roles.create_role(role)
    return {"detail": "Rol creado correctamente."}


@router.get("/{name}", response_model=RolModulo)
async def get_role_by_name(name: str):
    role = collection_name.find_one({"name": name})
    if not role:
        raise HTTPException(status_code=404, detail="Rol no encontrado.")
    return crud_roles.clean_mongo_document(role)
    


@router.delete("/{name}", status_code=200)
def delete_role(name: str):
    result = collection_name.delete_one({"name": name})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Rol no encontrado para eliminar.")
    return {"detail": f"Rol '{name}' eliminado correctamente."}







# @router.get("/roles")
# async def get_todos():
#     todos = list_serial(collection_name.find())
#     return todos

# #POST Reques Method
# @router.post("/roles")
# async def post_todo(todo:Todo):
#         collection_name.insert_one(dict(todo))

# #PUT Requeste Method
# @router.put("/roles{id}")
# async def put_todo(id: str, todo:Todo):
#       collection_name.find_one_and_update({"_id":ObjectId(id)}, {"$set":dict(todo)})

# #DELET Request Method
# @router.delete("/roles{id}")
# async def delete_todo(id:str):
#       collection_name.find_one_and_delete({"_id":ObjectId(id)})