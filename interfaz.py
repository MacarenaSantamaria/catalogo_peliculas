# interfaz_tkinter.py
import tkinter as tk
from tkinter import messagebox, simpledialog
from Catalogo import Pelicula, CatalogoPeliculas

# ---------- INTERFAZ GRÁFICA ----------
class AppCatalogo:
    def __init__(self, master):
        self.master = master
        self.master.title("🎬 Catálogo de Películas")
        self.master.geometry("420x420")
        self.master.configure(bg="#1e1e1e")

        # Campo de texto
        self.label = tk.Label(master, text="Nombre del Catálogo:", fg="white", bg="#1e1e1e", font=("Arial", 11))
        self.label.pack(pady=10)

        self.entry_catalogo = tk.Entry(master, width=30, font=("Arial", 11))
        self.entry_catalogo.pack()

        self.btn_crear = tk.Button(master, text="Crear / Abrir", command=self.crear_catalogo, width=20, bg="#0078D7", fg="white")
        self.btn_crear.pack(pady=10)

        self.frame_botones = tk.Frame(master, bg="#1e1e1e")
        self.frame_botones.pack(pady=10)

        self.btn_agregar = tk.Button(self.frame_botones, text="➕ Agregar película", command=self.agregar_pelicula, width=20, bg="#2e8b57", fg="white")
        self.btn_listar = tk.Button(self.frame_botones, text="📋 Listar", command=self.listar_peliculas, width=20, bg="#4682b4", fg="white")
        self.btn_eliminar = tk.Button(self.frame_botones, text="🗑️ Eliminar catálogo", command=self.eliminar_catalogo, width=20, bg="#b22222", fg="white")

        self.btn_agregar.grid(row=0, column=0, padx=5, pady=5)
        self.btn_listar.grid(row=1, column=0, padx=5, pady=5)
        self.btn_eliminar.grid(row=2, column=0, padx=5, pady=5)

        self.catalogo = None

    def crear_catalogo(self):
        nombre = self.entry_catalogo.get().strip()
        if not nombre:
            messagebox.showwarning("Advertencia", "Debe ingresar un nombre para el catálogo.")
            return
        self.catalogo = CatalogoPeliculas(nombre)
        messagebox.showinfo("Catálogo creado", f"Se ha abierto el catálogo '{nombre}.txt'.")

    def agregar_pelicula(self):
        if not self.catalogo:
            messagebox.showwarning("Error", "Primero crea o abre un catálogo.")
            return
        nombre = simpledialog.askstring("Agregar película", "Ingrese el nombre de la película:")
        if nombre:
            pelicula = Pelicula(nombre)
            self.catalogo.agregar(pelicula)
            messagebox.showinfo("Éxito", f"'{pelicula}' agregada al catálogo.")

    def listar_peliculas(self):
        if not self.catalogo:
            messagebox.showwarning("Error", "Primero crea o abre un catálogo.")
            return
        peliculas = list(self.catalogo.leer_peliculas())
        if not peliculas:
            messagebox.showinfo("Catálogo vacío", "No hay películas registradas.")
        else:
            lista = "\n".join(sorted(peliculas))
            messagebox.showinfo(f"🎬 Películas en '{self.catalogo.nombre}'", lista)

    def eliminar_catalogo(self):
        if not self.catalogo:
            messagebox.showwarning("Error", "Primero crea o abre un catálogo.")
            return
        confirmar = messagebox.askyesno("Confirmar eliminación", f"¿Eliminar '{self.catalogo.nombre}.txt'?")
        if confirmar:
            self.catalogo.eliminar()
            messagebox.showinfo("Eliminado", f"Catálogo '{self.catalogo.nombre}' eliminado.")
            self.catalogo = None
            self.entry_catalogo.delete(0, tk.END)


# ---------- EJECUCIÓN ----------
if __name__ == "__main__":
    root = tk.Tk()
    app = AppCatalogo(root)
    root.mainloop()
