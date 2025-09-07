# 111111111111111111111111 
# Crea un programa que: Pida al usuario 10 números. Los almacene en una lista. 
# Cree otra lista solo con los números pares. Imprima ambas listas.

"""
num = 10
nums = []
while num > 0:
    numero = int(input("Ingrese un num: "))
    nums.append(numero)
    num -= 1
print("numeros originales "+ str(nums))

nums_pares = []

for i in nums:
    if i % 2 == 0:
        nums_pares.append(i)

print("numeros pares: " + str(nums_pares))

"""


""" 222222222222222222222222222222222
Pida al usuario nombre y nota de 5 estudiantes.
Guarde los datos en un diccionario {nombre: nota}.
Crea una función promedio_notas(dic) que calcule el promedio de las notas.
Imprime el promedio usando la función.
"""


"""
alumnos_nota = {}

for i in range(5):
    nombre = input("Ingrese nombre estudiante: ")
    nota = input("Ingrese nota: ")
    alumnos_nota[nombre] = nota


for i, j in alumnos_nota.items():
    print(i, " tiene nota de ", j)

def calcular_promedio(dic_notas):
    suma_notas = 0
    cantidad = 0

    for i, j in dic_notas.items():
        suma_notas += int(j)
        cantidad += 1
    
    return suma_notas/cantidad

print("promedio es : " + str(calcular_promedio(alumnos_nota)))

"""



""" 33333333333333333333333333333333
Pida al usuario 5 nombres de ciudades y sus respectivas poblaciones.
Guarde los nombres en una lista y las poblaciones en una tupla.
Imprima cada ciudad con su población.
"""


"""
ciudades = []
poblacion = ()

for i in range(5):
    ciudad = input("Ingrese una ciudad: ")
    gente = input("Poblacion: ")

    ciudades.append(ciudad)
    poblacion += (gente,)

for i in range(5):
    print(ciudades[i] + " tiene una poblacion de "+ poblacion[i])

"""

"""444444444444444444444444444444444444
Pida al usuario 10 números y los guarde en un conjunto.
Imprima los números únicos y diga cuántos números distintos se ingresaron.
Pregunte un número y diga si ya estaba en el conjunto.
"""

"""
nums = set()
for i in range(10):
    nums.add(int(input("Ingrese un num: ")))

print("Numeros unicos: " + str(nums))
print("Numeros distintos: " + str(len(nums)))

valor = int(input("Ingres un valor para ver si ta en el set: "))

if valor in nums:
    print("si ta")
else:
    print("no ta")

"""    

"""55555555555555555555555555555555555555555555
Pida un número al usuario.
Use una función que devuelva True si el número es par y False si es impar.
Use la función sqrt de math para imprimir la raíz cuadrada del número solo si es par.
"""

"""
import math

def es_par():
    num = int(input("Ingrese un número: "))
    
    if num % 2 == 0:
        print(math.sqrt(num))
        return True
    else:
        return False
    
print(es_par())
"""

"""66666666666666666666666666666666
Lea un archivo nombres.txt con un nombre por línea.
Guarde los nombres en una lista.
Imprima cuántos nombres hay y todos los nombres que comienzan con la letra “A”.
"""


"""
f = open("nombres.txt", "r")
contenido = f.read()
f.close()

nombres = contenido.split("\n")
nombres_a = []

for i in nombres:
    if i.startswith("a") or i.startswith("A"):
        nombres_a.append(i)

print(nombres_a)

"""

"""777777777777777777777777777777777777777
Pida al usuario nombre, edad y ciudad de 3 personas.
Guarde los datos en un archivo personas.json en formato lista de diccionarios.
Luego, lea el archivo e imprima solo los nombres de las personas mayores de 25 años.
"""

"""
personas = []
import json

for i in range(3):
    nombre = input("Ingrese el nombre: ")
    edad = int(input("Ingrese la edad: "))
    ciudad = input("Ingrese su ciudad: ")
    personas.append({"id": i+1, "nombre": nombre, "edad": edad, "ciudad": ciudad})

# Guardar toda la lista en el archivo una sola vez
with open("personas.json", "w") as f:
    json.dump(personas, f, indent=4)  # indent=4 para mejor formato

with open("personas.json", "r") as f:
    datos = json.load(f)

for i in datos:
    if i["edad"] > 25:
        print(i["nombre"])

"""



"""8888888888888888888888888888888888888
Pida al usuario números hasta que ingrese “fin”.
Guarde los números en una lista.
Cree una función que devuelva suma, promedio, máximo y mínimo.
Imprima los resultados en consola y los guarde en un archivo estadisticas.txt.
"""

"""
nums = []
print("Ingrese numeros y para teminar fin")

while True:
    num = input("Numero: ")
    if num == "fin":
        break
    else:
        nums.append(int(num))

def cuentas(lista_numeros):
    suma = 0
    max = lista_numeros[0]
    min = lista_numeros[0]
    for i in lista_numeros:
        suma += i
        if i > max:
            max = i
        if i < min:
            min = i
    print("Suma: " + str(suma))
    print("Promedio: " + str(suma/len(lista_numeros)))
    print("Maximo: " + str(max))
    print("Minimo: " + str(min))

cuentas(nums)


"""


"""9999999999999999999999999999999999999999999999999999
Pida al usuario varios productos (nombre y precio) hasta que escriba “fin”.
Guarde los datos en un diccionario {producto: precio}.
Cree una función que devuelva los productos más caros (precio mayor a 100) y los baratos (precio menor o igual a 100).
Imprima ambas listas y guárdalas en un archivo productos.txt.
"""


"""10101010100010100101010101010101010110001 DIIIIIIIIIIIIIIIIIIIIEEEEEEEEEEEEEEEES
Crea un programa que:
Sea un registro de estudiantes.
Permita:
Agregar estudiante: nombre, edad, notas de 3 materias.
Calcular promedio de cada estudiante y determinar si aprobó (promedio ≥ 6).
Guardar todos los datos en un archivo estudiantes.json.
Listar todos los estudiantes con su promedio y estado (aprobado/reprobado).
Usa funciones separadas, estructuras de datos adecuadas y aplica buenas prácticas.
"""