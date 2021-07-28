"""
Introducción a Programación con Python.
Proyecto Agenda teléfonica de contactos.

Profesor:
Francis Fulgencio

Integrantes:
    Emmanuel Del Rosario Leonardo
    Josué Rafael Piña Fermín
    John Albert González De La Rosa
    Nelis Altagracia Ortiz Melo

Funciones Probadas:
#myContactApp.crearTabla(miTabla)
"""

#from sqlite3.dbapi2 import register_adapter
import string
from database import QueryBase

miDataBase = "MisContactos.db"
miTabla = "myContacts"
myContactApp = QueryBase(miDataBase)

def get_AZ ():
    # Retorna un diccionario de los contactos, agrupados segun su letra inicial alfabéticamente en orden ascendente.
    resultados = {}
    for i in string.ascii_uppercase:
        resultados[i] = myContactApp.buscarNombre(miTabla, f"{i}%")
    
    return resultados

def agregarContacto (nombre = "", apellido = "", phone = "", email = ""):
    myContactApp.insertarValores(nombreTabla=miTabla, nombre=nombre, apellido=apellido, phone=phone, email=email)

def buscarContacto (substring):
    return myContactApp.buscarValor(miTabla, f"%{substring}%")

def borrarContacto (contactID):
    myContactApp.eliminarcontactID( miTabla, contactID)

def actualizarContacto (contactID, nombre = "", apellido = "", phone = "", email = ""):
    myContactApp.actualizar_contacto(miTabla, contactID, nombre, apellido, phone, email)

def cerrarGuardar (bool = False):
    if bool == True:
        myContactApp.conexion.commit()
    
    myContactApp.micursor.close()
    myContactApp.conexion.close()

print(buscarContacto("gmail.com"))