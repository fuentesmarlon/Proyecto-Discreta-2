# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 01:50:57 2017

@author: Alejandro Vásquez, Marlon Fuentes, Davis
"""

from proyecto2 import *



while True:
    print ("Bienvenido!"+"\n"
               +"1. Realizar una reservacion nueva \n"
               +"2. Eliminar una reservacion creada \n"
               +"3. Crear un vuelo\n"
               +"4. Eliminar vuelo\n"
               +"5. Modificar hora de vuelo\n"
               +"6. Modificar numero de vuelo\n"
               +"7. Modificar numero de asientos disponibles\n"
               +"8. Consulta de Conexiones\n"
               +"9. Salir")
        
    resp = int(input("¿Que desea hacer?\n"))
        
    if resp ==1:
        cod_vuelo=input("Porfavor ingrese el codigo de vuelo para crear una reserva\n")
        reserva = hacer_reserva(cod_vuelo)
        if reserva ==True:
            print("\nLa reservacion se ha realizado con exito\n")
            log("Reservacion en el vuelo " + cod_vuelo)
        elif reserva == False:
            print("\nReservacion fallida. Ya no quedan asientos disponibles en este vuelo\n")
        else:
            print("\nIngrese un vuelo existente\n")
        

    if resp ==2:
        cod_vuelo = input("Porfavor ingrese el codigo de vuelo para eliminar la reserva\n")
        eliminar = eliminar_reserva(cod_vuelo)
        if eliminar == True:
            print("\nLa reservacion ha sido eliminada con exito\n")
            log("Se elimino una reserva del vuelo " + cod_vuelo)
        else:
            print("\nIngrese un vuelo existente\n")
        

    if resp ==3:
        aero= input("Ingrese nombre de la aerolinea:\n")
        origen = input("Ingrese ciudad de origen:\n")
        destino= input("Ingrese ciudad de destino:\n")
        codigo= input("Ingrese el codigo del vuelo:\n")
        salida= input("Ingrese la hora de salida en formato militar (e.g.: 16:30):\n")
        durar = input("Ingrese la duracion del vuelo:\n")
        llegada = input("Ingrese hora de llegada:\n")
        asientos = input("Ingrese numero de asientos disponibles:\n")
        agregar_vuelo(aero,origen,destino,codigo, salida,durar,llegada,asientos)
        print("Vuelo Guardado exitosamente")
        log("Se registro un nuevo vuelo, con código "+ codigo)
        
        
    if resp ==4:
        cod = input("Ingrese el codigo del vuelo que desea eliminar:\n")
        comp = eliminar_vuelo(cod)
        if comp == True:
            print("Vuelo eliminado")
            log("Se elimino "+ cod)
        else:
            print("\nIngrese un vuelo existente\n")
        
        
    if resp ==5:
        numeroV = input("Ingrese el codigo de vuelo a modificar\n")
        salida= input("Ingrese la nueva hora de salida en formato militar (e.g.: 16:30):\n")
        comp = mod_hora(numeroV,salida)
        if comp == True:
            print("Horas cambiadas exitosamente")
            log("Se cambió la hora de salida del vuelo "+ numeroV + "a las " + salida)
        else:
            print("\nIngrese un vuelo existente o una hora valida\n")
        

    if resp ==6:
        numeroV = input("Ingrese el codigo de vuelo a modificar\n")
        numeroN = input("Ingrese el nuevo numero de vuelo:\n")
        comp = mod_num_vuelo(numeroV,numeroN)
        if comp == True:
            print("Numero de vuelo cambiado exitosamente")
            log("Se cambio el vuelo "+numeroV + "al nuevo codigo "+numeroN)
        else:
            print("\nIngrese un vuelo existente\n")
        
        
    if resp ==7:
        numeroV= input("Ingresar el codigo de vuelo:\n")
        numeroA= input("Ingresar el nuevo numero de asientos disponibles:\n")
        comp = mod_asientos_disp(numeroV,numeroA)
        if comp == True:
            print("Numero de asientos cambiados exitosamente")
            log("Se cambio el numero de asientos disponibles del vuelo " + numeroV + "a " + numeroA)
        

    if resp ==8:
        ciudad1 = input("Ingrese la primer ciudad para buscar conexion:\n")
        ciudad2 = input("Ingrese la segunda ciudad a conectar:\n")
        conexiones, tiempo = consulta_conexion(ciudad1,ciudad2)
        if len(conexiones) == 2:
            print("La ruta recomendada es tomando los vuelos " + conexiones[0] + " y "+ conexiones[1] +", en un tiempo de " + tiempo + " horas")
            log("Se consulto una conexion entre " + ciudad1 + " y " +ciudad2)
        elif len(conexiones) == 1:
            print("La ruta recomendada es tomando el vuelo " + conexiones[0] +", en un tiempo de " + tiempo + " horas")
            log("Se consulto una conexion entre " + ciudad1 + " y " + ciudad2)
        else:
            print("No existe una conexion entre esas dos ciudades o esas ciudades no se encuentran en la base de datos")
        
        
    if resp ==9:
        salir()
        break
        

        


