# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 09:39:07 2017

@author: 
"""

from csv import *
import numpy as np

a = []
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
for i in range(len(a)):
    a[i][7] = int(a[i][7])

np_vuelos = np.array(a)


def hacer_reserva(cod_vuelo):
    for i in range(len(a)):
        if a[i][3]== cod_vuelo:
            seats = a[i][7]
            if seats == 0:
                return False
            else:
                seats -=1
                a[i][7] = seats
                return True

def eliminar_reserva(cod_vuelo):
    for i in range(len(a)):
        if a[i][3]== cod_vuelo:
            seats = a[i][7]
            if seats == 200:
                return False
            else:
                seats +=1
                a[i][7] = seats
                return True
    
def eliminar_vuelo(cod_vuelo):
    for i in range(len(a)):
        if a[i][3]== cod_vuelo:
            temp = a[:i]+a[i+1:]
            return temp

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
        
        
def mod_num_vuelo(cod_vuelo, new_cod_vuelo):
    for i in range(len(a)):
        if a[i][3] == cod_vuelo:
            a[i][3] = new_cod_vuelo
             
def mod_asientos_disp(cod_vuelo, new_asientos):
    for i in range(len(a)):
        if a[i][3] == cod_vuelo:
            a[i][7] = int(new_asientos)
            
def actualizar_csv():
    with open('vuelos.csv','w') as csvfile:
        guardar = writer(csvfile)
        guardar.writerow(["Airline", "Origin", "Destination", "Flight", "Departure", "Duration", "Arrival","Seats"])
        for i in a:
            guardar.writerow(i)
    csvfile.close()
