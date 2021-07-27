import sqlite3

class QueryBase:
    def __init__(self, nombreDataBase):
        self.nombreDataBase = nombreDataBase
        self.conexion = sqlite3.connect(self.nombreDataBase)
        self.micursor = self.conexion.cursor()

    def crearTabla (self, nombreTabla):
        query = f"""
        CREATE TABLE {nombreTabla} (contactID INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT, apellido TEXT, phone TEXT, email TEXT);
        """
        self.micursor.execute(query)

    def insertarValores (self, nombreTabla, nombre, apellido = "", phone = "", email = ""):
        query = f"""
        INSERT INTO {nombreTabla} VALUES ( NULL , ? , ? , ? , ?);
        """
        self.micursor.execute(query,(nombre, apellido, phone, email))

    def buscarValor (self, nombreTabla, valor):
        query = f"""
        SELECT contactID, nombre, apellido FROM {nombreTabla}
        WHERE nombre LIKE ? OR apellido LIKE ? OR phone LIKE ? OR email LIKE ?;
        """
        self.micursor.execute(query,(valor, valor, valor, valor))
        return self.micursor.fetchall()

    def eliminarcontactID (self, nombreTabla, contactID):
        query = f"""
        DELETE FROM {nombreTabla}
        WHERE contactID = ?;
        """
        self.micursor.execute(query,( contactID, ))
        return self.micursor.fetchall()



