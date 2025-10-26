import tkinter as tk
from tkinter import messagebox, simpledialog
from Catalogo import Pelicula, CatalogoPeliculas
from datetime import datetime

class AppCatalogo:
    def __init__(self, master):
        self.master = master
        self.master.title("🎬 Catálogo de Películas")
        self.master.geometry("500x600")
        self.master.config(bg="#0f1116")
        self.master.resizable(False, False)

        anio = datetime.now().year

        # ---------- BANNER SUPERIOR ----------
        banner = tk.Label(
            master,
            text=f"🎞️Catálogo de Películas🎞️",
            font=("Segoe UI", 16, "bold"),
            bg="#20232a",
            fg="#f8f8f2",
            pady=15
        )
        banner.pack(fill="x", pady=(0, 15))

        # ---------- MENSAJE DE BIENVENIDA ----------
        bienvenida = tk.Label(
            master,
            text="🍿 ¡Bienvenido/a de vuelta!  🍿\nPersonaliza tus listas de forma simple y divertida.",
            bg="#0f1116", fg="#e0e0e0",
            wraplength=440, justify="center",
            font=("Segoe UI", 15)
        )
        bienvenida.pack(pady=(0, 10))

        # ---------- ETIQUETA Y ENTRADA ----------
        label = tk.Label( master,
            text="🎬 Ingresa un nombre para tu catálogo\n",
            bg="#0f1116", fg="white",
            font=("Segoe UI", 11, "bold")
        )
        label.pack(pady=(20, 5))

        # campo de entrada 
        self.entry_var = tk.StringVar()
        self.entry = tk.Entry(
            master, textvariable=self.entry_var,
            font=("Segoe UI", 12), width=18,
            relief="flat", justify="center"
        )
        self.entry.pack(pady=(0, 10), ipady=6)

   
        # ---------- BOTONES ----------
        self.crear_btn = self.boton_redondo("📁 Crear / Abrir", "#0078D7", self.crear_catalogo)
        self.agregar_btn = self.boton_redondo("➕ Agregar película", "#2E8B57", self.agregar_pelicula)
        self.listar_btn = self.boton_redondo("📋 Listar", "#4682B4", self.listar_peliculas)
        self.eliminar_btn = self.boton_redondo("🗑️ Eliminar catálogo", "#B22222", self.eliminar_catalogo)

        for b in [self.crear_btn, self.agregar_btn, self.listar_btn, self.eliminar_btn]:
            b.pack(pady=6)

        # ---------- SECCIÓN RESULTADOS ----------
        self.text_area = tk.Text(
            master, height=12, width=55,
            bg="#1c1f26", fg="#ffffff",
            font=("Consolas", 10),
            relief="flat", wrap="word"
         )
        # self.text_area.pack(pady=(20, 10))
        # self.text_area.insert(tk.END, "🎬 Esperando creación de catálogo...\n")
        # self.text_area.configure(state="disabled")

        # ---------- PIE DE PÁGINA ----------
        footer = tk.Label(
            master,
            text="💻 Proyecto Final Curso Python Ada — Python 3.9+ — 2025",
            bg="#0f1116", fg="#a0a0a0",
            font=("Segoe UI", 8)
        )
        footer.pack(side="bottom", pady=10)

        self.catalogo = None

    # ---------- FUNCIÓN BOTÓN PERSONALIZADO ----------
    def boton_redondo(self, texto, color, comando):
        
        return tk.Button(
            self.master, text=texto,
            font=("Segoe UI", 10, "bold"),
            bg=color, fg="white",
            width=20, height=1,
            relief="flat", bd=0,
            activebackground=color,
            activeforeground="white",
            command=comando,
            cursor="hand2"
        )

    # ---------- FUNCIONES PRINCIPALES ----------
    def crear_catalogo(self):
        nombre = self.entry_var.get().strip()
        if not nombre:
            messagebox.showwarning("Advertencia", "Debe ingresar un nombre para el catálogo.")
            return

        # Crear el catálogo (archivo .txt)
        self.catalogo = CatalogoPeliculas(nombre)

        # Si ya existía un cuadro anterior, eliminarlo
        if hasattr(self, "text_area"):
            self.text_area.destroy()

        # Crear el cuadro de texto dinámicamente
        self.text_area = tk.Text(
            self.master, height=12, width=55,
            bg="#1c1f26", fg="#ffffff",
            font=("Consolas", 10),
            relief="flat", wrap="word"
        )
        self.text_area.pack(pady=(20, 10))
        self.text_area.insert(
            tk.END,
            f"✅ Catálogo '{nombre}' creado o abierto correctamente.\n"
        )
        self.text_area.configure(state="disabled")


    def agregar_pelicula(self):
        if not self.catalogo:
            messagebox.showwarning("Error", "Primero crea o abre un catálogo.")
            return
        nombre = simpledialog.askstring("Agregar película", "Ingrese el nombre de la película:")
        if nombre:
            pelicula = Pelicula(nombre)
            self.catalogo.agregar(pelicula)
            self.mostrar_mensaje(f"➕ Película '{pelicula}' agregada con éxito.")

    def listar_peliculas(self):
        if not self.catalogo:
            messagebox.showwarning("Error", "Primero crea o abre un catálogo.")
            return
        peliculas = list(self.catalogo.leer_peliculas())
        self.text_area.configure(state="normal")
        self.text_area.delete(1.0, tk.END)
        if not peliculas:
            self.text_area.insert(tk.END, "⚠️ No hay películas registradas.\n")
        else:
            self.text_area.insert(tk.END, f"🎬 Catálogo: {self.catalogo.nombre}\n\n")
            for i, p in enumerate(sorted(peliculas), start=1):
                self.text_area.insert(tk.END, f"{i}. {p}\n")
        self.text_area.configure(state="disabled")

    def eliminar_catalogo(self):
        if not self.catalogo:
            messagebox.showwarning("Error", "Primero crea o abre un catálogo.")
            return
        confirmar = messagebox.askyesno("Confirmar eliminación", f"¿Eliminar '{self.catalogo.nombre}.txt'?")
        if confirmar:
            self.catalogo.eliminar()
            self.mostrar_mensaje(f"🗑️ Catálogo '{self.catalogo.nombre}' eliminado.")
            self.catalogo = None
            self.entry_var.set("")

    def mostrar_mensaje(self, mensaje):
        self.text_area.configure(state="normal")
        self.text_area.insert(tk.END, f"{mensaje}\n")
        self.text_area.configure(state="disabled")
        self.text_area.see(tk.END)


# ---------- EJECUCIÓN ----------
if __name__ == "__main__":
    root = tk.Tk()
    AppCatalogo(root)
    root.mainloop()
