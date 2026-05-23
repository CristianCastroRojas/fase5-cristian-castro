# * IMPORTACIONES INTERFAZ
import tkinter as tk
from tkinter import ttk, messagebox

# * IMPORTACIONES LÓGICA NEGOCIO
from fases.fase_2.gestion_empleados import GestionEmpleados
from fases.fase_2.interfaz_reporte import ReporteApp

# * IMPORTACIÓN CONSTANTES VISUALES
# ? Variables de configuración colores y estilos
from config.fase_2.constantes import (
    TITULO_REGISTRO,
    COLOR_FONDO,
    COLOR_PRIMARIO,
    COLOR_SECUNDARIO,
    COLOR_BLANCO,
    COLOR_ACENTO,
    COLOR_BORDE,
)


# * CLASE PRINCIPAL REGISTRO
# ? Administra formulario registro empleados
class RegistroApp:

    # * VARIABLES TEMA VISUAL
    # ? Centraliza configuración colores interfaz
    COLOR_FONDO = COLOR_FONDO
    COLOR_PRIMARIO = COLOR_PRIMARIO
    COLOR_SECUNDARIO = COLOR_SECUNDARIO
    COLOR_BLANCO = COLOR_BLANCO
    COLOR_ACENTO = COLOR_ACENTO
    COLOR_BORDE = COLOR_BORDE

    # * CONSTRUCTOR PRINCIPAL
    def __init__(self, parent=None):

        # * CREACIÓN VENTANA REGISTRO
        self.ventana = tk.Toplevel(parent) if parent else tk.Toplevel()

        # * CONFIGURACIÓN GENERAL VENTANA
        self.ventana.title(TITULO_REGISTRO)
        self.ventana.geometry("600x700")
        self.ventana.configure(bg=self.COLOR_FONDO)
        self.ventana.resizable(False, False)

        # ? Objeto empleado inicialmente vacío
        self.empleado = None

        # * CONFIGURACIÓN INICIAL INTERFAZ
        self.centrar_ventana()
        self.configurar_estilos()
        self.crear_widgets()

    # * CENTRAR VENTANA
    # ? Calcula posición pantalla automáticamente
    def centrar_ventana(self):

        self.ventana.update_idletasks()

        ancho = self.ventana.winfo_width()
        alto = self.ventana.winfo_height()

        x = (self.ventana.winfo_screenwidth() // 2) - (ancho // 2)

        y = (self.ventana.winfo_screenheight() // 2) - (alto // 2)

        self.ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

    # * CONFIGURACIÓN COMPONENTES VISUALES
    # ? Personaliza widgets ttk
    def configurar_estilos(self):

        style = ttk.Style()

        style.theme_use("clam")

        style.configure(
            "TCombobox",
            fieldbackground=self.COLOR_BLANCO,
            background=self.COLOR_BLANCO,
        )

        style.configure(
            "Custom.TFrame",
            background=self.COLOR_BLANCO,
        )

    # * CONSTRUCCIÓN INTERFAZ
    def crear_widgets(self):

        # * CABECERA PRINCIPAL
        header_frame = tk.Frame(
            self.ventana,
            bg=self.COLOR_PRIMARIO,
            height=80,
        )

        header_frame.pack(fill="x")

        header_frame.pack_propagate(False)

        # ? Título principal aplicación
        lbl_titulo = tk.Label(
            header_frame,
            text="REGISTRO DE EMPLEADO",
            font=("Segoe UI", 18, "bold"),
            bg=self.COLOR_PRIMARIO,
            fg=self.COLOR_BLANCO,
        )

        lbl_titulo.pack(pady=20)

        # * CONTENEDOR FORMULARIO
        container = tk.Frame(
            self.ventana,
            bg=self.COLOR_BLANCO,
            bd=0,
            highlightthickness=1,
            highlightbackground="#dadce0",
        )

        container.pack(
            pady=30,
            padx=40,
            fill="both",
            expand=True,
        )

        content_frame = tk.Frame(
            container,
            bg=self.COLOR_BLANCO,
            padx=30,
            pady=20,
        )

        content_frame.pack(
            fill="both",
            expand=True,
        )

        # * FUNCIÓN AUXILIAR CAMPOS
        # ? Evita repetir código formularios
        def crear_campo(
            parent,
            text,
            row,
            widget_type="entry",
            options=None,
        ): ...

        # * CAMPOS INFORMACIÓN EMPLEADO

        self.entry_id = crear_campo(
            content_frame,
            "Identificación / CC:",
            0,
        )

        self.entry_nombre = crear_campo(
            content_frame,
            "Nombre Completo:",
            2,
        )

        # * SELECCIÓN GÉNERO

        self.genero_var = tk.StringVar(value="Masculino")

        # ? RadioButton permite selección única

        # * CARGO LABORAL

        # ? Lista obtenida desde GestiónEmpleados
        self.combo_cargo.bind(
            "<<ComboboxSelected>>",
            self.actualizar_valor_dia,
        )

        # * DÍAS LABORADOS Y VALOR DÍA

        # ? Valor día calculado automáticamente

        # * BOTONES ACCIÓN

        # ? Guardar datos
        # ? Mostrar reporte
        # ? Salir interfaz

    # * ACTUALIZAR VALOR DÍA
    # ? Consulta valor según cargo seleccionado
    def actualizar_valor_dia(self, event=None):

        cargo = self.cargo_var.get()

        valor = GestionEmpleados.VALORES_POR_CARGO.get(
            cargo,
            0,
        )

        self.entry_valor_dia.config(state="normal")

        self.entry_valor_dia.delete(
            0,
            tk.END,
        )

        self.entry_valor_dia.insert(
            0,
            f"$ {valor:,.0f}",
        )

        self.entry_valor_dia.config(state="disabled")

    # * GUARDAR INFORMACIÓN EMPLEADO
    def guardar_registro(self):

        try:

            # ! Validación días laborados
            dias_str = self.entry_dias.get()

            if not dias_str:

                raise ValueError("Debe ingresar los días laborados")

            # ? Conversión texto entero
            dias = int(dias_str)

            # * CREACIÓN OBJETO EMPLEADO
            self.empleado = GestionEmpleados(
                identificacion=self.entry_id.get().strip(),
                nombre_completo=self.entry_nombre.get().strip(),
                genero=self.genero_var.get(),
                cargo=self.cargo_var.get(),
                dias_laborados=dias,
            )

            # * CONFIRMACIÓN REGISTRO
            messagebox.showinfo(
                "Registro Exitoso",
                f"Los datos del empleado "
                f"{self.empleado.nombre_completo} "
                f"han sido guardados.",
            )

            # ? Reinicia formulario
            self.limpiar_campos()

        # ! Errores validación negocio
        except ValueError as e:

            messagebox.showerror(
                "Error de Validación",
                str(e),
            )

        # ! Errores inesperados sistema
        except Exception as e:

            messagebox.showerror(
                "Error Inesperado",
                f"Ocurrió un error: {str(e)}",
            )

    # * MOSTRAR REPORTE
    def mostrar_reporte(self):

        # ! Validar empleado existente
        if self.empleado is None:

            messagebox.showwarning(
                "Faltan Datos",
                "Primero debe completar y guardar " "el registro del empleado.",
            )

            return

        # * Abrir ventana reporte
        ReporteApp(
            self.empleado,
            parent=self.ventana,
        )

    # * CERRAR VENTANA
    def salir(self):

        # ? Solicita confirmación usuario
        if messagebox.askyesno(
            "Confirmar Salida",
            "¿Está seguro que desea cerrar " "la Fase 2 y volver al menú principal?",
        ):

            self.ventana.destroy()

    # * LIMPIAR FORMULARIO
    # ? Reinicia todos los campos
    def limpiar_campos(self):

        self.entry_id.delete(0, tk.END)

        self.entry_nombre.delete(0, tk.END)

        self.genero_var.set("Masculino")

        self.combo_cargo.set("")

        self.entry_dias.delete(0, tk.END)

        self.entry_valor_dia.config(state="normal")

        self.entry_valor_dia.delete(
            0,
            tk.END,
        )

        self.entry_valor_dia.config(state="disabled")
