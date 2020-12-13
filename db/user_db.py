from typing import Dict
from pydantic import BaseModel

#Definición de UserInDB
class UserInDB(BaseModel):
    nombre: str
    apellido: str
    alias: str
    email:str
    year: int
    password: str
    saldo: float

# Base de datos ficticia 
database_users = Dict[str, UserInDB]
database_users = {
    "jsdajerp": UserInDB(**{"nombre":"Juan",
                            "apellido":"Dajer",
                            "alias":"jsdajerp",
                            "email":"dajerjuansaid@gmail.com",
                            "year":1993,
                            "password":"root",
                            "saldo":1000000}),
    "afgarciap": UserInDB(**{"nombre":"Andrés",
                            "apellido":"García",
                            "alias":"afgarciap",
                            "email":"andres.perea@hotmail.com",
                            "year":1994,
                            "password":"root1",
                            "saldo":1100000}),
    "srinconz": UserInDB(**{"nombre":"Santiago",
                            "apellido":"Rincón",
                            "alias":"srinconz",
                            "email":"chago591@hotmail.com",
                            "year":1992,
                            "password":"root2",
                            "saldo":1200000}),
    "dacaidedom": UserInDB(**{"nombre":"David",
                            "apellido":"Caicedo",
                            "alias":"dacaicedom",
                            "email":"david.merchancano@correounivalle.edu.co",
                            "year":1993,
                            "password":"root3",
                            "saldo":1300000}),
}
#Funciones sobre la base de datos ficticia
def get_user(alias: str):
    if alias in database_users.keys():
        return database_users[alias]
    else:
        return None

def update_user(user_in_db: UserInDB):
    database_users[user_in_db.alias] = user_in_db
    return user_in_db

def borrar_user(alias: str):
    if alias in database_users.keys():
        database_users.pop(alias)
    else:
        return None
def lista_user():
    lista=[]
    for i in database_users:
        a = "Nombre:",database_users[i].nombre,"Apellido:",database_users[i].apellido,"Alias:",database_users[i].alias,"Saldo",database_users[i].saldo
        lista.append(a)
    return lista
#implementar control de saldo