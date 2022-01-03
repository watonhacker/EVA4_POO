from EVA4_POO.DAO.database import DAO

class Vista():

    def __init__(self):
        self.DAOAccess = DAO()

    def validarEntero(self, pregunta):
        while True:
            try:
                numero = int(input(pregunta))
            except ValueError:
                print("Debes escribir un número.")
                continue

            if type(numero) == float:
                print("Debes escribir un numero entero")
                continue

            if numero < 0:
                print("Debes escribir un número positivo.")
                continue

            else:
                break
        return numero

    def validarFloat(self, pregunta):
        while True:
            try:
                numero = float(input(pregunta))
            except ValueError:
                print("Debes escribir un número.")
                continue

            if numero < 0:
                print("Debes escribir un número positivo.")
                continue

            else:
                break
        return numero

    def datosCrearEncomienda(self):
        print("Formulario de creación de Encomienda:")
        remitente = input("Ingrese el remitente: ")
        destinatario = input("Ingrese el destinatario: ")
        peso = self.validarFloat("Ingrese el peso: ")
        alto = self.validarFloat("Ingrese el alto: ")
        largo = self.validarFloat("Ingrese el largo: ")
        ancho = self.validarFloat("Ingrese el ancho: ")
        valordeclarado = self.validarEntero("Ingrese el valor declarado: ")

        self.DAOAccess.crearEncomienda(remitente, destinatario, peso, alto, largo, ancho, valordeclarado)
        print("La encomienda ha sido creada con éxito")

    def idEliminarEncomienda(self):
        idEliminar = int(input(("Ingrese el id de la encomienda a eliminar: ")))
        self.DAOAccess.eliminarEncomienda(idEliminar)

    def datosActualizarEncomienda(self):
        idActualizar = self.validarEntero("Ingrese el id de la encomienda a actualizar: ")
        existeEncomienda = self.DAOAccess.leerEncomienda(idActualizar)

        while existeEncomienda == None:
            print("La encomienda N°{} no ha sido encontrada".format(idActualizar))
            idActualizar = self.validarEntero("Ingrese el id de la encomienda a actualizar: ")
            existeEncomienda = self.DAOAccess.leerEncomienda(idActualizar)

        remitente = input("Ingrese el remitente: ")
        destinatario = input("Ingrese el destinatario: ")
        peso = self.validarFloat("Ingrese el peso: ")
        alto = self.validarFloat("Ingrese el alto: ")
        largo = self.validarFloat("Ingrese el largo: ")
        ancho = self.validarFloat("Ingrese el ancho: ")
        valorDeclarado = self.validarEntero("Ingrese el valor declarado: ")
        self.DAOAccess.actualizarEncomienda(idActualizar, remitente, destinatario, peso, alto, largo, ancho, valorDeclarado)
        print("La encomienda {} ha sido actualizada".format(idActualizar))


    def traerEncomiendas(self):
        print("Buscando todas las ecomiendas...")
        return self.DAOAccess.leerEncomiendas()

    def traerEncomienda(self):
        idEncomienda = self.validarEntero("Ingrese el id de la encomienda: ")
        encomiendaEncontrada = self.DAOAccess.leerEncomienda(idEncomienda)
        if encomiendaEncontrada == None:
            print("No se ha encontrado la encomienda N°{}".format(idEncomienda))
        else:
            print(
                "N°{}:\n Datos personales: Remitente: {}, Destinatario: {} \n Datos Encomienda: {}kg, Alto: {}cm, Largo: {}cm, Ancho: {}cm, Valor: ${:,.0f}".format(
                    encomiendaEncontrada[0], encomiendaEncontrada[1], encomiendaEncontrada[2], encomiendaEncontrada[3]
                    , encomiendaEncontrada[4], encomiendaEncontrada[5], encomiendaEncontrada[6], encomiendaEncontrada[7]).replace(',', '.')
                )

            print("-----------------------------------")
