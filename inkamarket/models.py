import oracledb
oracledb.init_oracle_client(lib_dir=r"C:\instantclient_11_2\instantclient_11_2")
#import cx_Oracle

class Categorias:
    def __init__(self):
        self.miconexion = (oracledb.connect(user="system", password="pythonoracle", dsn="localhost/XE"))

    def alta(self, id, nombre):
        cursor = self.miconexion.cursor()
        try:
            sql = "INSERT INTO CATEGORIAS (ID_CATEGORIA,NOMBRE)VALUES(:P1,:P2)"
            cursor.execute(sql, (id, nombre))
            self.miconexion.commit()
        except Exception as error:
            print("error", error)
        return cursor

    def baja(self, id):
        cursor = self.miconexion.cursor()
        try:
            sql = "DELETE FROM CATEGORIAS WHERE ID_CATEGORIA=:P1"
            cursor.execute(sql, (id,))
            self.miconexion.commit()
        except Exception as error:
            print("error", error)
        return cursor

    def modificar(self, id, nombre):
        cursor = self.miconexion.cursor()
        try:
            sql = "UPDATE CATEGORIAS SET NOMBRE=:P2 WHERE ID_CATEGORIA=:P1"
            cursor.execute(sql, (nombre, id))
            self.miconexion.commit()
        except Exception as error:
            print("error", error)
        return cursor

    def consultar(self):
        cursor = self.miconexion.cursor()
        try:
            sql = "SELECT * FROM CATEGORIAS"
            cursor.execute(sql)
        except Exception as error:
            print("error", error)
        return cursor

class Productos:
    def __init__(self):
        self.miconexion = oracledb.connect(user="system", password="pythonoracle", dsn="localhost/XE")

    def alta(self, id, nombre, precio, id_cat):
        cursor = self.miconexion.cursor()
        try:

            #sql = "INSERT INTO PRODUCTOS (ID_PRO, NOMBRE, PRECIO, ID_CATEGORIA) VALUES (:P1, :P2, :P3, :P4)"
            #cursor.execute(sql, (id, nombre, precio, id_cat))
            cursor.callproc("ALTA_PRODUCTOS", [id, nombre, precio, id_cat])  # LLAMADA A ALTA_PROCEDURE
            self.miconexion.commit()
        except Exception as error:
            print("error", error)
        return cursor

    def baja(self, id):
        cursor = self.miconexion.cursor()
        try:
            #sql = "DELETE FROM PRODUCTOS WHERE ID_PRO = :P1"
            #cursor.execute(sql, (id,))
            cursor.callproc("BAJA_PRODUCTO", [id]) # LLAMADA A PROCEDURE "BAJA_PRODUCTO"
            self.miconexion.commit()
        except Exception as error:
            print("error", error)
        return cursor

    def consultar(self):
        cursor = self.miconexion.cursor()
        try:
            sql = "SELECT NOMBRE,FOTO FROM PRODUCTOS"
            cursor.execute(sql)
        except Exception as error:
            print("error", error)
        return cursor

class Clientes:
    def __init__(self):
        self.miconexion = oracledb.connect(user="system", password="pythonoracle", dsn="localhost/XE")

    def alta(self, dni, nombre, email, ciudad):
        cursor = self.miconexion.cursor()
        try:
            sql = "INSERT INTO CLIENTES VALUES(:P1,:P2,:P3,:P4)"
            cursor.execute(sql, (dni, nombre, email, ciudad))
            self.miconexion.commit()
        except Exception as error:
            print("error", error)
        return cursor

    def baja(self, dni):
        cursor = self.miconexion.cursor()
        try:
            sql = "DELETE FROM CLIENTES WHERE DNI=:P1"
            cursor.execute(sql, (dni,))
            self.miconexion.commit()
        except Exception as error:
            print("error", error)
        return cursor

    def modificar(self, dni, nombre, email, ciudad):
        cursor = self.miconexion.cursor()
        try:
            sql = "UPDATE CLIENTES SET NOMBRE=:P2, EMAIL=:P3, CIUDAD=:P4 WHERE DNI=:P1"
            cursor.execute(sql, (nombre, email, ciudad, dni))
            self.miconexion.commit()
        except Exception as error:
            print("error", error)
        return cursor

    def consultar(self):
        cursor = self.miconexion.cursor()
        try:
            sql = "SELECT * FROM CLIENTES"
            cursor.execute(sql)
        except Exception as error:
            print("error", error)
        return cursor

class Empleados:
    def __init__(self):
        self.miconexion = oracledb.connect(user="system", password="pythonoracle", dsn="localhost/XE")

    def consultar(self):
        cursor = self.miconexion.cursor()
        try:
            sql = "SELECT * FROM EMPLEADOS"
            cursor.execute(sql)
        except Exception as error:
            print("error", error)
        return cursor

class Proveedores:
    def __init__(self):
        self.miconexion = oracledb.connect(user="system", password="pythonoracle", dsn="localhost/XE")

    def consultar(self):
        cursor = self.miconexion.cursor()
        try:
            sql = "SELECT * FROM PROVEEDORES"
            cursor.execute(sql)
        except Exception as error:
            print("error", error)
        return cursor

class Contactos:
    def __init__(self):
        self.miconexion = oracledb.connect(user="system", password="pythonoracle", dsn="localhost/XE")

    def insertar(self, id, nombre, email, mensaje,tipo):
        cursor = self.miconexion.cursor()
        try:
            #sql = "INSERT INTO CONTACTOS VALUES(:P1,:P2,:P3,:P4)"
            #cursor.execute(sql, (id, nombre, email, mensaje))
            cursor.callproc("INSERTAR_CONTACTO", [id, nombre, email, mensaje, tipo])   # <-- procedimiento

            self.miconexion.commit()
        except Exception as error:
            print("error", error)

        return cursor


