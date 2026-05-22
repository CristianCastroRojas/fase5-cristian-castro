# ============================
# IMPORTACIONES
# ============================
import tkinter as tk
from fases.fase_2.gestion_empleados import GestionEmpleados
from config.fase_2.constantes import (
    TITULO_REPORTE,
    COLOR_FONDO,
    COLOR_PRIMARIO,
    COLOR_TEXTO,
    COLOR_SECUNDARIO,
    COLOR_BLANCO,
)


class ReporteApp:
    # ================================================
    # CONSTANTES DEFINIDAS COMO VARIABLES PARA EL TEMA
    # ================================================
    COLOR_FONDO = COLOR_FONDO
    COLOR_PRIMARIO = COLOR_PRIMARIO
    COLOR_TEXTO = COLOR_TEXTO
    COLOR_SECUNDARIO = COLOR_SECUNDARIO
    COLOR_BLANCO = COLOR_BLANCO

    def __init__(self, empleado, parent=None):
        if parent is not None and hasattr(parent, "ventana"):
            window_parent = parent.ventana
        else:
            window_parent = parent
        self.ventana = tk.Toplevel(window_parent)
        self.ventana.title(TITULO_REPORTE)
        self.ventana.geometry("500x700")
        self.ventana.configure(bg=self.COLOR_FONDO)
        self.ventana.resizable(False, False)

        self.empleado = empleado
        self.parent = parent

        self.centrar_ventana()
        self.crear_widgets()

    def centrar_ventana(self):
        self.ventana.update_idletasks()
        ancho = self.ventana.winfo_width()
        alto = self.ventana.winfo_height()
        x = (self.ventana.winfo_screenwidth() // 2) - (ancho // 2)
        y = (self.ventana.winfo_screenheight() // 2) - (alto // 2)
        self.ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

    def crear_widgets(self):

        # ================================================
        # HEADER
        # ================================================
        header_frame = tk.Frame(self.ventana, bg=self.COLOR_PRIMARIO, height=80)
        header_frame.pack(fill="x")
        header_frame.pack_propagate(False)

        lbl_titulo = tk.Label(
            header_frame,
            text="RESUMEN DE PAGO",
            font=("Segoe UI", 18, "bold"),
            bg=self.COLOR_PRIMARIO,
            fg=self.COLOR_BLANCO,
        )
        lbl_titulo.pack(pady=20)

        # ================================================
        # CONTENEDOR PRINCIPAL
        # ================================================
        container = tk.Frame(
            self.ventana,
            bg=self.COLOR_BLANCO,
            highlightthickness=1,
            highlightbackground=self.COLOR_SECUNDARIO,
        )
        container.pack(pady=20, padx=40, fill="both")

        content_frame = tk.Frame(container, bg=self.COLOR_BLANCO, padx=25, pady=25)
        content_frame.pack(fill="both")

        datos = self.empleado.generar_reporte()

        # ================================================
        # CAMPOS DE INFORMACIÓN
        # ================================================
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

        # ================================================
        # SEPARADOR
        # ================================================
        tk.Frame(content_frame, height=1, bg=self.COLOR_SECUNDARIO).grid(
            row=fila, column=0, sticky="ew", pady=15
        )

        fila += 1

        # ================================================
        # TOTAL A PAGAR
        # ================================================
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

        # ================================================
        # BOTÓN NUEVO REGISTRO
        # ================================================
        btn_volver = tk.Button(
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
        )
        btn_volver.pack(pady=(0, 20))

    def volver(self):
        self.ventana.destroy()
        if self.parent:
            self.parent.limpiar_campos()
