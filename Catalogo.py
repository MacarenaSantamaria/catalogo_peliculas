import os

# ---------- DECORADOR ----------
def registro_accion(func):
    """Decorador para registrar acciones del catálogo."""
    def wrapper(*args, **kwargs):
        print(f"\n🟢 Ejecutando: {func.__name__}")
        resultado = func(*args, **kwargs)
        print(f"🔵 Acción '{func.__name__}' completada.")
        return resultado
    return wrapper


# ---------- CLASE PELÍCULA ----------
class Pelicula:
    def __init__(self, nombre):
        limpiar_nombre = lambda n: n.strip().title()  # función lambda
        self.__nombre = limpiar_nombre(nombre)

    def __str__(self):
        return self.__nombre


# ---------- CLASE CATÁLOGO ----------
class CatalogoPeliculas:
    def __init__(self, nombre_catalogo):
        self.nombre = nombre_catalogo
        self.ruta_archivo = f"{nombre_catalogo}.txt"

        # if ternario para crear el archivo si no existe
        open(self.ruta_archivo, 'w', encoding='utf-8').close() if not os.path.exists(self.ruta_archivo) else None

    @registro_accion
    def agregar(self, pelicula):
        with open(self.ruta_archivo, 'a', encoding='utf-8') as archivo:
            archivo.write(f"{pelicula}\n")
        print(f"✅ Película '{pelicula}' agregada al catálogo '{self.nombre}'.")

    def leer_peliculas(self):
        """Generador que lee las películas una por una."""
        if os.path.exists(self.ruta_archivo):
            with open(self.ruta_archivo, 'r', encoding='utf-8') as archivo:
                for linea in archivo:
                    yield linea.strip()

    @registro_accion
    def listar(self):
        print(f"\n🎬 Catálogo: {self.nombre}")
        peliculas = list(self.leer_peliculas())

        if peliculas:
            peliculas_ordenadas = sorted(peliculas, key=lambda p: p.lower())  # ordenadas alfabéticamente
            print("Películas registradas:")
            for i, pelicula in enumerate(peliculas_ordenadas, start=1):
                print(f"{i}. {pelicula}")
        else:
            print("⚠️ No hay películas registradas aún.")

    @registro_accion
    def eliminar(self):
        def confirmar_eliminacion():  # función anidada
            return input("¿Seguro que desea eliminar el catálogo? (s/n): ").lower() == "s"

        if os.path.exists(self.ruta_archivo):
            if confirmar_eliminacion():
                os.remove(self.ruta_archivo)
                print(f"🗑️ Catálogo '{self.nombre}' eliminado correctamente.")
            else:
                print("Operación cancelada.")
        else:
            print("⚠️ El catálogo no existe o ya fue eliminado.")
