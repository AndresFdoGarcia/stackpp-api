from pydantic import BaseModel
from datetime import datetime

class MovemIn(BaseModel):
    alias: str
    value: int
class MovemOUT(BaseModel):
    id_movem: int
    alias: str
    fecha: datetime
    value: int
    actual_saldo: int