from fastapi import FastAPI, UploadFile, File, Form, Depends
from typing import Optional
from pydantic import BaseModel
import shutil
import os
import uuid
import orm.repo as repo #funciones para hacer consultas a la BD
from sqlalchemy.orm import Session
from orm.config import generador_sesion #generador de sesiones

# creación del servidor
app = FastAPI()

# decorator
@app.get("/")
def hola_mundo():
    print("invocando a ruta /")
    respuesta = {
        "mensaje": "hola mundo!"
    }

    return respuesta

#-------------Peticion Alumnos----------------------

@app.get("/alumnos")
def lista_alumnos(sesion:Session=Depends(generador_sesion)):
    print("API consultando todos los alumnos")
    return repo.devuelve_alumnos(sesion)

@app.get("/alumnos/{id}")
def alumno_por_id(id:int,sesion:Session=Depends(generador_sesion)):
    print("Api consultando alumno por id")
    return repo.alumno_por_id(sesion, id)

@app.get("/alumnos/{id}/calificaciones")
def calificaciones_por_id_alumno(id:int,sesion:Session=Depends(generador_sesion)):
    print("API consultando calificaciones del alumno ", id)
    return repo.calificaciones_por_id_alumno(sesion, id)

@app.get("/alumnos/{id}/fotos")
def fotos_por_id_alumno(id:int,sesion:Session=Depends(generador_sesion)):
    print("API consultando fotos del alumno ", id)
    return repo.fotos_por_id_alumno(sesion, id)

#-------------Peticion Fotos----------------------

@app.get("/fotos/{id}")
def fotos_por_id_foto(id:int, sesion:Session=Depends(generador_sesion)):
    print("Buscando foto por id")
    return repo.fotos_por_id_foto(sesion,id)

#-------------Peticion Calificaciones----------------------
@app.get("/calificaciones")
def lista_calificaciones(sesion:Session=Depends(generador_sesion)):
    print("API consultando todas las calificaciones")
    return repo.devuelve_calificaciones(sesion)

@app.get("/calificaciones/{id}")
def calificaciones_por_id_calificacion(id:int,sesion:Session=Depends(generador_sesion)):
    print("API consultando calificaciones", id)
    return repo.calificaciones_por_id_calificacion(sesion, id)


#------------- DELETE ----------------------
    
@app.delete("/alumno/{id}")
def borrar_alumno(id:int, sesion:Session=Depends(generador_sesion)):
    repo.borrar_calificaciones_por_id_alumno(sesion,id)
    repo.borrar_fotos_por_id_alumno(sesion,id)
    repo.borrar_alumno_por_id(sesion,id)
    return {"alumno_borrado", "ok"}

@app.delete("/alumno/{id}/calificaciones")
def borrar_alumno_calificaciones(id:int, sesion:Session=Depends(generador_sesion)):
    repo.borrar_calificaciones_por_id_alumno(sesion,id)
    return {"calificaciones_del_alumno_borrado", "ok"}

@app.delete("/alumno/{id}/fotos")
def borrar_alumno_fotos(id:int, sesion:Session=Depends(generador_sesion)):
    repo.borrar_fotos_por_id_alumno(sesion,id)
    return {"fotos_del_alumno_borrado", "ok"}

@app.delete("/calificacion/{id}")
def borrar_calificaciones(id:int, sesion:Session=Depends(generador_sesion)):
    repo.borrar_calificaciones_por_id_calificacion(sesion,id)
    return {"calificaciones_borradas", "ok"}

@app.delete("/foto/{id}")
def borrar_foto(id:int, sesion:Session=Depends(generador_sesion)):
    repo.borrar_fotos_por_id_foto(sesion,id)
    return {"fotos_borradas", "ok"}

