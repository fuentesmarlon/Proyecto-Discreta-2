# -*- coding: utf-8 -*-
"""

@author: Alejandro Vásquez, Marlon Fuentes, Davis
"""

from csv import *


a = []
registro = []

with open('vuelos.csv') as csvfile:
    vuelos = reader(csvfile, delimiter=',',quotechar= '|')
    for row in vuelos:
        a.append(row)
csvfile.close()
n = len(a)
k = 0

while k < n:
    if a[k] == []:
        a = a[:k]+a[k+1:]
        n-=1
    k+=1
a = a[1:]        
#for i in range(len(a)):
#    a[i][7] = int(a[i][7])

def get_duration(cod_vuelo):
    for i in range(len(a)):
        if a[i][3] == cod_vuelo:
            time = a[i][5]
            mins = int(time[0:time.index(":")])*60 + int(time[time.index(":")+1:])
            return mins
        
def get_time(time):
    return int(time[0:time.index(":")])*60+int(time[time.index(":")+1:])

def convert_time(time):
    h = int(time/60)
    m = time-h*60
    h = str(h)
    m = str(m)
    if len(h)==1:
        h = "0"+h
    if len(m)==1:
        m += "0"
    return h+":"+m

def get_time_between_flights(vuelo1,vuelo2):
    for i in range(len(a)):
        if a[i][3] == vuelo1:
            t1 = get_time(a[i][6])
        if a[i][3] == vuelo2:
            t2 = get_time(a[i][4])
    time = t2-t1
    if time<0:
        time+=1440
    return time

def consulta_conexion(ciudad1,ciudad2):
    time = 10000000000000
    time_comp = 0
    lista_conexion = []
    for i in range(len(a)):
        if a[i][1] == ciudad1 and a[i][2] == ciudad2:
            time_comp = get_time(a[i][5])
            if time_comp < time:
                lista_conexion= [a[i][3]]
                time = time_comp
    for i in range(len(a)):
        if a[i][1]==ciudad1:
            for j in range(len(a)):
                if a[j][1] == a[i][2] and a[j][2] == ciudad2:
                    time_comp = get_time_between_flights(a[i][3],a[j][3]) + get_time(a[i][5]) + get_time(a[j][5])
                    if time_comp < time:
                        time = time_comp
                        lista_conexion= [a[i][3]]
                        lista_conexion.append(a[j][3])                    
    return lista_conexion, convert_time(time)

def hacer_reserva(cod_vuelo):
    for i in range(len(a)):
        if a[i][3]== cod_vuelo:
            seats = int(a[i][7])
            if seats == 0:
                return False
            else:
                seats -=1
                a[i][7] = str(seats)
                return True

def eliminar_reserva(cod_vuelo):
    for i in range(len(a)):
        if a[i][3]== cod_vuelo:
            seats = int(a[i][7])
            seats +=1
            a[i][7] = str(seats)
            return True
    return False
            
def eliminar_vuelo(cod_vuelo):
    for i in range(len(a)):
        if a[i][3]== cod_vuelo:
            del a[i]
            return True
    return false
        

def agregar_vuelo(aerolinea,origen,destino,cod_vuelo,hora_salida,duracion,hora_llegada,asientos):
    a.append([aerolinea,origen,destino,cod_vuelo,hora_salida,duracion,hora_llegada,asientos])
    
def dif_tiempo(time1,time2):
    h1 = int(time1[0:time1.index(":")])
    m1 = int(time1[time1.index(":")+1:])
    h2 = int(time2[0:time2.index(":")])
    m2 = int(time2[time2.index(":")+1:])
    h = h1+h2
    m = m1 + m2
    if m >=60:
        h += 1
        m -= 60
    if h >= 24:
        h -= 24
    h = str(h)
    if len(h) == 1:
        h = "0"+h
    m=str(m)
    if len(m) == 1:
        m = m+"0"
    return str(h)+":"+str(m)

def mod_hora(cod_vuelo,new_hora):
    for i in range(len(a)):
        if a[i][3]== cod_vuelo:
            a[i][4] = new_hora
            a[i][6] = dif_tiempo(new_hora, a[i][5])
            return True
    return False
        
        
def mod_num_vuelo(cod_vuelo, new_cod_vuelo):
    for i in range(len(a)):
        if a[i][3] == cod_vuelo:
            a[i][3] = new_cod_vuelo
            return True
    return False
             
def mod_asientos_disp(cod_vuelo, new_asientos):
    for i in range(len(a)):
        if a[i][3] == cod_vuelo:
            a[i][7] = new_asientos
            return True
    return False
            
def actualizar_csv():
    with open('vuelos.csv','w') as csvfile:
        guardar = writer(csvfile)
        guardar.writerow(["Airline", "Origin", "Destination", "Flight", "Departure", "Duration", "Arrival","Seats"])
        for i in a:
            guardar.writerow(i)
    csvfile.close()
    
def log(string):
    registro.append(string)
    
def actualizar_log():
    file = open("log.txt", "w")
    for i in registro:
        file.write(i)
        
def salir():
    print("Gracias por utilizar este servicio")
    actualizar_csv()
