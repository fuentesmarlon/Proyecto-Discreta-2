
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
               +"7. Modificar numero de asientos disponibles\n ")
        resp = input("Que desea hacer?")
    if resp ==1:
        cod_vuelo=raw_input("Porfavor ingrese el codigo de vuelo para crear una reserva")
        hacer_reserva(cod_vuelo)
        actualizar_csv()
        print("La reservacion se ha realizado con exito\n")
        log("nueva reservacion")
        menu()

    if resp ==2:
        cod_vuelo = raw_input("Porfavor ingrese el codigo de vuelo para eliminar la reserva\n")
        eliminar_reserva(cod_vuelo)
        actualizar_csv()
        print("La reservacion ha sido eliminada con exito\n")
        log("Eliminar Reservacion")
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
        log("Nuevo Vuelo")
        menu()
    if resp ==4:
        cod = raw_input("Ingrese el codigo del vuelo que desea eliminar:\n")
        eliminar_vuelo(cod)
        actualizar_csv()
        print("Vuelo eliminado :(")
        log("Eliminar Vuelo")
        menu()
    if resp ==5:
        numeroV = raw_input("Ingrese el codigo de vuelo a modificar")
        salida=raw_input("Ingrese la nueva hora de salida:\n")
        mod_hora(numeroV,salida)
        actualizar_csv()
        print("Horas cambiadas exitosamente!")
        log("Cambiar horas")
        menu()

    if resp ==6:
        numeroV = raw_input("Ingrese el codigo de vuelo a modificar")
        numeroN=raw_input("Ingrese el nuevo numero de vuelo:\n")
        mod_num_vuelo(numeroV,numeroN)
        actualizar_csv()
        print("Numero de vuelo cambiado exitosamente")
        log("Nuevo numero de vuelo")
        menu()
    if resp ==7:
        numeroV=raw_input("Ingresar el codigo de vuelo:\n")
        numeroA= input("Cuantos asientos nuevos?:\n")
        mod_asientos_disp(numeroV,numeroA)
        actualizar_csv()
        print("Numero de asientos cambiados exitosamente")
        log("Modificacion asientos")
        menu()

    else:
        print("Porfavor Ingrese un numero correcto")
        log("Te COnFunDIsTe wEEEE xDxDxD")
        menu()

menu()