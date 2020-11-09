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
import random
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

#funcion para el inverso multiplicativo
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

#algoritmo de euclides extendido para encontrar el inverso multiplicativo de dos numeros
def inverso_multi(e, phi):
    g, x, y = egcd(e, phi)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % phi

#generar llaves publicas y privadas
def keypair(p, q):
    if not (primo(p) and primo(q)):
        raise ValueError('Los numeros tienen que ser numeros primos.')
    elif p == q:
        raise ValueError('"p" y "q" no pueden ser iguales')
    #n = pq
    n = p * q

    #Phi is the totient of n
    phi = (p-1) * (q-1)

    #Choose an integer e such that e and phi(n) are coprime
    e = random.randrange(1, phi)

    #usar el algoritm de euclides para verificar que e y phi(n) son coprimos
    g = mcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = mcd(e, phi)

    
    #encontrar el inverso multiplicativo para generar las claves privadas
    d = inverso_multi(e, phi)
    
    
    #regesar las claves publicas y privadas
    #clave publica (e,n) y clave privada (d,n)
    return ((e, n), (d, n))

#funcion que encripta un mensaje
def encriptar(pk, mensaje):
    #desempacar las llaves en componentes
    key, n = pk
    #convertir cada letra del mensaje a numeros basados en using a^b mod m
    cipher = [(ord(char) ** key) % n for char in mensaje]
    #regresar un array de bytes
    return cipher

#funcion que desencripta el mensaje
def desencriptar(pk, ciphertext):
    #desempacar las llaves en componentes
    key, n = pk
    # generar el mensaje baso en el mensaje cifrado y la llave usando a^b mod m
    plain = [chr((char ** key) % n) for char in ciphertext]
    #regresar el array de bytes como una string
    return ''.join(plain)

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


publica, privada = keypair(Val1,Val2)
mensaje = ""
mensajeEncrip = ""
msjDescrip =""
print("")
while not salir:
 
    print ("1. Encriptar")
    print ("2. Desencriptar")
    print ("3. Ver llaves publicas y privadas")
    print ("4. Salir")  
    print ("Elige una opcion")
 
    opcion = pedirNumeroEntero()
 
    if opcion == 1:
        mensaje = input("Ingrese el mensaje que desee encriptar: ")
        mensajeEncrip = encriptar(privada,mensaje)
        print("Su mensaje encriptado es: ")
        print (''.join(map(lambda x: str(x), mensajeEncrip)))
        print("")
    elif opcion == 2:
        print("El mensaje desencriptado es: ")
        msjDescrip = desencriptar(publica,mensajeEncrip)
        print(msjDescrip)
        print("")      
    elif opcion == 3:
        print("Opcion 3")
    elif opcion == 4:
        salir = True
    else:
        print ("Introduce un numero entre 1 y 3")
 
print ("Fin")
