# Crear lista ----------------------------------------------------------------
ips = ["192.168.1.1", "192.168.1.10", "10.0.0.5"]

# Acceder por índice
print(ips[0])   # "192.168.1.1"
print(ips[-1])  # último elemento

# Modificar
ips[1] = "192.168.1.20"

# Añadir y eliminar
ips.append("172.16.0.1")
ips.remove("10.0.0.5")

# Recorrer lista
for ip in ips:
    print("Escaneando:", ip)


#tuplas (listas inmutables) ----------------------------------------------------------------
puertos = (21, 22, 80, 443)

print(puertos[0])  # 21
# puertos[1] = 25  ❌ ERROR → no se puede cambiar


#diccionarios ----------------------------------------------------------------

usuario = {
    "nombre": "bruno",
    "rol": "pentester",
    "nivel": "novato"
}

print(usuario["nombre"])  # "bruno"

# Modificar
usuario["nivel"] = "intermedio"

# Agregar
usuario["email"] = "bruno@ejemplo.com"

# Recorrer
for clave, valor in usuario.items():
    print(clave, ":", valor)


 #conjuntos (no tienen dublicados)   

dominios = {"google.com", "yahoo.com", "google.com"}
print(dominios)  # {"google.com", "yahoo.com"} → elimina duplicados

# Agregar
dominios.add("hotmail.com")

# Comprobar
print("yahoo.com" in dominios)  # True



#Ejercicios boludos

#1 Crea una lista con 5 puertos comunes y recórrela mostrando: "Probando puerto X...".

lista_puertos = [21, 22, 23, 80, 443]
for i in lista_puertos:
    print(i)

#2 Crea un diccionario con un usuario (usuario, password, rol) y muestra solo el password.

dic = {
    "usuario":"bruno23",
    "password":"hola123",
    "rol":"admin"
}
print(dic["password"])

#3 Usa un conjunto para eliminar IPs duplicadas de esta lista:

ips = [1, 2, 3, 4, 1, 5, 1, 3, 6, 3, 6, 4, 3]

ips_no_repetidas = set()

for i in ips:
    ips_no_repetidas.add(i)

print(ips_no_repetidas)
