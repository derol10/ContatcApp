#! /usr/bin/env python
# -*- coding: utf-8 -*-
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
#print(buscarContacto("gmail.com"))
"""

#from sqlite3.dbapi2 import register_adapter
import string
from database import QueryBase

from tkinter import ttk
import tkinter as tk

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


# -------------------------------- tkinter --------------------------------


def getListOfKeys(dict):
    # retorna las llaves de un diccionario como una lista.
    list = []
    for key in dict.keys():
        list.append(key)
    return list

def getListOfValues(dict):
    # retorna las llaves de un diccionario como una lista.
    list = []
    for key in dict.values():
        list.append(key)
    return list

def caracterValido (caracter):
    # Solo permite introducir: 0-9, #, *, -
    # Adaptado desde https://foro.recursospython.com/printthread.php?tid=168
    return caracter in "0123456789*+#"
 

def AbrirVentana ():
    # Definiendo la Ventana y su geometría 
    root = tk.Tk()
    root.geometry("400x600")
    fuente = "Arial Rounded MT Bold"

    # configure the grid
    root.columnconfigure(0, weight=3)
    root.columnconfigure(1, weight=3)
    root.columnconfigure(2, weight=3)


    # Definiendo Label Principal
    etiquetaTitulo= tk.Label(text="Contactos", font=(fuente, 14))
    etiquetaTitulo.grid(column=1, row=0, sticky=tk.EW, padx=5, pady=5)

    # Definiendo Buscador
    etiquetaBuscar= tk.Label(text="Buscar", font=(fuente, 10))
    etiquetaBuscar.grid(column=0, row=1, sticky=tk.EW, padx=5, pady=5)
    buscador= tk.Entry(font=(fuente, 14))
    buscador.grid(column=1, row=1, sticky=tk.EW, padx=8, pady=5)

    # Agrupador de Contactos
    miscontactos = get_AZ()
    k = getListOfKeys(miscontactos)
    v = getListOfValues(miscontactos)
    
    i = 0
    #for x in miscontactos:
    #    for 
    
    
    

   # prueba
    listaNombre = tk.Listbox()
    listaNombre.insert(0,get_AZ())
    listaNombre.grid(column=1, row=2, sticky=tk.EW, padx=8, pady=5)

    # Habilitando un Entry con los caracteres permitidos.
    validarComando = root.register(caracterValido)
    cajadeNumero = ttk.Entry(root, validate="key", validatecommand=(validarComando, "%S"))
    cajadeNumero.grid(column=1)


    root.mainloop()

AbrirVentana()

#print(get_AZ())