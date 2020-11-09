#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#xxxxxxxxxxx                       xxxxxxxxxxxxx
#x   Universidad del Valle de Guatemala        x
#x   Proyecto Matematica Discreta              x
#x   6-11-2020                                 x
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#x   Carlos Alberto Raxtum  19721              x
#x   Abraham Gutierrez      19                 x
#x   Juan Manuel Marroquin  19845              x
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

#!/usr/bin/python3
# Write Python3 code here
import sys
from decimal import Decimal
import math
import msvcrt # getch()
import os # clear console
import re # expressions regulars

def pedirNumeroEntero(): #Funcion para ingresar solo numeros enteros
 
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Introduce un numero entero: "))
            correcto=True
        except ValueError:
            print('Error, introduce un numero entero')
     
    return num
 
salir = False
opcion = 0


def primo(num): #funcion para verificar Num primos
    contador = 0
    if num < 2:
        return False
    
    for i in range (2, num):
        if num % i == 0:
            return False
        
    return True

#algoritmo de euclides para el mcd
def mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

#algoritmo de euclides extendido para encontrar el inverso multiplicativo de dos numeros
def inverso_multi(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi
    
    while e > 0:
        temp1 = temp_phi/e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2
        
        x = x2- temp1* x1
        y = d - temp1 * y1
        
        x2 = x1
        x1 = x
        d = y1
        y1 = y
    
    if temp_phi == 1:
        return d + phi

#funcion que encripta un mensaje
def encriptar():
    return 1

#funcion que desencripta el mensaje
def desencriptar():
    return 0

# funcion que imprime las llaves publicas y privadas
def verKeys():
    return 2

print ("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n")
print ("x     Bienvenido a nuestro proyecto                                                                 x")
print ("x     A continuacion se le pediran dos valores primos para generar su clave publica y privada       x\n")
print ("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n")


a = pedirNumeroEntero()
if primo(a) == True:
    Val1 = a;
    print(Val1)
else:
    print ("El numero (a) no es primo, vuelva a iniciar el programa\n")
    sys.exit() 

b = pedirNumeroEntero()
if primo(b) == True:
    Val2 = b;
    print(Val2)
else:
    print ("El numero (b) no es primo, vuelva a iniciar el programa\n")
    sys.exit() 

print ("a iniciado satisfactoriamente los dos valores\n")
 
while not salir:
 
    print ("1. Encriptar")
    print ("2. Desencriptar")
    print ("3. Ver llaves publicas y privadas")
    print ("4. Salir")  
    print ("Elige una opcion")
 
    opcion = pedirNumeroEntero()
 
    if opcion == 1:
        print ("Opcion 1")
        gcd()
    elif opcion == 2:
        print ("Opcion 2")
    elif opcion == 3:
        print("Opcion 3")
    elif opcion == 4:
        salir = True
    else:
        print ("Introduce un numero entre 1 y 3")
 
print ("Fin")
