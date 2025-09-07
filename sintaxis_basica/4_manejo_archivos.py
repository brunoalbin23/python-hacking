# Modo lectura ("r")---------------------------------------------


f = open("datos.txt", "r")
contenido = f.read()
print(contenido)
f.close()


# escribir un archivo --------------------------------------------------------

with open("resultados.txt", "w") as f:
    f.write("Escaneo completado\n")
    f.write("IP: 192.168.1.1 - Puerto 80 abierto\n")


# agregar sin borrar --------------------------------------------------------

with open("resultados.txt", "a") as f:
    f.write("IP: 192.168.1.2 - Puerto 22 abierto\n")
    f.write("IP: 192.168.9.2 - Puerto 1 abierto\n")



# archivos como lista ----------------------------------------------------

with open("datos.txt", "r") as f:
    usuarios = f.readlines()

print(usuarios)  # lista con cada línea

# ahora letra por letra del documento

with open("datos.txt", "r") as f:
    usuarios = f.readlines()
    letras = []
    for i in usuarios:
        for j in i:
            letras.append(j)

print(letras)  # lista con cada letras



# json ----------------------------------------------------

import json

# Guardar datos
datos = {"usuario": "bruno", "rol": "pentester"}
with open("user.json", "w") as f:
    json.dump(datos, f)


# json con forma----------------------------------------------------


# Diccionario en Python
datos = {"usuario": "bruno","rol": "pentester"}

# Guardar en archivo JSON
with open("usuario.json", "w") as f:
    json.dump(datos, f, indent=4)  # indent=4 lo hace "bonito"
