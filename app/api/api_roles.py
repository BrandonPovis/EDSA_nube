from fastapi import APIRouter
from models.model_roles import RolModulo
from core.database_NR import collection_name
from crud.crud_roles import serialize_rolmodulo
from fastapi import HTTPException
from bson import ObjectId

router = APIRouter(prefix="/roles", tags=["Roles"])

#GET Request Method


@router.post("/roles")
async def post_roles(RolModulo: RolModulo):
    try:
        document = serialize_rolmodulo(RolModulo)
        result = collection_name.insert_one(document)
        return {"message": "Rol guardado", "id": str(result.inserted_id)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



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