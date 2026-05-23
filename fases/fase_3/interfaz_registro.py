# ============================
# * IMPORTACIONES
# ============================

# * Librería principal para construir interfaces gráficas
import tkinter as tk

# * Componentes adicionales de Tkinter:
# * ttk -> widgets modernos
# * messagebox -> ventanas emergentes
from tkinter import ttk, messagebox

# * Permite trabajar con fechas
from datetime import datetime

# * Calendario visual para seleccionar fechas
from tkcalendar import DateEntry

# * Clase principal que representa la estructura de datos
# * de cada afiliado registrado
from fases.fase_3.estructura_datos_afiliado import EstructuraDatosAfiliado

# ============================
# * CLASE REGISTRO
# ============================


class RegistroApp:

    # * CONSTANTES VISUALES:
    # * Definen colores principales utilizados
    # * en la interfaz gráfica.
    COLOR_FONDO = "#f8f9fa"
    COLOR_PRIMARIO = "#1a73e8"
    COLOR_EXITO = "#34a853"
    COLOR_PELIGRO = "#ea4335"
    COLOR_BLANCO = "#ffffff"

    # ! CONSTRUCTOR PRINCIPAL:
    # ? Inicializa ventana, estructuras
    # ? de datos y componentes gráficos.
    def __init__(self):

        # * Crear ventana secundaria
        self.ventana = tk.Toplevel()

        # * Título principal
        self.ventana.title("Caja Compensándote - Afiliados")

        # * Maximizar ventana automáticamente
        try:
            self.ventana.state("zoomed")

        # ? Compatibilidad si el sistema no soporta zoom
        except:
            self.ventana.geometry("1100x800")

        self.ventana.configure(bg=self.COLOR_FONDO)

        # ============================
        # * ESTRUCTURAS DE DATOS
        # ============================

        # * PILA -> comportamiento LIFO
        self.pila = []

        # * COLA -> comportamiento FIFO
        self.cola = []

        # * LISTA -> almacenamiento general
        self.lista = []

        # * Configuración inicial
        self.centrar_ventana()
        self.crear_widgets()

    # ============================
    # * CENTRAR VENTANA
    # ============================

    # ? Posiciona la ventana al centro
    # ? de la pantalla automáticamente.
    def centrar_ventana(self):

        self.ventana.update_idletasks()

        w = self.ventana.winfo_width()
        h = self.ventana.winfo_height()

        x = (self.ventana.winfo_screenwidth() // 2) - (w // 2)
        y = (self.ventana.winfo_screenheight() // 2) - (h // 2)

        self.ventana.geometry(f"{w}x{h}+{x}+{y}")

    # ============================
    # * CREACIÓN INTERFAZ
    # ============================

    # ? Construye todos los componentes
    # ? visuales del formulario.
    def crear_widgets(self):

        # ============================
        # * HEADER
        # ============================

        header = tk.Frame(self.ventana, bg=self.COLOR_PRIMARIO, height=70)

        header.pack(fill="x")

        tk.Label(
            header,
            text="GESTIÓN DE AFILIADOS - COMPENSÁNDOTE",
            bg=self.COLOR_PRIMARIO,
            fg="white",
            font=("Segoe UI", 16, "bold"),
        ).pack(pady=18)

        # ============================
        # * FORMULARIO PRINCIPAL
        # ============================

        form = tk.LabelFrame(
            self.ventana, text="Formulario de Registro", bg=self.COLOR_BLANCO
        )

        form.pack(fill="x", padx=20, pady=15)

        form.columnconfigure((1, 3), weight=1)

        # ============================
        # * FILA 1
        # ============================

        # * Tipo identificación
        tk.Label(form, text="Tipo de Identificación", bg=self.COLOR_BLANCO).grid(
            row=0, column=0, sticky="w", padx=10, pady=5
        )

        self.tipo_id = ttk.Combobox(form, values=["CC", "CE", "TI", "PAS"])

        self.tipo_id.grid(row=0, column=1, sticky="ew", padx=10)

        # * Número identificación
        tk.Label(form, text="Nro. de Identificación", bg=self.COLOR_BLANCO).grid(
            row=0, column=2, sticky="w", padx=10
        )

        self.num_id = tk.Entry(form)

        self.num_id.grid(row=0, column=3, sticky="ew", padx=10)

        # ============================
        # * FILA 2
        # ============================

        # * Nombre afiliado
        tk.Label(form, text="Nombre Completo", bg=self.COLOR_BLANCO).grid(
            row=1, column=0, sticky="w", padx=10, pady=5
        )

        self.nombre = tk.Entry(form)

        self.nombre.grid(row=1, column=1, sticky="ew", padx=10)

        # * Ingresos actuales
        tk.Label(form, text="Ingresos Actuales", bg=self.COLOR_BLANCO).grid(
            row=1, column=2, sticky="w", padx=10
        )

        self.ingresos_var = tk.StringVar()

        self.ingresos = tk.Entry(form, textvariable=self.ingresos_var)

        self.ingresos.grid(row=1, column=3, sticky="ew", padx=10)

        # ! EVENTO AUTOMÁTICO:
        # ? Recalcula tarifa cuando cambia ingreso.
        self.ingresos_var.trace_add("write", self.actualizar_tarifa)

        # ============================
        # * FILA 3
        # ============================

        # * Servicio solicitado
        tk.Label(form, text="Servicios Deseados", bg=self.COLOR_BLANCO).grid(
            row=2, column=0, sticky="w", padx=10, pady=5
        )

        self.servicio = ttk.Combobox(
            form,
            values=[
                "Subsidio de desempleo",
                "Ingreso a parque",
                "Curso de formación",
                "Paquete de viaje",
                "Medicina preventiva",
            ],
        )

        self.servicio.grid(row=2, column=1, sticky="ew", padx=10)

        # ! EVENTO:
        # ? Actualiza tarifa al cambiar servicio.
        self.servicio.bind("<<ComboboxSelected>>", self.actualizar_tarifa)

        # ============================
        # * MODALIDAD EMPLEO
        # ============================

        mode_frame = tk.Frame(form, bg=self.COLOR_BLANCO)

        self.modalidad = tk.StringVar(value="None")

        # * RadioButton empleado
        tk.Radiobutton(
            mode_frame,
            text="Empleado",
            variable=self.modalidad,
            value="Empleado",
            command=self.actualizar_tarifa,
        ).pack(side="left")

        # * RadioButton independiente
        tk.Radiobutton(
            mode_frame,
            text="Independiente",
            variable=self.modalidad,
            value="Independiente",
            command=self.actualizar_tarifa,
        ).pack(side="left")

        # ! El resto continúa igual:
        # ? estructura de datos
        # ? tabla TreeView
        # ? botones
        # ? reportes
        # ? eventos
        # ? eliminación
