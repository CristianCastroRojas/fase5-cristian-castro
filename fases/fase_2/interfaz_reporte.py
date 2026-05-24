# ============================
# IMPORTACIONES
# ============================
import tkinter as tk

# ? Lógica de negocio de empleados (cálculo de nómina y datos)
from fases.fase_2.gestion_empleados import GestionEmpleados

# ? Constantes de diseño para la interfaz del reporte
from config.fase_2.constantes import (
    TITULO_REPORTE,
    COLOR_FONDO,
    COLOR_PRIMARIO,
    COLOR_TEXTO,
    COLOR_SECUNDARIO,
    COLOR_BLANCO,
)


# ============================
# CLASE: VENTANA DE REPORTE
# ============================
class ReporteApp:

    # ? Variables de estilo (tema visual)
    COLOR_FONDO = COLOR_FONDO
    COLOR_PRIMARIO = COLOR_PRIMARIO
    COLOR_TEXTO = COLOR_TEXTO
    COLOR_SECUNDARIO = COLOR_SECUNDARIO
    COLOR_BLANCO = COLOR_BLANCO

    # ============================
    # INICIALIZACIÓN
    # ============================
    def __init__(self, empleado, parent=None):

        # * Obtener ventana padre si existe
        if parent is not None and hasattr(parent, "ventana"):
            window_parent = parent.ventana
        else:
            window_parent = parent

        # * Crear ventana secundaria del reporte
        self.ventana = tk.Toplevel(window_parent)
        self.ventana.title(TITULO_REPORTE)
        self.ventana.geometry("500x700")
        self.ventana.configure(bg=self.COLOR_FONDO)
        self.ventana.resizable(False, False)

        # * Datos del empleado a mostrar
        self.empleado = empleado
        self.parent = parent

        # * Construcción de interfaz
        self.centrar_ventana()
        self.crear_widgets()

    # ============================
    # CENTRAR VENTANA
    # ============================
    def centrar_ventana(self):

        # * Centra la ventana en pantalla
        self.ventana.update_idletasks()

        ancho = self.ventana.winfo_width()
        alto = self.ventana.winfo_height()

        x = (self.ventana.winfo_screenwidth() // 2) - (ancho // 2)
        y = (self.ventana.winfo_screenheight() // 2) - (alto // 2)

        self.ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

    # ============================
    # CREACIÓN DE INTERFAZ
    # ============================
    def crear_widgets(self):

        # ============================
        # HEADER
        # ============================
        header_frame = tk.Frame(self.ventana, bg=self.COLOR_PRIMARIO, height=80)
        header_frame.pack(fill="x")
        header_frame.pack_propagate(False)

        tk.Label(
            header_frame,
            text="RESUMEN DE PAGO",
            font=("Segoe UI", 18, "bold"),
            bg=self.COLOR_PRIMARIO,
            fg=self.COLOR_BLANCO,
        ).pack(pady=20)

        # ============================
        # CONTENEDOR PRINCIPAL
        # ============================
        container = tk.Frame(
            self.ventana,
            bg=self.COLOR_BLANCO,
            highlightthickness=1,
            highlightbackground=self.COLOR_SECUNDARIO,
        )
        container.pack(pady=20, padx=40, fill="both")

        content_frame = tk.Frame(container, bg=self.COLOR_BLANCO, padx=25, pady=25)
        content_frame.pack(fill="both")

        # * Obtener datos del empleado en formato diccionario
        datos = self.empleado.generar_reporte()

        # ============================
        # CAMPOS DEL REPORTE
        # ============================
        campos = [
            ("Fecha Reporte:", datos["fecha_registro"]),
            ("Identificación:", datos["identificacion"]),
            ("Nombre Empleado:", datos["nombre"]),
            ("Género:", datos["genero"]),
            ("Cargo Desempeñado:", datos["cargo"]),
            ("Días Laborados:", f"{datos['dias_laborados']} días"),
            ("Valor del Día:", f"$ {datos['valor_dia']:,.0f}"),
        ]

        fila = 0

        # * Renderiza cada campo en pantalla
        for label, valor in campos:

            tk.Label(
                content_frame,
                text=label,
                font=("Segoe UI", 9, "bold"),
                bg=self.COLOR_BLANCO,
                fg=self.COLOR_SECUNDARIO,
            ).grid(row=fila, column=0, sticky="w", pady=(10, 0))

            fila += 1

            tk.Label(
                content_frame,
                text=valor,
                font=("Segoe UI", 11),
                bg=self.COLOR_BLANCO,
                fg=self.COLOR_TEXTO,
            ).grid(row=fila, column=0, sticky="w", pady=(0, 5))

            fila += 1

        # ============================
        # SEPARADOR VISUAL
        # ============================
        tk.Frame(
            content_frame,
            height=1,
            bg=self.COLOR_SECUNDARIO,
        ).grid(row=fila, column=0, sticky="ew", pady=15)

        fila += 1

        # ============================
        # TOTAL A PAGAR
        # ============================
        tk.Label(
            content_frame,
            text="TOTAL NETO A PAGAR:",
            font=("Segoe UI", 11, "bold"),
            bg=self.COLOR_BLANCO,
            fg=self.COLOR_PRIMARIO,
        ).grid(row=fila, column=0, sticky="w")

        fila += 1

        tk.Label(
            content_frame,
            text=f"$ {datos['total_pagar']:,.0f}",
            font=("Segoe UI", 20, "bold"),
            bg=self.COLOR_BLANCO,
            fg=self.COLOR_TEXTO,
        ).grid(row=fila, column=0, sticky="w")

        content_frame.columnconfigure(0, weight=1)

        # ============================
        # BOTÓN: NUEVO REGISTRO
        # ============================
        tk.Button(
            self.ventana,
            text="NUEVO REGISTRO",
            command=self.volver,
            font=("Segoe UI", 10, "bold"),
            bg=self.COLOR_PRIMARIO,
            fg=self.COLOR_BLANCO,
            activebackground=self.COLOR_PRIMARIO,
            activeforeground=self.COLOR_BLANCO,
            bd=0,
            padx=30,
            pady=12,
            cursor="hand2",
        ).pack(pady=(0, 20))

    # ============================
    # VOLVER AL FORMULARIO
    # ============================
    def volver(self):

        # * Cierra la ventana del reporte
        self.ventana.destroy()

        # * Limpia el formulario del padre si existe
        if self.parent:
            self.parent.limpiar_campos()
