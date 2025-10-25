# main.py
from catalogo import Pelicula, CatalogoPeliculas  # importamos las clases

# ---------- FUNCIÓN RECURSIVA DEL MENÚ ----------
def mostrar_menu(catalogo):
    print("\n--- MENÚ ---")
    print("1. Agregar Película")
    print("2. Listar Películas")
    print("3. Eliminar Catálogo de Películas")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre_pelicula = input("Ingrese el nombre de la película: ")
        pelicula = Pelicula(nombre_pelicula)
        catalogo.agregar(pelicula)

    elif opcion == "2":
        catalogo.listar()

    elif opcion == "3":
        catalogo.eliminar()

    elif opcion == "4":
        print("👋 ¡Gracias por usar el catálogo de películas!")
        return  # caso base para terminar la recursión

    else:
        print("❌ Opción no válida. Intente nuevamente.")

    # llamada recursiva para volver al menú
    mostrar_menu(catalogo)


# ---------- FUNCIÓN PRINCIPAL ----------
def main():
    nombre_catalogo = input("Ingrese el nombre del catálogo de películas: ")
    catalogo = CatalogoPeliculas(nombre_catalogo)
    mostrar_menu(catalogo)


# ---------- EJECUCIÓN ----------
if __name__ == "__main__":
    main()
