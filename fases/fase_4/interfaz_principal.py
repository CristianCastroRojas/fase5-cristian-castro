# ============================
# IMPORTACIONES
# ============================

# Constantes globales para título de aplicación y nombre del estudiante
from config.fase_4.constantes_globales import TITULO_APP, NOMBRE_ESTUDIANTE

# Librería gráfica Tkinter
import tkinter as tk

# Ventanas emergentes (errores, confirmaciones, información)
from tkinter import messagebox

# Clase del Árbol Binario de Búsqueda
from fases.fase_4.arbol import ArbolBinarioBusqueda

# Importación de constantes visuales y mensajes
from config.fase_4.constantes_interfaz import (
    ANCHO_VENTANA,
    ALTO_VENTANA,
    COLOR_FONDO,
    COLOR_PRIMARIO,
    COLOR_EXITO,
    COLOR_PELIGRO,
    COLOR_BLANCO,
    COLOR_CANVAS_BORDE,
    TEXTO_INPUT,
    TEXTO_PREORDEN,
    TEXTO_INORDEN,
    TEXTO_POSORDEN,
    ERROR_VACIO,
    ERROR_SOLO_ENTEROS,
    ERROR_RANGO_EXCEDIDO,
    ERROR_GENERAL,
    MSG_EXISTE,
    MSG_NO_EXISTE,
)

# Clase encargada únicamente del dibujo del árbol
from fases.fase_4.renderizador import RenderizadorArbol

# ============================
# INICIO DE LA APLICACIÓN
# ============================


# Función principal que crea la ventana
def iniciar_app():
    Ventana()


# ============================
# CLASE PRINCIPAL DE INTERFAZ
# ============================


class Ventana:

    def __init__(self, parent=None):

        # Crear instancia del árbol binario
        self.arbol = ArbolBinarioBusqueda()

        # Si existe una ventana padre se abre como ventana secundaria
        if parent:
            self.ventana = tk.Toplevel(parent)
        else:
            # Si no existe padre se crea ventana principal
            self.ventana = tk.Tk()

        # Configuración básica de ventana
        self.ventana.title(TITULO_APP + " - " + NOMBRE_ESTUDIANTE)
        self.ventana.geometry(f"{ANCHO_VENTANA}x{ALTO_VENTANA}")
        self.ventana.resizable(False, False)

        self.ventana.configure(bg=COLOR_FONDO)

        # Guarda el último nodo agregado
        # Se usa para resaltarlo visualmente
        self.ultimo_agregado = None

        # Construcción interfaz gráfica
        self.crear_interfaz()

    # =========================
    # CREACIÓN INTERFAZ
    # =========================

    def crear_interfaz(self):

        # ------------------------
        # CABECERA
        # ------------------------

        header = tk.Frame(self.ventana, bg=COLOR_PRIMARIO, height=60)
        header.pack(fill="x")

        tk.Label(
            header,
            text=TITULO_APP.upper(),
            bg=COLOR_PRIMARIO,
            fg="white",
            font=("Segoe UI", 14, "bold"),
        ).pack(pady=15)

        # ------------------------
        # CONTENEDOR PRINCIPAL
        # ------------------------

        main_frame = tk.Frame(self.ventana, bg=COLOR_FONDO)
        main_frame.pack(fill="both", expand=True, padx=25, pady=15)

        # ------------------------
        # FORMULARIO DE ENTRADA
        # ------------------------

        form = tk.Frame(main_frame, bg=COLOR_BLANCO)
        form.pack(pady=(0, 10), fill="x")

        tk.Label(
            form,
            text=TEXTO_INPUT,
            bg=COLOR_BLANCO,
            font=("Segoe UI", 10),
        ).pack(anchor="w")

        # Campo donde el usuario escribe valores
        self.entry = tk.Entry(form, font=("Segoe UI", 12))

        self.entry.pack(fill="x", pady=5)

        # Cursor automático en entrada
        self.entry.focus()

        # ------------------------
        # BOTONES
        # ------------------------

        btn_frame = tk.Frame(main_frame, bg=COLOR_FONDO)
        btn_frame.pack(pady=10, fill="x")

        # Botón agregar nodo
        tk.Button(
            btn_frame,
            text="AGREGAR NODO",
            bg=COLOR_PRIMARIO,
            fg="white",
            command=self.agregar,
            font=("Segoe UI", 10, "bold"),
        ).pack(
            side="left",
            expand=True,
            fill="x",
            padx=(0, 5),
        )

        # Botón buscar nodo
        tk.Button(
            btn_frame,
            text="BUSCAR NODO",
            bg=COLOR_EXITO,
            fg="white",
            command=self.buscar,
            font=("Segoe UI", 10, "bold"),
        ).pack(
            side="left",
            expand=True,
            fill="x",
            padx=5,
        )

        # Botón limpiar árbol
        tk.Button(
            btn_frame,
            text="LIMPIAR",
            bg="#f0ad4e",
            fg="white",
            command=self.limpiar,
            font=("Segoe UI", 10, "bold"),
        ).pack(
            side="left",
            expand=True,
            fill="x",
            padx=5,
        )

        # Botón salir
        tk.Button(
            btn_frame,
            text="SALIR",
            bg=COLOR_PELIGRO,
            fg="white",
            command=self.salir,
            font=("Segoe UI", 10, "bold"),
        ).pack(
            side="left",
            expand=True,
            fill="x",
            padx=(5, 0),
        )

        # ------------------------
        # ÁREA DE DIBUJO DEL ÁRBOL
        # ------------------------

        tk.Label(
            main_frame,
            text="ÁRBOL",
            bg=COLOR_FONDO,
            font=("Segoe UI", 12, "bold"),
        ).pack(pady=(10, 0))

        # Canvas donde se dibuja el árbol
        self.canvas = tk.Canvas(
            main_frame,
            width=850,
            height=280,
            bg="white",
            highlightthickness=1,
            highlightbackground=COLOR_CANVAS_BORDE,
        )

        self.canvas.pack(pady=10)

        # Principio SOLID (SRP)
        # Una clase diferente se encarga exclusivamente del dibujo
        self.renderizador = RenderizadorArbol(self.canvas)

        # ------------------------
        # RECORRIDOS DEL ÁRBOL
        # ------------------------

        rec_frame = tk.Frame(main_frame, bg=COLOR_FONDO)
        rec_frame.pack(pady=5)

        tk.Label(rec_frame, text=TEXTO_PREORDEN, bg=COLOR_FONDO).grid(row=0, column=0)

        tk.Label(rec_frame, text=TEXTO_INORDEN, bg=COLOR_FONDO).grid(row=0, column=1)

        tk.Label(rec_frame, text=TEXTO_POSORDEN, bg=COLOR_FONDO).grid(row=0, column=2)

        # Cajas de texto para mostrar recorridos
        self.pre = tk.Text(rec_frame, height=4, width=30)
        self.ino = tk.Text(rec_frame, height=4, width=30)
        self.pos = tk.Text(rec_frame, height=4, width=30)

        # Centrar texto
        self.pre.tag_configure("center", justify="center")
        self.ino.tag_configure("center", justify="center")
        self.pos.tag_configure("center", justify="center")

        # Solo lectura
        self.pre.config(state=tk.DISABLED, bg="#f0f0f0")
        self.ino.config(state=tk.DISABLED, bg="#f0f0f0")
        self.pos.config(state=tk.DISABLED, bg="#f0f0f0")

        self.pre.grid(row=1, column=0, padx=5)
        self.ino.grid(row=1, column=1, padx=5)
        self.pos.grid(row=1, column=2, padx=5)

    # =========================
    # VALIDACIÓN
    # =========================

    def validar(self):

        # Obtener valor digitado
        v = self.entry.get().strip()

        # Campo vacío
        if v == "":
            messagebox.showerror(ERROR_GENERAL, ERROR_VACIO)
            return None

        try:
            # Convertir entero decimal
            valor = int(v)

        except ValueError:

            try:
                # Permitir binario, hexadecimal y octal
                valor = int(v, 0)

            except ValueError:
                messagebox.showerror(ERROR_GENERAL, ERROR_SOLO_ENTEROS)
                return None

        # Validación rango entero 32 bits
        MIN_INT32 = -2147483648
        MAX_INT32 = 2147483647

        if valor < MIN_INT32 or valor > MAX_INT32:
            messagebox.showerror(ERROR_GENERAL, ERROR_RANGO_EXCEDIDO)
            return None

        return valor

    # =========================
    # AGREGAR NODO
    # =========================

    def agregar(self):

        v = self.validar()

        if v is None:
            return

        try:

            # Insertar nodo
            self.arbol.insertar(v)

            # Guardar último agregado
            self.ultimo_agregado = v

            # Actualizar interfaz
            self.actualizar()

            # Limpiar entrada
            self.entry.delete(0, tk.END)

        except Exception as e:
            messagebox.showerror(ERROR_GENERAL, str(e))

    # =========================
    # BUSCAR NODO
    # =========================

    def buscar(self):

        v = self.validar()

        if v is None:
            return

        # Buscar valor en árbol
        if self.arbol.buscar(v):

            messagebox.showinfo("Resultado", MSG_EXISTE.format(valor=v))

        else:

            messagebox.showwarning("Resultado", MSG_NO_EXISTE.format(valor=v))

    # =========================
    # LIMPIAR ÁRBOL
    # =========================

    def limpiar(self):

        self.arbol.limpiar()

        self.ultimo_agregado = None

        self.actualizar()

        self.canvas.delete("all")

    # =========================
    # ACTUALIZAR INTERFAZ
    # =========================

    def actualizar(self):

        # Habilitar edición temporal
        self.pre.config(state=tk.NORMAL)
        self.ino.config(state=tk.NORMAL)
        self.pos.config(state=tk.NORMAL)

        # Limpiar textos anteriores
        self.pre.delete("1.0", tk.END)
        self.ino.delete("1.0", tk.END)
        self.pos.delete("1.0", tk.END)

        # Obtener recorridos
        str_pre = ", ".join(map(str, self.arbol.preorden()))
        str_ino = ", ".join(map(str, self.arbol.inorden()))
        str_pos = ", ".join(map(str, self.arbol.posorden()))

        # Mostrar resultados
        self.pre.insert(tk.END, str_pre, "center")
        self.ino.insert(tk.END, str_ino, "center")
        self.pos.insert(tk.END, str_pos, "center")

        # Volver solo lectura
        self.pre.config(state=tk.DISABLED)
        self.ino.config(state=tk.DISABLED)
        self.pos.config(state=tk.DISABLED)

        # Redibujar árbol
        self.renderizador.dibujar(self.arbol, self.ultimo_agregado)

    # =========================
    # SALIR
    # =========================

    def salir(self):

        if messagebox.askyesno(
            "Confirmar Salida",
            "¿Está seguro que desea cerrar la Fase 4 y volver al menú principal?",
        ):
            self.ventana.destroy()
