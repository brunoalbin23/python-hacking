print("hola mundo") # Imprimir

#Comentarios en una sola linea

"""
Comentarios en multiples lineas
"""

a = 10
b = 3
print(a + b)  # suma
print(a - b)  # resta
print(a * b)  # multiplicación
print(a / b)  # división
print(a % b)  # módulo


edad = 18

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

# Bucle for
for i in range(5):
    print("Intento número:", i)

# Bucle while
x = 0
while x < 5:
    print("x vale:", x)
    x += 1

def saludar(nombre):
    return f"Hola, {nombre}, bienvenido al hacking 😈"

print(saludar("Bruno"))

