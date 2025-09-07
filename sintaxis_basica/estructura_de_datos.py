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
