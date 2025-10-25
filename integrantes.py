integrantes = ["Macarena Santamaria", "Francisca Urrutia", "Sofia Daniela Vedia"]

# Abrir (o crear) el archivo en modo escritura
with open("integrantes.txt", "w") as archivo:
    for nombre in integrantes:
        archivo.write(nombre + "\n")  # Escribe cada nombre en una línea

print("Archivo 'integrantes.txt' creado con éxito.\n")

# Leer y mostrar el contenido del archivo
with open("integrantes.txt", "r") as archivo:
    contenido = archivo.read()
    print("Contenido del archivo:")
    print(contenido)