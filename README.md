# 🎬 Catálogo de Películas

> Proyecto colaborativo desarrollado para practicar **POO en Python**, manejo de archivos y diseño modular.  
> Permite crear, listar y eliminar catálogos de películas de forma interactiva (por consola o ventana gráfica).  

---

## 🧩 Descripción general

El sistema **Catálogo de Películas** permite administrar una lista de películas almacenadas en archivos `.txt`.  
Cada catálogo se crea con un nombre propio, y las películas pueden **agregarse**, **listarse** o **eliminarse** fácilmente.

💡 Está construido siguiendo una estructura clara:
- Uso de **clases** y **métodos** (Programación Orientada a Objetos)
- Decoradores y funciones anidadas
- Lectura y escritura en archivos
- Interacción con el usuario mediante consola o interfaz gráfica

---

## 🗂️ Estructura del proyecto

catalogo_peliculas-feature-principal/
├─ Catalogo.py # Lógica principal: clases y métodos del catálogo
├─ principal.py # Menú principal por consola
├─ interfaz.py # Versión gráfica del catálogo (Tkinter)
├─ integrantes.py # Genera y muestra la lista de integrantes
├─ Drama.txt # Ejemplo de catálogo existente
├─ requirements.txt # Versión mínima de Python
└─ README.md # Detalles del proyecto


---

## ⚙️ Requisitos

- **Python 3.9 o superior**
- (Opcional) VS Code o cualquier IDE que soporte Python  
- No se requieren librerías externas 🐍

---

## 🚀 Ejecución por consola

1. Abre la carpeta del proyecto en tu terminal o VS Code.
2. Ejecuta el siguiente comando:

```bash
python principal.py

El programa mostrará un menú interactivo como este:

--- MENÚ ---
1. Agregar Película
2. Listar Películas
3. Eliminar Catálogo de Películas
4. Salir

Sigue las instrucciones para crear tu propio catálogo.
Por ejemplo, puedes ingresar nombres como:

Titanic
El Señor de los Anillos
Barbie

💻 Ejecución alternativa 

Existe una versión opcional del proyecto que utiliza Tkinter,
la cual permite manejar el catálogo mediante una ventana gráfica interactiva.
Esta versión se encuentra en etapa de pruebas y se ejecuta desde el archivo interfaz.py. 💅

🪟 Descripción

La interfaz permite:

Crear o abrir un catálogo nuevo.

Agregar películas con un cuadro de diálogo.

Listar todas las películas registradas directamente en pantalla.

Eliminar un catálogo existente.

Todo se realiza mediante botones y cuadros de texto, sin necesidad de usar la consola.

🚀 Cómo ejecutarla

Desde la carpeta del proyecto:
python interfaz.py

Al iniciar, se abrirá una ventana como esta:

🎬 Catálogo de Películas
[ Nombre del catálogo... ]
📁 Crear / Abrir
➕ Agregar película
📋 Listar
🗑️ Eliminar catálogo

Cada acción mostrará los resultados directamente dentro de la ventana.
El programa utiliza la misma lógica de clases (CatalogoPeliculas, Pelicula)
que la versión por consola, por lo que ambas son totalmente compatibles.

👩‍💻 Integrantes del equipo

| Nombre                     | Rol            | Aporte principal                            |
| -------------------------- | -------------- | ------------------------------------------- |
| 🩵 **Macarena Santamaría** | Desarrolladora | Estructura de clases y diseño inicial       |
| 💜 **Francisca Urrutia**   | Desarrolladora | Decoradores, funciones recursivas y pruebas |
| 💗 **Sofía Daniela Vedia** | Desarrolladora | Manejo de archivos y menú principal         |

🌸 Características destacadas

Uso de decoradores para registrar acciones

Función recursiva para el menú principal

Generadores (yield) para leer películas una por una

Buenas prácticas con POO y archivos

Diseño simple, funcional y extensible

🌈 Ejemplo de salida (versión consola)

🎬 Catálogo: Drama
Películas registradas:
1. Titanic
2. El Padrino
3. La La Land

Y si eliminas un catálogo:

🗑️ Catálogo 'Drama' eliminado correctamente.

