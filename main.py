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
"""

from database import QueryBase

miDataBase = "MisContactos.db"
miTabla = "myContacts"

myContactApp = QueryBase(miDataBase)

#myContactApp.crearTabla(miTabla)
#myContactApp.insertarValores(nombreTabla=miTabla, nombre="Maria", apellido="Abreu", phone="809-962-6944", email="maria@gmail.com")
myContactApp.eliminarcontactID( miTabla, 4)

resultados = myContactApp.buscarValor(miTabla, "%")

myContactApp.conexion.commit()
myContactApp.micursor.close()
myContactApp.conexion.close()

print(resultados)