# funcion -------------------------------------------------------

def saludar(nombre):
    return f"Hola, {nombre}, bienvenido al hacking 😈"

print(saludar("Bruno"))


# funcion con parametros -------------------------------------------------------

def sumar(a, b):
    return a + b

print(sumar(10, 5))


# funciones lambda--------------------------------------------

cuadrado = lambda x: x ** 2
print(cuadrado(5))  # 25


#importar modulos------------------------------------------------


import math

print(math.sqrt(16))   # raíz cuadrada
print(math.pi)         # constante pi




from random import randint

print(randint(1, 10))  # número aleatorio entre 1 y 10


#crear mis propios modulos-------------------------------------------------------------


#en un archivo llamado "hola.py" hago esto:

def saludar(nombre):
    return f"Hola {nombre}, bienvenido al curso 🚀"

#en otro archivo importo la funcion

#import hola.py            (lo comento si no da error)

#print(mis_funciones.saludar("Bruno"))      (lo comento si no da error)



#ejercicos boludos

# 1 Crea una función que reciba una lista de IPs y las recorra imprimiendo "Escaneando IP: ..."

def recorrer_ips(lista_ip):
    for i in lista_ip:
        print("Escaneando... "+ str(i))

ips = [18183, 19823, 18923, 18238, 1212]

recorrer_ips(ips)

# 2 Haz una función que reciba usuario y contraseña y devuelva un diccionario con esos datos.

def usu_contra(usuario, contra):
    dic = {
        "usuario":usuario,
        "contra":contra
    }
    return dic

print(usu_contra("nasheee","ola123")) #forma 1

otra_forma = usu_contra("naa","loo")
for i, j in otra_forma.items():
    print(i," es ",j)


# 3 Usa el módulo random para crear una función que genere un número aleatorio de 6 dígitos (como un código OTP).

import random

num = random.randint(100000, 999999)
print(num)






