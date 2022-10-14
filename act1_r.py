import numpy as np
import pandas as pd


def mi_func():
  print("Hola mundo")


mi_func()

#def colores(string_colores):
    #for x in string_colores:
        #if string_colores[x] == "-":

print ("Ingrese los colores separados por un - : ")
string_colores = input()

#print (string_colores)   

def colores(string_colores):
    x = string_colores.split("-")
    
    #print(x)
    
    length = len(x)
    result = ""
    
    for y in range(length):
        if x[y] == "Negro":
            result = result + "0"
        if x[y] == "Marron":
            result = result + "1"
        if x[y] == "Rojo":
            result = result + "2"
        if x[y] == "Naranja":
            result = result + "3"
        if x[y] == "Amarillo":
            result = result + "4"
        if x[y] == "Verde":
            result = result + "5"
        if x[y] == "Azul":
            result = result + "6"
        if x[y] == "Purpura":
            result = result + "7"
        if x[y] == "Gris":
            result = result + "8"
        if x[y] == "Blanco":
            result = result + "9"
        
    
    return result[0]+result[1]
    
    #Negro: 0, Marrón: 1, Rojo: 2, Naranja: 3, Amarillo: 4, Verde: 5, Azul: 6, Púrpura: 7, Gris: 8, Blanco: 9

print(colores(string_colores))

print ("Ingrese el año: ")
dato1 = input()
dato1 = int(dato1)


def bisiesto(dato):
    if (dato % 4 == 0) and (dato%100 != 0):
        res = "Bisiesto"
        return res
    elif (dato%100 == 0) and (dato%400 == 0):
        res = "Bisiesto"
        return res
    else :
        res = "No es bisiesto"
        return res

print(bisiesto(dato1))


def edad_planeta(edad,planeta):
    year_to_sec = 31557600
    
    edadTierra = edad/year_to_sec
    
    dicPlanetas = {
        "Mercurio":0.2408467,
        "Venus":0.61519726, 
        "Marte":1.8808158, 
        "Jupiter":11.862615, 
        "Saturno":29.447498, 
        "Urano":84.016846, 
        "Neptuno":164.79132 }
    
    if planeta == "Tierra":
        return round(edadTierra,2)
    else:
        return round(edadTierra/dicPlanetas[planeta],2)

edad_planeta(946100000,"Venus")

