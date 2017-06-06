
from modulo import *

def menu():
    resp = 0
    while resp==0:
        print ("Bienvenido!"+"\n"
               +"1. Realizar una reservacion nueva \n"
               +"2. Eliminar una reservacion creada \n"
               +"3. Realizar vuelo\n"
               +"4. Eliminar vuelo\n"
               +"5. Modificar hora de vuelo\n"
               +"6. Modificar numero de vuelo\n"
               +"7. Modificar numero de asientos disponibles\n "
               + "8. Disponibilidad de Conexiones\n"
               +"9. Agregar Conexiones\n"
               +"10. Eliminar Conexiones\n")
        resp = input("Que desea hacer?")
    if resp ==1:
        cod_vuelo=raw_input("Porfavor ingrese el codigo de vuelo para crear una reserva")
        hacer_reserva(cod_vuelo)
        actualizar_csv()
        print("La reservacion se ha realizado con exito\n")
        log("\nnueva reservacion")
        menu()

    if resp ==2:
        cod_vuelo = raw_input("Porfavor ingrese el codigo de vuelo para eliminar la reserva\n")
        eliminar_reserva(cod_vuelo)
        actualizar_csv()
        print("La reservacion ha sido eliminada con exito\n")
        log("\nEliminar Reservacion")
        menu()

    if resp ==3:
        aero= raw_input("Ingrese nombre de la aerolina:\n")
        origen = raw_input("Ingrese ciudad de origen:\n")
        destino=raw_input("Ingrese ciudad de destino:\n")
        codigo=raw_input("Ingrese el codigo deseado para el vuelo:\n")
        salida= raw_input("Ingrese la hora de salida (formato militar):\n")
        durar = raw_input("Ingrese la duracion del vuelo:\n")
        llegada = raw_input("Ingrese hora de llegada:\n")
        asientos = input("Ingrese numero de asientos ya reservados:\n")
        agregar_vuelo(aero,origen,destino,codigo, salida,durar,llegada,asientos)
        actualizar_csv()
        print("Vuelo Guardado exitosamente")
        log("\nNuevo Vuelo")
        menu()
    if resp ==4:
        cod = raw_input("Ingrese el codigo del vuelo que desea eliminar:\n")
        eliminar_vuelo(cod)
        actualizar_csv()
        print("Vuelo eliminado :(")
        log("\nEliminar Vuelo")
        menu()
    if resp ==5:
        numeroV = raw_input("Ingrese el codigo de vuelo a modificar")
        salida=raw_input("Ingrese la nueva hora de salida:\n")
        mod_hora(numeroV,salida)
        actualizar_csv()
        print("Horas cambiadas exitosamente!")
        log("\nCambiar horas")
        menu()

    if resp ==6:
        numeroV = raw_input("Ingrese el codigo de vuelo a modificar")
        numeroN=raw_input("Ingrese el nuevo numero de vuelo:\n")
        mod_num_vuelo(numeroV,numeroN)
        actualizar_csv()
        print("Numero de vuelo cambiado exitosamente")
        log("\nNuevo numero de vuelo")
        menu()
    if resp ==7:
        numeroV=raw_input("Ingresar el codigo de vuelo:\n")
        numeroA= input("Cuantos asientos nuevos?:\n")
        mod_asientos_disp(numeroV,numeroA)
        actualizar_csv()
        print("Numero de asientos cambiados exitosamente")
        log("\nModificacion asientos\n")
        menu()
#AQUI COMIENZA LO FALSO
    #-------------------------------------------------------------------------------------
    #YOU ARE ABOUT TO WITNESS THE STRENGTH OF STREET KNOWLEDGE
    if resp ==8:
        ciudad1 = raw_input("Ingrese la primer ciudad para buscar conexion:\n")
        ciudad2 = raw_input("Ingrese la segunda ciudad a conectar:\n")
        conexion = disp_conexiones(ciudad1,ciudad2)
        log("Descubrir Conexiones")
        print("Estas son las conexiones disponibles"+conexion)
        menu()
    if resp ==9
        ciudad1=raw_input("Ingrese la primera ciudad para una nueva conexion:\n")
        ciudad2=raw_input("Ingrese la segunda ciudad para una nueva conexion:\n")
        conexionN = nueva_conexion(ciudad1, ciudad2)
        log("\nNueva Conexion")
        print("Nueva Conexion Guardada con exito")
        menu()
    if resp ==10:
        ciudad1 = raw_input("Ingrese la ciudad1 para eliminar su conexion:\n")
        ciudad2= raw_input("Ingrese la ciudad2 para eliminar su conexion:\n")
        eliminar_conexion(ciudad1,ciudad2)
        log("\nEliminar Conexion")
        print("La conexion fue eliminada")
    else:
        print("Porfavor Ingrese un numero correcto")
        log("\nTe COnFunDIsTe wEEEE xDxDxD")
        menu()

menu()