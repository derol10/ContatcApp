from _typeshed import Self
import sqlite3

class QueryBase:
    def __init__(self):
        pass
               

    def conectarDB (self, nombreDataBase):
        self.nombreDataBase = nombreDataBase
        self.conexion = sqlite3.connect(self.nombreDataBase)
        self.micursor = self.conexion.cursor()

    def crearTabla (self, nombreTabla):
        self.nombreTabla = nombreTabla
        query = """
        CREATE TABLE ? (nombre TEXT, apellido TEXT, phone TEXT, e-mail TEXT)
        """
        self.micursor.execute(query,(nombreTabla,))

    