import orm.modelos as modelos
import orm.esquemas as esquemas
from sqlalchemy.orm import Session
from sqlalchemy import and_

# ------------ Peticiones a alumnos ---------------------

# Esta función es llamada por api.py

# GET '/alumnos'
# select * from app.alumnos
def devuelve_alumnos(sesion:Session):
    print("select * from app.alumnos")
    return sesion.query(modelos.Alumno).all()

# para atender GET '/alumnos/{id}'
# select * from app.alumno where id = id_alumno
def alumno_por_id(sesion:Session,id_alumno:int):
    print("select * from app.alumnos where id = ", id_alumno)
    return sesion.query(modelos.Alumno).filter(modelos.Alumno.id==id_alumno).first()

#PUT '/alumnos/{id}
def actualiza_alumno(sesion:Session,id_alumno:int,alm_esquema:esquemas.AlumnosBase):
    #Verificar que el alumno existe
    alm_bd = alumno_por_id(sesion,id_alumno)
    if alm_bd is not None:
        alm_bd.nombre = alm_esquema.nombre
        alm_bd.edad = alm_esquema.edad
        alm_bd.domicilio = alm_esquema.domicilio
        alm_bd.carrera = alm_esquema.carrera
        alm_bd.trimestre = alm_esquema.trimestre
        alm_bd.email = alm_esquema.email
        alm_bd.password = alm_esquema.password
        #3.-  Confirmamos los cambios
        sesion.commit()
        #4.- Refrescar la  BD
        sesion.refresh(alm_bd)
        #5.- Imprimir los datos nuevos
        print(alm_esquema)
        return alm_esquema
    else:
        respuesta = {"mensaje": "No existe el alumno"}
        return  respuesta

#POST '/alumnos'
def guardar_alumno(sesion:Session, alm_nuevo:esquemas.AlumnosBase):
    #2.-Crear un nuevi objeo de la clase modelo alumno
    alm_bd = modelos.Alumno()
    alm_bd.nombre = alm_nuevo.nombre
    alm_bd.edad = alm_nuevo.edad
    alm_bd.domicilio = alm_nuevo.domicilio
    alm_bd.carrera = alm_nuevo.carrera
    alm_bd.trimestre = alm_nuevo.trimestre
    alm_bd.email = alm_nuevo.email
    alm_bd.password = alm_nuevo.password
    #3.- Insertar el nuevo objeto a la BD
    sesion.add(alm_bd)
    #4.- Confirmamos el cambio
    sesion.commit()
    #5.-Hacemos un refresh
    sesion.refresh(alm_bd)
    return alm_bd

#POST'/alumnos/{id}/calificaciones
def guardar_alumno_calificacion(sesion:Session,id_alumno:int,calf_nuevo:esquemas.CalificacionesBase):
    #Se crea un nuevo objeo dela clase modelo calificacion
    
    #Se  verifica que el alumno exista
    alm_bd = alumno_por_id(sesion,id_alumno)
    if alm_bd is not None:
        calf_bd = modelos.Calificacion()
        calf_bd.uea = calf_nuevo.uea
        calf_bd.calificacion = calf_nuevo.calificacion
           #3.- Insertar el nuevo objeto a la BD
        sesion.add(calf_bd)
        #3.-  Confirmamos los cambios
        sesion.commit()
        #4.- Refrescar la  BD
        sesion.refresh(calf_bd)
    else:
        mensaje = {"mensaje":"No existe el alumno"}
        return  mensaje
    return  calf_bd

#POST'/alumnos/{id}/fotos
def guardar_alumno_foto(sesion:Session,id_alumno:int,foto_esquema:esquemas.FotosBase):
    #Se crea un nuevo objeo dela clase modelo fotos
    
    #Se  verifica que el alumno exista
    foto_bd = alumno_por_id(sesion,id_alumno)
    if foto_bd is not None:
        foto_bd = modelos.Foto()
        foto_bd.titulo = foto_esquema.titulo
        foto_bd.descripcion = foto_esquema.descripcion
        foto_bd.ruta  = foto_esquema.ruta

        sesion.add(foto_bd)
        #3.-  Confirmamos los cambios
        sesion.commit()
        #4.- Refrescar la  BD
        sesion.refresh(foto_bd)
    else:
        mensaje = {"mensaje":"No existe el alumno"}
        return  mensaje
    return  foto_bd

# ------------ Peticiones a fotos ---------------------

# Buscar fotos por id de alumno
# GET '/alumnos/{id}/fotos'
# select * from app.fotos where id_alumno=id
def fotos_por_id_alumno(sesion:Session,id_alumno:int):
    print("select * from app.fotos where id_alumno=", id_alumno)
    return sesion.query(modelos.Foto).filter(modelos.Foto.id_alumno==id_alumno).all()

# GET '/fotos/{id}'
# select * from app.fotos where id = id_foto
def fotos_por_id_foto(sesion:Session,id_foto:int):
    print("select * from fotos where id = id_foto")
    return sesion.query(modelos.Foto).filter(modelos.Foto.id==id_foto).first()

#PUT '/fotos/{id}
def actualiza_fotos(sesion:Session,id_foto:int,foto_esquema:esquemas.FotosBase):
    #Verificar que la foto exista
    foto_bd = fotos_por_id_foto(sesion,id_foto)
    if foto_bd is not None:
        foto_bd.titulo = foto_esquema.titulo
        foto_bd.descripcion = foto_esquema.descripcion
        foto_bd.ruta = foto_esquema.ruta
        #3.-  Confirmamos los cambios
        sesion.commit()
        #4.- Refrescar la  BD
        sesion.refresh(foto_bd)
        #5.- Imprimir los datos nuevos
        print(foto_esquema)
        return foto_esquema
    else:
        respuesta = {"mensaje": "No existe la calificacion a modificar"}
        return  respuesta


# ------------ Peticiones a calificaciones ---------------------

# select * from app.calificaciones where id_alumno=id
def calificaciones_por_id_alumno(sesion:Session,id_alumno:int):
    print("select * from app.calificaciones where id=", id_alumno)
    return sesion.query(modelos.Calificacion).filter(modelos.Calificacion.id_alumno==id_alumno).all()

def calificaciones_por_id_calificacion(sesion:Session,id_calificacion:int):
    print("select * from app.calificaciones where id=", id_calificacion)
    return sesion.query(modelos.Calificacion).filter(modelos.Calificacion.id==id_calificacion).first()

#PUT '/calificaciones/{id}
def actualiza_calificacion(sesion:Session,id_calificacion:int,calf_esquema:esquemas.CalificacionesBase):
    #Verificar que el alumno existe
    calf_bd = calificaciones_por_id_calificacion(sesion,id_calificacion)
    if calf_bd is not None:
        calf_bd.uea = calf_esquema.uea
        calf_bd.calificacion = calf_esquema.calificacion
        #3.-  Confirmamos los cambios
        sesion.commit()
        #4.- Refrescar la  BD
        sesion.refresh(calf_bd)
        #5.- Imprimir los datos nuevos
        print(calf_esquema)
        return calf_esquema
    else:
        respuesta = {"mensaje": "No existe la calificacion a modificar"}
        return  respuesta
