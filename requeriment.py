# Lista de librerías necesarias para tu proyecto
librerias = [
 
    "Python >= 3.9"
]

# Crear el archivo requirements.txt
with open("requirements.txt", "w") as archivo:
    for lib in librerias:
        archivo.write(lib + "\n")

print("Archivo 'requirements.txt' generado con éxito.")