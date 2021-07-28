import tkinter as tk
import main
from tkinter import ttk

agendaventana= tk.Tk()
agendaventana.geometry("400x600")

lbl= tk.Label(text="Agenda", font=("Arial Rounded MT Bold", 14))

lbl.pack()

def agregarContacto (nombre = "", apellido = "", phone = "", email = ""):
    print(f" se ha guardado a {nombre, apellido, phone}")


# Entry de nombre.
txtNombre = ttk.Entry()
txtNombre.pack()

# Entry de apellido.
txtApellido = ttk.Entry()
txtApellido.pack()

# Entry de numero de teléfono.
validarComando = agendaventana.register(main.caracterValido)
txtPhone = ttk.Entry(agendaventana, validate="key", validatecommand=(validarComando, "%S"))
txtPhone.pack()

# Entry de email.
txtEmail = ttk.Entry()
txtEmail.pack()

def interfaz_agregarContactos ():
    main.agregarContacto(nombre=txtNombre.get(), apellido=txtApellido.get(), phone=txtPhone.get(), email=txtEmail.get())

bt1= tk.Button(text="AÑADIR CONTACTO", command=interfaz_agregarContactos)
bt1.pack()
bt2= tk.Button(text="BORRAR CONTACTO")
bt2.pack()
bt3= tk.Button(text="ACTUALIZAR CONTACTO")
bt3.pack()
bt4= tk.Button(text="GUARDAR" , command= lambda:(main.cerrarGuardar(True)))
bt4.pack()
bt5= tk.Button(text="MOSTRAR" , command= print(main.get_AZ()))
bt5.pack()
bt6= tk.Button(text="SALIR")
bt6.pack()

#print(main.get_AZ())







agendaventana.mainloop()

