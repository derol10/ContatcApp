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
from ctypes import DEFAULT_MODE
import string
from database import QueryBase

from tkinter import *
from tkinter import ttk
import tkinter as tk

miDataBase = "MisContactos.db"
miTabla = "myContacts"
myContactApp = QueryBase(miDataBase)


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

def get_AZ ():
    # Retorna un diccionario de los contactos, agrupados segun su letra inicial alfabéticamente en orden ascendente.
    resultados = {}
    for i in string.ascii_uppercase:
        resultados[i] = myContactApp.buscarNombre(miTabla, f"{i}%")
    
    return resultados

def get_AZ_filtro (substring=""):
    # Retorna un diccionario de los contactos, agrupados segun su letra inicial alfabéticamente en orden ascendente.
    resultados = {}
    for i in string.ascii_uppercase:
        resultados[i] = myContactApp.buscarValor_AZ(miTabla, f"{i}%", f"%{substring}%")
    
    return resultados
# -------------------------------- tkinter --------------------------------
class ScrollableFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = tk.Canvas(self)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = ttk.Frame(canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

def caracterValido (caracter):
    # Solo permite introducir: 0-9, #, *, -
    # Adaptado desde https://foro.recursospython.com/printthread.php?tid=168
    return caracter in "0123456789*+#"
 

def AbrirVentana ():
    # Definiendo la Ventana y su geometría 
    root = Tk()
    root.geometry("400x600")
    fuenteTitulo = "Arial Rounded MT Bold"
    fuenteCuerpo = "Calibri" 

    # Pantalla Principal
    Label(text="Contactos", font=(fuenteTitulo, 14)).pack()

    # Definiendo Buscador
    
    
    frame = ScrollableFrame(root)
    def grupoContactos ():
        # Agrupador de Contactos  
        #Creando Scrollbar ----------
        #https://blog.teclado.com/tkinter-scrollable-frames/

        print(cajaBusqueda.get())
        miscontactos = get_AZ_filtro(str(cajaBusqueda.get()))
        for x, y in miscontactos.items():
            Label(frame.scrollable_frame, text=f"   {x}", width=1000, borderwidth=1, relief='raised' , anchor="w", font=(fuenteCuerpo, 14)).pack(anchor="w", padx="2", pady="2", fill="x")
            for z in y:
                Button(frame.scrollable_frame, text=f"{z[0]} - {z[1]} {z[2]} ", anchor="e", font=(fuenteCuerpo, 12)).pack(anchor="w", padx="20")
        
        frame.pack(pady="10", expand=True, fill='both')

    def borrarBusqueda ():
        for widgets in frame.winfo_children():
            widgets.pack_forget()
    
    Button(text="Buscar", font=(fuenteTitulo, 10), command= grupoContactos).pack()
    Button(text="Borrar", font=(fuenteTitulo, 10), command= borrarBusqueda).pack()
    cajaBusqueda = Entry(font=(fuenteTitulo, 14))
    cajaBusqueda.pack()
    
    

    grupoContactos()
    # ------------------------------------------------------

    # Habilitando un Entry con los caracteres permitidos.
    validarComando = root.register(caracterValido)
    cajadeNumero = Entry(root, validate="key", validatecommand=(validarComando, "%S"))
    cajadeNumero.pack()
    
    root.mainloop()

AbrirVentana()



#print(get_AZ())