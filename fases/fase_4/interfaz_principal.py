# ============================
# IMPORTACIONES
# ============================
import tkinter as tk
from tkinter import messagebox

from fases.fase_4.arbol import ArbolBinarioBusqueda

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

from fases.fase_4.renderizador import RenderizadorArbol


# ============================
# INICIADOR DE LA APLICACIÓN
# ============================
def iniciar_app():
    Ventana()


# ============================
# CLASE PRINCIPAL: INTERFAZ ÁRBOL BINARIO
# ============================
class Ventana:

    # ============================
    # INICIALIZACIÓN
    # ============================
    def __init__(self, parent=None):

        # * Estructura principal del árbol
        self.arbol = ArbolBinarioBusqueda()

        # * Ventana principal o secundaria
        if parent:
            self.ventana = tk.Toplevel(parent)
        else:
            self.ventana = tk.Tk()

        # * Configuración base de ventana
        self.ventana.title("Árbol Binario - UNAD")
        self.ventana.geometry(f"{ANCHO_VENTANA}x{ALTO_VENTANA}")
        self.ventana.resizable(False, False)
        self.ventana.configure(bg=COLOR_FONDO)

        # * Último nodo agregado (para resaltado visual)
        self.ultimo_agregado = None

        # * Construcción de interfaz
        self.crear_interfaz()

    # ============================
    # INTERFAZ GRÁFICA
    # ============================
    def crear_interfaz(self):

        # ============================
        # HEADER
        # ============================
        header = tk.Frame(self.ventana, bg=COLOR_PRIMARIO, height=60)
        header.pack(fill="x")

        tk.Label(
            header,
            text="ÁRBOL BINARIO DE BÚSQUEDA",
            bg=COLOR_PRIMARIO,
            fg="white",
            font=("Segoe UI", 14, "bold"),
        ).pack(pady=15)

        # ============================
        # CONTENEDOR PRINCIPAL
        # ============================
        main_frame = tk.Frame(self.ventana, bg=COLOR_FONDO)
        main_frame.pack(fill="both", expand=True, padx=25, pady=15)

        # ============================
        # FORMULARIO DE ENTRADA
        # ============================
        form = tk.Frame(main_frame, bg=COLOR_BLANCO)
        form.pack(pady=(0, 10), fill="x")

        tk.Label(form, text=TEXTO_INPUT, bg=COLOR_BLANCO, font=("Segoe UI", 10)).pack(
            anchor="w"
        )

        self.entry = tk.Entry(form, font=("Segoe UI", 12))
        self.entry.pack(fill="x", pady=5)
        self.entry.focus()

        # ============================
        # BOTONES DE ACCIÓN
        # ============================
        btn_frame = tk.Frame(main_frame, bg=COLOR_FONDO)
        btn_frame.pack(pady=10, fill="x")

        # * Agregar nodo
        tk.Button(
            btn_frame,
            text="AGREGAR NODO",
            bg=COLOR_PRIMARIO,
            fg="white",
            command=self.agregar,
            font=("Segoe UI", 10, "bold"),
        ).pack(side="left", expand=True, fill="x", padx=(0, 5))

        # * Buscar nodo
        tk.Button(
            btn_frame,
            text="BUSCAR NODO",
            bg=COLOR_EXITO,
            fg="white",
            command=self.buscar,
            font=("Segoe UI", 10, "bold"),
        ).pack(side="left", expand=True, fill="x", padx=5)

        # * Limpiar árbol
        tk.Button(
            btn_frame,
            text="LIMPIAR",
            bg="#f0ad4e",
            fg="white",
            command=self.limpiar,
            font=("Segoe UI", 10, "bold"),
        ).pack(side="left", expand=True, fill="x", padx=5)

        # * Salir
        tk.Button(
            btn_frame,
            text="SALIR",
            bg=COLOR_PELIGRO,
            fg="white",
            command=self.salir,
            font=("Segoe UI", 10, "bold"),
        ).pack(side="left", expand=True, fill="x", padx=(5, 0))

        # ============================
        # CANVAS DEL ÁRBOL
        # ============================
        tk.Label(
            main_frame,
            text="VISUALIZACIÓN DEL ÁRBOL",
            bg=COLOR_FONDO,
            font=("Segoe UI", 12, "bold"),
        ).pack(pady=(10, 0))

        self.canvas = tk.Canvas(
            main_frame,
            width=850,
            height=280,
            bg="white",
            highlightthickness=1,
            highlightbackground=COLOR_CANVAS_BORDE,
        )
        self.canvas.pack(pady=10)

        # * Responsabilidad de renderizado separada (SRP)
        self.renderizador = RenderizadorArbol(self.canvas)

        # ============================
        # RECORRIDOS DEL ÁRBOL
        # ============================
        rec_frame = tk.Frame(main_frame, bg=COLOR_FONDO)
        rec_frame.pack(pady=5)

        tk.Label(rec_frame, text=TEXTO_PREORDEN, bg=COLOR_FONDO).grid(row=0, column=0)
        tk.Label(rec_frame, text=TEXTO_INORDEN, bg=COLOR_FONDO).grid(row=0, column=1)
        tk.Label(rec_frame, text=TEXTO_POSORDEN, bg=COLOR_FONDO).grid(row=0, column=2)

        # * Textos de recorridos
        self.pre = tk.Text(rec_frame, height=4, width=30)
        self.ino = tk.Text(rec_frame, height=4, width=30)
        self.pos = tk.Text(rec_frame, height=4, width=30)

        # * Centrado de texto
        self.pre.tag_configure("center", justify="center")
        self.ino.tag_configure("center", justify="center")
        self.pos.tag_configure("center", justify="center")

        # * Solo lectura visual
        self.pre.config(state=tk.DISABLED, bg="#f0f0f0")
        self.ino.config(state=tk.DISABLED, bg="#f0f0f0")
        self.pos.config(state=tk.DISABLED, bg="#f0f0f0")

        self.pre.grid(row=1, column=0, padx=5)
        self.ino.grid(row=1, column=1, padx=5)
        self.pos.grid(row=1, column=2, padx=5)

    # ============================
    # VALIDACIÓN DE ENTRADA
    # ============================
    def validar(self):

        # * Obtener valor ingresado
        v = self.entry.get().strip()

        # * Validación de vacío
        if v == "":
            messagebox.showerror(ERROR_GENERAL, ERROR_VACIO)
            return None

        # * Validación de entero (base 10 o automática)
        try:
            valor = int(v)
        except ValueError:
            try:
                valor = int(v, 0)
            except ValueError:
                messagebox.showerror(ERROR_GENERAL, ERROR_SOLO_ENTEROS)
                return None

        # * Validación de rango 32 bits
        MIN_INT32 = -2147483648
        MAX_INT32 = 2147483647

        if valor < MIN_INT32 or valor > MAX_INT32:
            messagebox.showerror(ERROR_GENERAL, ERROR_RANGO_EXCEDIDO)
            return None

        return valor

    # ============================
    # INSERTAR NODO
    # ============================
    def agregar(self):

        # * Validar entrada del usuario
        v = self.validar()

        # * Si la validación falla, no continuar
        if v is None:
            return

        try:
            # * Insertar valor en el árbol binario
            self.arbol.insertar(v)

            # * Guardar último nodo agregado (para animación)
            self.ultimo_agregado = v

            # * Actualizar interfaz (recorridos + render)
            self.actualizar()

            # * Limpiar campo de entrada
            self.entry.delete(0, tk.END)

        except Exception as e:
            # * Mostrar error del sistema si falla la inserción
            messagebox.showerror(ERROR_GENERAL, str(e))

    # ============================
    # BUSCAR NODO
    # ============================
    def buscar(self):

        # * Validar entrada del usuario
        v = self.validar()

        # * Si no es válido, salir
        if v is None:
            return

        # * Buscar valor en el árbol
        if self.arbol.buscar(v):
            messagebox.showinfo("Resultado", MSG_EXISTE.format(valor=v))
        else:
            messagebox.showwarning("Resultado", MSG_NO_EXISTE.format(valor=v))

    # ============================
    # LIMPIAR ÁRBOL
    # ============================
    def limpiar(self):

        # * Reiniciar estructura del árbol
        self.arbol.limpiar()

        # * Reiniciar último nodo agregado
        self.ultimo_agregado = None

        # * Actualizar interfaz (vaciar recorridos y vista)
        self.actualizar()

        # * Limpiar canvas visual
        self.canvas.delete("all")

    # ============================
    # ACTUALIZAR INTERFAZ
    # ============================
    def actualizar(self):

        # * Habilitar edición temporal
        self.pre.config(state=tk.NORMAL)
        self.ino.config(state=tk.NORMAL)
        self.pos.config(state=tk.NORMAL)

        # * Limpiar textos
        self.pre.delete("1.0", tk.END)
        self.ino.delete("1.0", tk.END)
        self.pos.delete("1.0", tk.END)

        # * Recorridos
        str_pre = ", ".join(map(str, self.arbol.preorden()))
        str_ino = ", ".join(map(str, self.arbol.inorden()))
        str_pos = ", ".join(map(str, self.arbol.posorden()))

        # * Insertar datos
        self.pre.insert(tk.END, str_pre, "center")
        self.ino.insert(tk.END, str_ino, "center")
        self.pos.insert(tk.END, str_pos, "center")

        # * Bloquear edición
        self.pre.config(state=tk.DISABLED)
        self.ino.config(state=tk.DISABLED)
        self.pos.config(state=tk.DISABLED)

        # * Dibujar árbol
        self.renderizador.dibujar(self.arbol, self.ultimo_agregado)

    # ============================
    # SALIR DEL SISTEMA
    # ============================
    def salir(self):

        # * Mostrar diálogo de confirmación antes de cerrar
        if messagebox.askyesno(
            "Confirmar Salida",
            "¿Está seguro que desea cerrar la Fase 4 y volver al menú principal?",
        ):

            # * Cerrar ventana principal de la aplicación
            self.ventana.destroy()
