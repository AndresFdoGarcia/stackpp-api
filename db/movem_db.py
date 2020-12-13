from datetime import datetime
from pydantic import BaseModel

class MovemInDB (BaseModel):
    id_movem : int = 0
    alias: str
    fecha : datetime = datetime.now()
    value : int
    actual_saldo : int

database_movem = []
generator = {"id":0}

def save_movem(movem_in_db: MovemInDB):
    generator["id"] = generator["id"] + 1
    movem_in_db.id_movem = generator["id"]
    database_movem.append(movem_in_db)
    return movem_in_db