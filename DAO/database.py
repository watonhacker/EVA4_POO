import mysql.connector


class DAO():
    conexion = None

    def __init__(self):
        self.conexion = mysql.connector.connect(
            host="uh1.hnc.cl",
            port=3306,
            user="mobalzen_keyzen",
            password="keyzencl123",
            db="mobalzen_inacap"
        )

    def crearEncomienda(self, remitente, destinatario, peso, alto, largo, ancho, valordeclarado):

        try:
            cursor = self.conexion.cursor()
            cursor.execute("INSERT INTO encomienda (remitente, destinatario, peso, alto, largo, ancho, valordeclarado) VALUES ('{}', '{}', {}, {}, {}, {}, {})".format(remitente, destinatario, peso, alto, largo, ancho, valordeclarado))
            self.conexion.commit()
        except Exception:
            raise

    def leerEncomiendas(self):
        try:
            cursor = self.conexion.cursor()
            cursor.execute("SELECT * FROM encomienda")
            resultado = cursor.fetchall()
            for res in resultado:
                print("N°{}:\n Datos personales: Remitente: {}, Destinatario: {} \n Datos Encomienda: {}kg, Alto: {}cm, Largo: {}cm, Ancho: {}cm, Valor: ${:,.0f}".format(
                    res[0], res[1], res[2], res[3], res[4], res[5], res[6], res[7]).replace(',','.')
                )
                print("-----------------------------")

        except Exception:
            raise

    def leerEncomienda(self, id):
        try:
            cursor = self.conexion.cursor()
            cursor.execute("SELECT * FROM encomienda WHERE encomienda.id = {}".format(id))
            encomienda = cursor.fetchone()
            return encomienda
        except Exception:
            raise
    def actualizarEncomienda(self, id, remitente, destinatario, peso, alto, largo, ancho, valordeclarado):
        try:
            cursor = self.conexion.cursor()
            cursor.execute("UPDATE encomienda SET remitente = '{}', destinatario = '{}', peso = {}, alto = {}, largo = {}, ancho = {}, valordeclarado = {} WHERE id = {}".format(remitente, destinatario, peso, alto, largo, ancho, valordeclarado, id))
            self.conexion.commit()
        except Exception:
            raise
    def eliminarEncomienda(self, id):

        try:
            cursor = self.conexion.cursor()
            cursor.execute("DELETE FROM encomienda WHERE id = {}".format(id))
            self.conexion.commit()
        except Exception:
            raise



