from db.user_db import UserInDB
from db.user_db import update_user, get_user, borrar_user,lista_user
from db.movem_db import MovemInDB
from db.movem_db import save_movem

from models.user_models import UserIn, UserOut,GetUser
from models.movem_models import MovemIn,MovemOUT

import datetime
from fastapi import FastAPI
from fastapi import HTTPException

api = FastAPI()

@api.post("/user/auth/")
async def auth_user(user_in: UserIn):
    user_in_db = get_user(user_in.alias)
    if user_in_db == None:
        raise HTTPException(status_code=404,
                            detail="El usuario no existe")
    if user_in_db.password != user_in.password:
        return {"Autenticado": False}
    return {"Autenticado": True}

@api.get("/user/saldo/{alias}")
async def get_saldo(alias: str):
    user_in_db = get_user(alias)
    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")
    user_out = UserOut(**user_in_db.dict())
    return user_out

@api.put("/user/movem/")
async def make_movem_add(movem_in: MovemIn):
    user_in_db = get_user(movem_in.alias)
    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")

    user_in_db.saldo = user_in_db.saldo + movem_in.value
    update_user(user_in_db)

    movem_in_db = MovemInDB(**movem_in.dict(),actual_saldo = user_in_db.saldo)
    movem_in_db = save_movem(movem_in_db)

    movem_out = MovemOUT(**movem_in_db.dict())
    return movem_out

@api.delete("/user/borrar/")
async def user_delete(user_get: GetUser):
    usuario = get_user(user_get.alias)
    if usuario == None:
        raise HTTPException(status_code=404,
                            detail="El usuario no existe")
    else:  
        borrar_user(usuario.alias)
        raise HTTPException(status_code=200,
                                detail="El usuario ha sido eliminado")

@api.get("/user/lista/")
async def user_list():
    return lista_user()