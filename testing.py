import tkinter as tk
import main
from tkinter import ttk

agendaventana= tk.Tk()
agendaventana.title("Agenda")


lbl= tk.Label(text="Agenda", font=("Arial Rounded MT Bold", 14))

lbl.grid(row="0", column="1")


def agregarContacto (nombre = "", apellido = "", phone = "", email=""):
    print(f" se ha guardado a {nombre, apellido, phone}")

#buscador
etiquetaBuscar= tk.Label(text="Buscar", font=("calibri", 12))
etiquetaBuscar.grid(column=0, row=1, sticky=tk.EW, padx=5, pady=5)
buscador= tk.Entry(font=("calibri", 12))
buscador.grid(column=1, row=1, sticky=tk.EW, padx=8, pady=5)
bsearch=tk.Button(text="SEARCH",)
bsearch.grid(row="1", column="6")

# Entry de nombre.
txtNombre = ttk.Entry()
txtNombre.grid(row="2", column="1")
lbl2= tk.Label(text="Nombre", font=("calibri", 12))
lbl2.grid(row="2", column="0")

# Entry de apellido.
txtApellido = ttk.Entry()
txtApellido.grid(row="3", column="1")
lbl3= tk.Label(text="Apellido", font=("calibri", 12))
lbl3.grid(row="3", column="0")

# Entry de numero de teléfono.
validarComando = agendaventana.register(main.caracterValido)
txtPhone = ttk.Entry(agendaventana, validate="key", validatecommand=(validarComando, "%S"))
txtPhone.grid(row="4", column="1")
lbl3= tk.Label(text="Telefono", font=("calibri", 12))
lbl3.grid(row="4", column="0")

# Entry de email.
txtEmail = ttk.Entry()
txtEmail.grid(row="5", column="1")
lbl3= tk.Label(text="Email", font=("calibri", 12))
lbl3.grid(row="5", column="0")

def interfaz_agregarContactos ():
    main.agregarContacto(nombre=txtNombre.get(), apellido=txtApellido.get(), phone=txtPhone.get(), email=txtEmail.get())

#botones
bt1= tk.Button(text="AÑADIR CONTACTO", command=interfaz_agregarContactos)
bt1.grid(row="2", column="6")
bt2= tk.Button(text="BORRAR CONTACTO")
bt2.grid(row="3", column="6")
bt3= tk.Button(text="ACTUALIZAR CONTACTO")
bt3.grid(row="4", column="6")
bt4= tk.Button(text="GUARDAR")
bt4.grid(row="7", column="1")
bt5= tk.Button(text="DESCARTAR")
bt5.grid(row="8", column="1")


#print(main.get_AZ())


agendaventana.resizable(0,0)
agendaventana.mainloop()

