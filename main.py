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
from os import name
import string
from typing import Dict, Sized
from database import QueryBase

from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter.messagebox import *

miDataBase = "MisContactos.db"
miTabla = "myContacts"
myContactApp = QueryBase(miDataBase)

def agregarContacto (nombre = "", apellido = "", phone = "", email = ""):
    myContactApp.insertarValores(nombreTabla=miTabla, nombre=nombre, apellido=apellido, phone=phone, email=email)
    return myContactApp.buscarValor (miTabla,  "%").pop()

def buscarContacto (substring):
    return myContactApp.buscarValor(miTabla, f"%{substring}%")

def borrarContacto (contactID):
    myContactApp.eliminarcontactID( miTabla, contactID)

def actualizarContacto (contactID, nombre = "", apellido = "", phone = "", email = ""):
    myContactApp.actualizar_contacto(miTabla, contactID, nombre, apellido, phone, email)

def buscarID (contactID):
    return myContactApp.buscarParam_byContactID(miTabla, contactID)

def cerrarGuardar (bool = False):
    if bool == True:
        myContactApp.conexion.commit()
    
    #myContactApp.micursor.close()
    #myContactApp.conexion.close()

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
    root.iconbitmap('icon.ico') #https://www.codegrepper.com/code-examples/python/tkinter+change+app+icon
    root.title('ContactApp')
    
    fuenteTitulo = "Arial Rounded MT Bold"
    fuenteCuerpo = "Calibri" 

    # Pantalla Principal
    #Label(root, image= PhotoImage(file= 'Apps-Contacts-icon.png'), height="96", width='96' ).pack()
    Label(root, text="Contactos", font=(fuenteTitulo, 14)).pack()
    Button(root, text="Cerrar ventana", command=root.destroy).pack(side=TOP)

    # Definiendo Buscador
    def borrarFrame (tipoframe):
        for widgets in root.winfo_children():
            print(type(widgets))
            if tipoframe in str(type(widgets)):
                widgets.destroy()

    def volverAtras():
        borrarFrame('.Frame')
        agregarContactoBoton.pack()
        buscarBoton.pack()
        cajaBusqueda.pack()
        grupoContactos ()
        myContactApp.conexion.rollback()

    def perfil(contactID):
        def interfaz_actualizarContactos (contactID):
            if e1.get() != "" or e2.get() != "" or e3.get() != "" or e4.get() !="":
                actualizarContacto(contactID = contactID, nombre=e1.get(), apellido=e2.get(), phone=e3.get(), email=e4.get())
                cerrarGuardar(True)
                showinfo(title="Contacto actualizado",message=f"el contacto {contactID} ha sido actualizado!")
            else:
                showerror(title="ERROR", message="ERROR: ingrese texto en almenos un campo")
                
        def interfaz_borrarContacto (contactID):
            respuesta = askyesno(title="Eliminar Contacto", message= "¿Desea eliminar el contacto?" )
            if respuesta==YES:
                borrarContacto (contactID)
                cerrarGuardar(True)
                showinfo(title="Contacto", message="el contacto se ha eliminado de forma exitosa!")
                volverAtras()

        borrarFrame('__main__.ScrollableFrame')
        buscarBoton.pack_forget()
        cajaBusqueda.pack_forget()
        agregarContactoBoton.pack_forget()
        datos = buscarID(contactID)
        print(datos)        
        
        frame = Frame(root)
        
        Button(frame, text="Volver atrás", command=volverAtras).pack()
        Button(frame, text="Actualizar / Guardar contacto", command= lambda: interfaz_actualizarContactos(contactID)).pack()
        Button(frame, text="Eliminar Contacto", command= lambda: interfaz_borrarContacto(contactID)).pack()

        print(type(datos))
        Label(frame, text="Nombre", font=(fuenteCuerpo, 14)).pack()
        e1 = Entry(frame, font=(fuenteCuerpo, 14))
        e1.insert(END, datos[0][1])
        e1.pack()

        Label(frame, text="Apellido", font=(fuenteCuerpo, 14)).pack()
        e2 = Entry(frame, font=(fuenteCuerpo, 14))
        e2.insert(END, datos[0][2])
        e2.pack()


        Label(frame, text="Telefono", font=(fuenteCuerpo, 14)).pack()

        # https://foro.recursospython.com/printthread.php?tid=168
        validarComando = root.register(caracterValido)
        e3 = Entry(frame, font=(fuenteCuerpo, 14))
        e3.insert(END, datos[0][3])
        e3.config(validate="key", validatecommand=(validarComando, "%S"))
        e3.pack()

        Label(frame, text="Correo", font=(fuenteCuerpo, 14)).pack()
        e4 = Entry(frame, font=(fuenteCuerpo, 14))
        e4.insert(END, datos[0][4])
        e4.pack()

        frame.pack()


    def grupoContactos ():
        # Agrupador de Contactos  
        #Creando Scrollbar ----------
        #https://blog.teclado.com/tkinter-scrollable-frames/
        borrarFrame('__main__.ScrollableFrame')
        frame = ScrollableFrame(root)
        print(cajaBusqueda.get())
        miscontactos = get_AZ_filtro(str(cajaBusqueda.get()))
        for x, y in miscontactos.items():
            Label(frame.scrollable_frame, text=f"   {x}", width=1000, borderwidth=1, relief='raised' , anchor="w", font=(fuenteCuerpo, 14)).pack(anchor="w", padx="2", pady="2", fill="x")
            for z in y:
                print(z[0])
                d = {'ID' : z[0]}
                Button(frame.scrollable_frame, text=f"{z[0]} - {z[1]} {z[2]} ", command=lambda c = z[0]: perfil(c), anchor="e", font=(fuenteCuerpo, 12)).pack(anchor="w", padx="20")
        
        frame.pack(pady="10", expand=True, fill='both')
    
    agregarContactoBoton = Button(root, text="Agregar Contacto", command=lambda: perfil(agregarContacto()[0]), anchor="e", font=(fuenteCuerpo, 12))
    buscarBoton = Button(root, text="Buscar", font=(fuenteTitulo, 10), command= grupoContactos)
    cajaBusqueda = Entry(root, font=(fuenteTitulo, 14))
    volverAtras()
    
    root.mainloop()

AbrirVentana()