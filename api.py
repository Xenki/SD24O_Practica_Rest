from fastapi import FastAPI, UploadFile, File, Form, Depends
from typing import Optional
from pydantic import BaseModel
import orm.esquemas as esquemas
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

@app.post("/alumnos")
def guardar_alumno(alumno:esquemas.AlumnosBase,sesion:Session=Depends(generador_sesion)):
    print(alumno)
    #guardado en la base.
    return repo.guardar_alumno(sesion,alumno)

@app.put("/alumnos{id}")
def actualizar_alumnos(id:int,info_alumno:esquemas.AlumnosBase,sesion:Session=Depends(generador_sesion)):
    return repo.actualiza_alumno(sesion,id,info_alumno)

@app.post("/alumnos/{id}/calificaciones")
def guardar_alumno_calificacion(id:int,calificacion:esquemas.CalificacionesBase,sesion:Session=Depends(generador_sesion)):
    print(calificacion)
    #guardado en la base.
    return repo.guardar_alumno_calificacion(sesion,id,calificacion)

@app.post("/alumnos/{id}/fotos")
def guardar_alumno_foto(id:int,foto:esquemas.FotosBase,sesion:Session=Depends(generador_sesion)):
    print(foto)
    #guardado en la base.
    return repo.guardar_alumno_foto(sesion,id,foto)

#-------------Peticion Fotos----------------------

@app.get("/fotos/{id}")
def fotos_por_id_foto(id:int, sesion:Session=Depends(generador_sesion)):
    print("Buscando foto por id")
    return repo.fotos_por_id_foto(sesion,id)

@app.put("/fotos/{id}")
def actualizar_fotos(id:int,info_foto:esquemas.FotosBase,sesion:Session=Depends(generador_sesion)):
    return repo.actualiza_fotos(sesion,id,info_foto)

#-------------Peticion Calificaciones----------------------
@app.get("/calificaciones")
def lista_calificaciones(sesion:Session=Depends(generador_sesion)):
    print("API consultando todas las calificaciones")
    return repo.devuelve_calificaciones(sesion)

@app.get("/calificaciones/{id}")
def calificaciones_por_id_calificacion(id:int,sesion:Session=Depends(generador_sesion)):
    print("API consultando calificaciones", id)
    return repo.calificaciones_por_id_calificacion(sesion, id)

@app.put("/calificaciones/{id}")
def actualizar_calificaciones(id:int,info_calificacion:esquemas.CalificacionesBase,sesion:Session=Depends(generador_sesion)):
    return repo.actualiza_calificacion(sesion,id,info_calificacion)


