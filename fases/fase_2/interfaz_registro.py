# ============================
# IMPORTACIONES
# ============================
import tkinter as tk
from tkinter import ttk, messagebox

# ? Lógica de negocio (gestión de empleados)
from fases.fase_2.gestion_empleados import GestionEmpleados

# ? Interfaz de reporte (fase 2)
from fases.fase_2.interfaz_reporte import ReporteApp

# ? Constantes de diseño de la interfaz
from config.fase_2.constantes import (
    TITULO_REGISTRO,
    COLOR_FONDO,
    COLOR_PRIMARIO,
    COLOR_SECUNDARIO,
    COLOR_BLANCO,
    COLOR_ACENTO,
    COLOR_BORDE,
)


# ============================
# CLASE PRINCIPAL DE REGISTRO
# ============================
class RegistroApp:

    # ? Colores usados en la interfaz (tema visual)
    COLOR_FONDO = COLOR_FONDO
    COLOR_PRIMARIO = COLOR_PRIMARIO
    COLOR_SECUNDARIO = COLOR_SECUNDARIO
    COLOR_BLANCO = COLOR_BLANCO
    COLOR_ACENTO = COLOR_ACENTO
    COLOR_BORDE = COLOR_BORDE

    # ============================
    # INICIALIZACIÓN DE LA VENTANA
    # ============================
    def __init__(self, parent=None):

        # * Crear ventana secundaria
        self.ventana = tk.Toplevel(parent) if parent else tk.Toplevel()
        self.ventana.title(TITULO_REGISTRO)
        self.ventana.geometry("600x700")
        self.ventana.configure(bg=self.COLOR_FONDO)
        self.ventana.resizable(False, False)

        # * Variable para almacenar empleado
        self.empleado = None

        # * Construcción de interfaz
        self.centrar_ventana()
        self.configurar_estilos()
        self.crear_widgets()

    # ============================
    # CENTRAR VENTANA
    # ============================
    def centrar_ventana(self):

        # * Centra la ventana en la pantalla
        self.ventana.update_idletasks()

        ancho = self.ventana.winfo_width()
        alto = self.ventana.winfo_height()

        x = (self.ventana.winfo_screenwidth() // 2) - (ancho // 2)
        y = (self.ventana.winfo_screenheight() // 2) - (alto // 2)

        self.ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

    # ============================
    # CONFIGURACIÓN DE ESTILOS
    # ============================
    def configurar_estilos(self):

        # * Estilos personalizados de ttk
        style = ttk.Style()
        style.theme_use("clam")

        style.configure(
            "TCombobox",
            fieldbackground=self.COLOR_BLANCO,
            background=self.COLOR_BLANCO,
        )

        style.configure("Custom.TFrame", background=self.COLOR_BLANCO)

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
            text="REGISTRO DE EMPLEADO",
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
            bd=0,
            highlightthickness=1,
            highlightbackground="#dadce0",
        )
        container.pack(pady=30, padx=40, fill="both", expand=True)

        content_frame = tk.Frame(container, bg=self.COLOR_BLANCO, padx=30, pady=20)
        content_frame.pack(fill="both", expand=True)

        # ============================
        # HELPER PARA CAMPOS
        # ============================
        def crear_campo(parent, text, row, widget_type="entry", options=None):

            # * Etiqueta del campo
            tk.Label(
                parent,
                text=text,
                font=("Segoe UI", 10, "bold"),
                bg=self.COLOR_BLANCO,
                fg=self.COLOR_SECUNDARIO,
            ).grid(row=row, column=0, sticky="w", pady=(15, 5))

            # * Campo tipo Entry
            if widget_type == "entry":
                entry = tk.Entry(
                    parent,
                    font=("Segoe UI", 11),
                    bg="#f1f3f4",
                    bd=0,
                    highlightthickness=1,
                    highlightbackground="#dadce0",
                )
                entry.grid(row=row + 1, column=0, sticky="ew", ipady=5)
                return entry

            # * Campo tipo ComboBox
            elif widget_type == "combo":
                var = tk.StringVar()
                combo = ttk.Combobox(
                    parent,
                    textvariable=var,
                    font=("Segoe UI", 11),
                    state="readonly",
                )
                combo["values"] = options
                combo.grid(row=row + 1, column=0, sticky="ew")
                return combo, var

        # ============================
        # CAMPOS DEL FORMULARIO
        # ============================
        self.entry_id = crear_campo(content_frame, "Identificación / CC:", 0)
        self.entry_nombre = crear_campo(content_frame, "Nombre Completo:", 2)

        # ================================================
        # SECCIÓN: GÉNERO
        # ================================================

        # * Etiqueta del campo género
        tk.Label(
            content_frame,
            text="Género:",
            font=("Segoe UI", 10, "bold"),
            bg=self.COLOR_BLANCO,
            fg=self.COLOR_SECUNDARIO,
        ).grid(row=4, column=0, sticky="w", pady=(15, 5))

        # * Variable que almacena el género seleccionado
        self.genero_var = tk.StringVar(value="Masculino")

        # * Contenedor de opciones (radio buttons)
        genero_frame = tk.Frame(content_frame, bg=self.COLOR_BLANCO)
        genero_frame.grid(row=5, column=0, sticky="w")

        # * Opción Masculino
        tk.Radiobutton(
            genero_frame,
            text="Masculino",
            variable=self.genero_var,
            value="Masculino",
            bg=self.COLOR_BLANCO,
            font=("Segoe UI", 10),
            activebackground=self.COLOR_BLANCO,
        ).pack(side="left", padx=(0, 20))

        # * Opción Femenino
        tk.Radiobutton(
            genero_frame,
            text="Femenino",
            variable=self.genero_var,
            value="Femenino",
            bg=self.COLOR_BLANCO,
            font=("Segoe UI", 10),
            activebackground=self.COLOR_BLANCO,
        ).pack(side="left")

        # ================================================
        # SECCIÓN: CARGO
        # ================================================

        # * ComboBox de cargos laborales
        self.combo_cargo, self.cargo_var = crear_campo(
            content_frame,
            "Cargo Laboral:",
            6,
            "combo",
            list(GestionEmpleados.VALORES_POR_CARGO.keys()),
        )

        # * Evento: actualiza valor del día al cambiar cargo
        self.combo_cargo.bind("<<ComboboxSelected>>", self.actualizar_valor_dia)

        # ================================================
        # SECCIÓN: DÍAS LABORADOS Y VALOR POR DÍA
        # ================================================

        # * Contenedor de dos columnas
        row_7 = tk.Frame(content_frame, bg=self.COLOR_BLANCO)
        row_7.grid(row=8, column=0, sticky="ew", pady=(15, 0))

        row_7.columnconfigure(0, weight=1)
        row_7.columnconfigure(1, weight=1)

        # * Etiqueta días laborados
        tk.Label(
            row_7,
            text="Días Laborados:",
            font=("Segoe UI", 10, "bold"),
            bg=self.COLOR_BLANCO,
            fg=self.COLOR_SECUNDARIO,
        ).grid(row=0, column=0, sticky="w")

        # * Etiqueta valor por día
        tk.Label(
            row_7,
            text="Valor por Día:",
            font=("Segoe UI", 10, "bold"),
            bg=self.COLOR_BLANCO,
            fg=self.COLOR_SECUNDARIO,
        ).grid(row=0, column=1, sticky="w")

        # * Entrada de días trabajados
        self.entry_dias = tk.Entry(
            row_7,
            font=("Segoe UI", 11),
            bg="#f1f3f4",
            bd=0,
            highlightthickness=1,
            highlightbackground="#dadce0",
        )
        self.entry_dias.grid(row=1, column=0, sticky="ew", padx=(0, 10), ipady=5)

        # * Campo de solo lectura para valor del día
        self.entry_valor_dia = tk.Entry(
            row_7,
            font=("Segoe UI", 11),
            bg="#e8eaed",
            bd=0,
            state="disabled",
            highlightthickness=1,
            highlightbackground="#dadce0",
        )
        self.entry_valor_dia.grid(row=1, column=1, sticky="ew", ipady=5)

        # * Permitir que la columna se expanda correctamente
        content_frame.columnconfigure(0, weight=1)

        # ================================================
        # SECCIÓN: BOTONES DE ACCIÓN
        # ================================================

        # * Contenedor de botones inferiores
        actions_frame = tk.Frame(self.ventana, bg=self.COLOR_FONDO)
        actions_frame.pack(fill="x", padx=40, pady=(0, 30))

        # * Función auxiliar para crear botones
        def crear_boton(parent, text, cmd, color, fg=self.COLOR_BLANCO):
            btn = tk.Button(
                parent,
                text=text,
                command=cmd,
                font=("Segoe UI", 10, "bold"),
                bg=color,
                fg=fg,
                bd=0,
                padx=15,
                pady=8,
                cursor="hand2",
                activebackground=color,
                activeforeground=fg,
            )
            return btn

        # * Botón: guardar registro
        self.btn_guardar = crear_boton(
            actions_frame,
            "Guardar Registro",
            self.guardar_registro,
            self.COLOR_PRIMARIO,
        )
        self.btn_guardar.pack(side="left", fill="x", expand=True, padx=5)

        # * Botón: calcular nómina / mostrar reporte
        self.btn_reporte = crear_boton(
            actions_frame,
            "Calcular Nomina/Mostrar Reporte",
            self.mostrar_reporte,
            "#34a853",
        )
        self.btn_reporte.pack(side="left", fill="x", expand=True, padx=5)

        # * Botón: salir del sistema
        self.btn_salir = crear_boton(
            actions_frame,
            "Salir",
            self.salir,
            "#ea4335",
        )
        self.btn_salir.pack(side="left", fill="x", expand=True, padx=5)

    # ================================================
    # MÉTODO: ACTUALIZAR VALOR POR DÍA
    # ================================================
    def actualizar_valor_dia(self, event=None):

        # * Obtiene el cargo seleccionado en el combo
        cargo = self.cargo_var.get()

        # * Busca el valor diario según el cargo
        valor = GestionEmpleados.VALORES_POR_CARGO.get(cargo, 0)

        # * Habilita el campo para poder modificarlo
        self.entry_valor_dia.config(state="normal")

        # * Limpia el campo
        self.entry_valor_dia.delete(0, tk.END)

        # * Inserta el valor formateado como moneda
        self.entry_valor_dia.insert(0, f"$ {valor:,.0f}")

        # * Vuelve a dejarlo como solo lectura
        self.entry_valor_dia.config(state="disabled")

    # ================================================
    # MÉTODO: GUARDAR REGISTRO
    # ================================================
    def guardar_registro(self):

        try:
            # * Obtener días laborados desde la interfaz
            dias_str = self.entry_dias.get()

            # * Validar campo vacío
            if not dias_str:
                raise ValueError("Debe ingresar los días laborados")

            # * Convertir a entero
            dias = int(dias_str)

            # * Crear objeto empleado con los datos ingresados
            self.empleado = GestionEmpleados(
                identificacion=self.entry_id.get().strip(),
                nombre_completo=self.entry_nombre.get().strip(),
                genero=self.genero_var.get(),
                cargo=self.cargo_var.get(),
                dias_laborados=dias,
            )

            # * Mensaje de confirmación
            messagebox.showinfo(
                "Registro Exitoso",
                f"Los datos del empleado {self.empleado.nombre_completo} han sido guardados.",
            )

            # * Limpiar campos después del registro
            self.limpiar_campos()

        except ValueError as e:
            # * Errores de validación de datos
            messagebox.showerror("Error de Validación", str(e))

        except Exception as e:
            # * Errores inesperados del sistema
            messagebox.showerror("Error Inesperado", f"Ocurrió un error: {str(e)}")

    # ================================================
    # MÉTODO: MOSTRAR REPORTE
    # ================================================
    def mostrar_reporte(self):

        # * Verifica si hay un empleado registrado
        if self.empleado is None:
            messagebox.showwarning(
                "Faltan Datos",
                "Primero debe completar y guardar el registro del empleado.",
            )
            return

        # * Abre la ventana de reporte
        ReporteApp(self.empleado, parent=self.ventana)

    # ================================================
    # MÉTODO: SALIR
    # ================================================
    def salir(self):

        # * Confirmación antes de cerrar la ventana
        if messagebox.askyesno(
            "Confirmar Salida",
            "¿Está seguro que desea cerrar la Fase 2 y volver al menú principal?",
        ):
            self.ventana.destroy()

    # ================================================
    # MÉTODO: LIMPIAR CAMPOS
    # ================================================
    def limpiar_campos(self):

        # * Limpia todos los campos del formulario
        self.entry_id.delete(0, tk.END)
        self.entry_nombre.delete(0, tk.END)

        # * Reinicia el género por defecto
        self.genero_var.set("Masculino")

        # * Limpia el combo de cargo
        self.combo_cargo.set("")

        # * Limpia días laborados
        self.entry_dias.delete(0, tk.END)

        # * Limpia valor por día (campo bloqueado)
        self.entry_valor_dia.config(state="normal")
        self.entry_valor_dia.delete(0, tk.END)
        self.entry_valor_dia.config(state="disabled")
