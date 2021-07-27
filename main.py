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
#myContactApp.insertarValores(nombreTabla=miTabla, nombre="Josefa", apellido="Martinez", phone="8296361446", email="john.albert@gmail.com")
#myContactApp.eliminarcontactID( miTabla, 5)


myContactApp.actualizar_contacto(miTabla, 11, phone=82923332222, email="peter.cabrera@gmail.com")
# Búsqueda inteligente
resultados = myContactApp.buscarValor(miTabla, "%")

# Sección Alfabética
# resultados = myContactApp.buscarValor(miTabla, "A%")
# resultados = myContactApp.buscarValor(miTabla, "J%")

myContactApp.conexion.commit()
myContactApp.micursor.close()
myContactApp.conexion.close()


"""def insertarNumero (numero):
    try: 
        myContactApp.conexion.commit()
        myContactApp.micursor.close()
        myContactApp.conexion.close()
    except:
        print("ERROR: el valor ingresado debe ser un numero")
"""

print(resultados)

#ok


