from EVA4_POO.vistas.Vistas import Vista

while True:

    print("Menú Principal")
    print("1.Creación de encomiendas")
    print("2.Consulta de encomiendas")
    print("3.Consulta de encomienda particular")
    print("4.Actualización de estado de encomiendas")
    print("5.Eliminación de encomiendas")
    print("6.Salir")

    opcion = int(input("Ingrese una opcion: "))


    DAOVista = Vista()

    if opcion == 1:
        DAOVista.datosCrearEncomienda()
    elif opcion == 2:
        DAOVista.traerEncomiendas()
    elif opcion == 3:
        DAOVista.traerEncomienda()
    elif opcion == 4:
        DAOVista.datosActualizarEncomienda()
    elif opcion == 5:
        DAOVista.idEliminarEncomienda()
    else:
        break

