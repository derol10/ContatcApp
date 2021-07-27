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

    def insertarValores (self, nombreTabla, nombre = "", apellido = "", phone = "", email = ""):
        if nombre != "" or apellido != "" or phone != "" or email !="":
            query = f"""
            INSERT INTO {nombreTabla} VALUES ( NULL , ? , ? , ? , ?);
            """
            self.micursor.execute(query,(nombre, apellido, phone, email))
            
            return "Contacto guardado exitosamente."
        else:
            return ("Se han descartado los cambios")

    def buscarValor (self, nombreTabla, valor):
        query = f"""
        SELECT * FROM {nombreTabla}
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

    def buscarParam_byContactID (self, nombreTabla, contactID):
        query = f"""
        SELECT * FROM {nombreTabla}
        WHERE contactID = ?;
        """
        self.micursor.execute(query,(contactID, ))
        return self.micursor.fetchall()


    def actualizar_contacto(self, nombreTabla, contactID, nombre = "", apellido ="", phone = "", email = ""):
        resultado = self.buscarParam_byContactID(nombreTabla, contactID)
        tuplavieja = resultado[0]
        tuplanueva = (contactID, nombre, apellido, phone, email)
        parametros = ("concactID", "nombre", "apellido", "phone", "email")

        for i in range(1,5):
            if tuplavieja[i] != tuplanueva[i] and tuplanueva[i] != "":
                query= f"""
                UPDATE {nombreTabla}
                SET {parametros[i]} = ?
                WHERE contactID = ? ;
                """
                
                self.micursor.execute(query,(tuplanueva[i], contactID))

