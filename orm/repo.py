import orm.modelos as modelos
from sqlalchemy.orm import Session
from sqlalchemy import and_

# ------------ Peticiones a usuarios ---------------------

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

# ------------ Peticiones a fotos ---------------------

# GET '/fotos'
# select * from app.fotos
def devuelve_fotos(sesion:Session):
    print("select * from app.fotos")
    return sesion.query(modelos.Foto).all()

# GET '/fotos/{id}'
# select * from app.fotos where id = id_foto
def fotos_por_id_foto(sesion:Session,id_foto:int):
    print("select * from fotos where id = id_foto")
    return sesion.query(modelos.Foto).filter(modelos.Foto.id==id_foto).all()


# Buscar fotos por id de alumno
# GET '/alumnos/{id}/fotos'
# select * from app.fotos where id_alumno=id
def fotos_por_id_alumno(sesion:Session,id_alumno:int):
    print("select * from app.fotos where id_alumno=", id_alumno)
    return sesion.query(modelos.Foto).filter(modelos.Foto.id_alumno==id_alumno).all() 

# ------------ Peticiones a calificaciones ---------------------

# GET '/calificacion'
# select * from app.calificaciones
def devuelve_calificaciones(sesion:Session):
    print("select * from app.calificaciones")
    return sesion.query(modelos.Calificacion).all()

# select * from app.calificaciones where id_calificacion=id
def calificaciones_por_id_calificacion(sesion:Session,id_calificacion:int):
    print("select * from app.calificaciones where id=", id_calificacion)
    return sesion.query(modelos.Calificacion).filter(modelos.Calificacion.id==id_calificacion).all()

# select * from app.calificaciones where id_alumno=id
def calificaciones_por_id_alumno(sesion:Session,id_alumno:int):
    print("select * from app.calificaciones where id=", id_alumno)
    return sesion.query(modelos.Calificacion).filter(modelos.Calificacion.id_alumno==id_alumno).all()

# ------------ Borrar calificaciones de alumno ---------------------

# Borra calificaciones por id de alumno
# DELETE '/alumnos/{id}/ccalificacion'
# delete from app.calificacion where id_alumno=id
def borrar_calificaciones_por_id_alumno(sesion:Session,id_alumno:int):
    print("delete from app.calificaciones where id_alumno=",id_alumno)
    calificacion_usr = calificaciones_por_id_alumno(sesion, id_alumno)
    if calificacion_usr is not None:
        for calificacion_alumno in calificacion_usr:
            sesion.delete(calificacion_alumno)
        sesion.commit()

# ------------ Borrar fotos de alumno ---------------------

# Borra fotos por id de alumno
# DELETE '/alumnos/{id}/fotos'
# delete from app.fotos where id_alumno=id
def borrar_fotos_por_id_alumno(sesion:Session,id_alumno:int):
    print("delete from app.fotos where id_alumno=",id_alumno)
    fotos_usr = fotos_por_id_alumno(sesion, id_alumno)
    if fotos_usr is not None:
        for foto_alumno in fotos_usr:
            sesion.delete(foto_alumno)
        sesion.commit()

# ------------ Borrar alumno ---------------------

# DELETE '/alumnos/{id}'
# delete from app.alumnos where id=id_usuario
def borrar_alumno_por_id(sesion:Session,id_alumno:int):
    print("delete from app.alumnos where id=", id_alumno)
    #1.- select para ver si existe el alumno a borrar
    usr = alumno_por_id(sesion, id_alumno)
    #2.- Borramos
    if usr is not None:
        #Borramos alumno
        sesion.delete(usr)
        #Confirmar los cambios
        sesion.commit()
    respuesta = {
        "mensaje": "alumno eliminado"
    }
    return respuesta


# ------------ Borrar fotos ---------------------

def borrar_fotos_por_id_foto(sesion:Session,id_foto:int):
    print("delete from app.fotos where id_foto=",id_foto)
    fotos_del = fotos_por_id_foto(sesion, id_foto)
    if fotos_del is not None:
        for foto_borra in fotos_del:
            sesion.delete(foto_borra)
        sesion.commit()

# ------------ Borrar caificaciones ---------------------

def borrar_calificaciones_por_id_calificacion(sesion:Session,id_calificacion:int):
    print("delete from app.calificaciones where id_calificacion=",id_calificacion)
    calificacion_del = calificaciones_por_id_calificacion(sesion, id_calificacion)
    if calificacion_del is not None:
        for calificacion_borra in calificacion_del:
            sesion.delete(calificacion_borra)
        sesion.commit()