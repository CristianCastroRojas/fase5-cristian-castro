# ============================
# IMPORTACIONES
# ============================
import tkinter as tk
from tkinter import ttk, messagebox

from fases.fase_2.gestion_empleados import GestionEmpleados
from fases.fase_2.interfaz_reporte import ReporteApp
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
# CLASE E INTERFAZ DE REGISTRO
# ============================
class RegistroApp:
    # ================================================
    # CONSTANTES DEFINIDAS COMO VARIABLES PARA EL TEMA
    # ================================================
    COLOR_FONDO = COLOR_FONDO
    COLOR_PRIMARIO = COLOR_PRIMARIO
    COLOR_SECUNDARIO = COLOR_SECUNDARIO
    COLOR_BLANCO = COLOR_BLANCO
    COLOR_ACENTO = COLOR_ACENTO
    COLOR_BORDE = COLOR_BORDE

    # ================================================
    # DEFINICION DE METODOS
    # ================================================
    def __init__(self, parent=None):
        self.ventana = tk.Toplevel(parent) if parent else tk.Toplevel()
        self.ventana.title(TITULO_REGISTRO)
        self.ventana.geometry("600x700")
        self.ventana.configure(bg=self.COLOR_FONDO)
        self.ventana.resizable(False, False)

        self.empleado = None

        self.centrar_ventana()
        self.configurar_estilos()
        self.crear_widgets()

    # ================================================
    # METODOS DE LA CLASE
    # ================================================
    def centrar_ventana(self):
        self.ventana.update_idletasks()
        ancho = self.ventana.winfo_width()
        alto = self.ventana.winfo_height()
        x = (self.ventana.winfo_screenwidth() // 2) - (ancho // 2)
        y = (self.ventana.winfo_screenheight() // 2) - (alto // 2)
        self.ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

    def configurar_estilos(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure(
            "TCombobox", fieldbackground=self.COLOR_BLANCO, background=self.COLOR_BLANCO
        )
        style.configure("Custom.TFrame", background=self.COLOR_BLANCO)

    def crear_widgets(self):
        # ================================================
        # HEADER
        # ================================================
        header_frame = tk.Frame(self.ventana, bg=self.COLOR_PRIMARIO, height=80)
        header_frame.pack(fill="x")
        header_frame.pack_propagate(False)

        lbl_titulo = tk.Label(
            header_frame,
            text="REGISTRO DE EMPLEADO",
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
            bd=0,
            highlightthickness=1,
            highlightbackground="#dadce0",
        )
        container.pack(pady=30, padx=40, fill="both", expand=True)

        content_frame = tk.Frame(container, bg=self.COLOR_BLANCO, padx=30, pady=20)
        content_frame.pack(fill="both", expand=True)

        # Helper para crear etiquetas y campos
        def crear_campo(parent, text, row, widget_type="entry", options=None):
            tk.Label(
                parent,
                text=text,
                font=("Segoe UI", 10, "bold"),
                bg=self.COLOR_BLANCO,
                fg=self.COLOR_SECUNDARIO,
            ).grid(row=row, column=0, sticky="w", pady=(15, 5))

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
            elif widget_type == "combo":
                var = tk.StringVar()
                combo = ttk.Combobox(
                    parent, textvariable=var, font=("Segoe UI", 11), state="readonly"
                )
                combo["values"] = options
                combo.grid(row=row + 1, column=0, sticky="ew")
                return combo, var

        # ================================================
        # CAMPOS
        # ================================================
        self.entry_id = crear_campo(content_frame, "Identificación / CC:", 0)
        self.entry_nombre = crear_campo(content_frame, "Nombre Completo:", 2)

        # ================================================
        # GÉNERO
        # ================================================
        tk.Label(
            content_frame,
            text="Género:",
            font=("Segoe UI", 10, "bold"),
            bg=self.COLOR_BLANCO,
            fg=self.COLOR_SECUNDARIO,
        ).grid(row=4, column=0, sticky="w", pady=(15, 5))

        self.genero_var = tk.StringVar(value="Masculino")
        genero_frame = tk.Frame(content_frame, bg=self.COLOR_BLANCO)
        genero_frame.grid(row=5, column=0, sticky="w")

        tk.Radiobutton(
            genero_frame,
            text="Masculino",
            variable=self.genero_var,
            value="Masculino",
            bg=self.COLOR_BLANCO,
            font=("Segoe UI", 10),
            activebackground=self.COLOR_BLANCO,
        ).pack(side="left", padx=(0, 20))
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
        # CARGO
        # ================================================
        self.combo_cargo, self.cargo_var = crear_campo(
            content_frame,
            "Cargo Laboral:",
            6,
            "combo",
            list(GestionEmpleados.VALORES_POR_CARGO.keys()),
        )
        self.combo_cargo.bind("<<ComboboxSelected>>", self.actualizar_valor_dia)

        # ================================================
        # DÍAS LABORADOS Y VALOR POR DÍA
        # ================================================
        row_7 = tk.Frame(content_frame, bg=self.COLOR_BLANCO)
        row_7.grid(row=8, column=0, sticky="ew", pady=(15, 0))
        row_7.columnconfigure(0, weight=1)
        row_7.columnconfigure(1, weight=1)

        tk.Label(
            row_7,
            text="Días Laborados:",
            font=("Segoe UI", 10, "bold"),
            bg=self.COLOR_BLANCO,
            fg=self.COLOR_SECUNDARIO,
        ).grid(row=0, column=0, sticky="w")
        tk.Label(
            row_7,
            text="Valor por Día:",
            font=("Segoe UI", 10, "bold"),
            bg=self.COLOR_BLANCO,
            fg=self.COLOR_SECUNDARIO,
        ).grid(row=0, column=1, sticky="w")

        self.entry_dias = tk.Entry(
            row_7,
            font=("Segoe UI", 11),
            bg="#f1f3f4",
            bd=0,
            highlightthickness=1,
            highlightbackground="#dadce0",
        )
        self.entry_dias.grid(row=1, column=0, sticky="ew", padx=(0, 10), ipady=5)

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

        content_frame.columnconfigure(0, weight=1)

        # ================================================
        # BOTONES DE ACCIÓN
        # ================================================
        actions_frame = tk.Frame(self.ventana, bg=self.COLOR_FONDO)
        actions_frame.pack(fill="x", padx=40, pady=(0, 30))

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

        self.btn_guardar = crear_boton(
            actions_frame,
            "Guardar Registro",
            self.guardar_registro,
            self.COLOR_PRIMARIO,
        )
        self.btn_guardar.pack(side="left", fill="x", expand=True, padx=5)

        self.btn_reporte = crear_boton(
            actions_frame,
            "Calcular Nomina/Mostrar Reporte",
            self.mostrar_reporte,
            "#34a853",
        )
        self.btn_reporte.pack(side="left", fill="x", expand=True, padx=5)

        self.btn_salir = crear_boton(actions_frame, "Salir", self.salir, "#ea4335")
        self.btn_salir.pack(side="left", fill="x", expand=True, padx=5)

    # ================================================
    # METODO PARA ACTUALIZAR EL VALOR POR DÍA
    # ================================================
    def actualizar_valor_dia(self, event=None):
        cargo = self.cargo_var.get()
        valor = GestionEmpleados.VALORES_POR_CARGO.get(cargo, 0)

        self.entry_valor_dia.config(state="normal")
        self.entry_valor_dia.delete(0, tk.END)
        self.entry_valor_dia.insert(0, f"$ {valor:,.0f}")
        self.entry_valor_dia.config(state="disabled")

    # ================================================
    # METODO PARA GUARDAR EL REGISTRO
    # ================================================
    def guardar_registro(self):
        try:
            # Convertir días a entero
            dias_str = self.entry_dias.get()
            if not dias_str:
                raise ValueError("Debe ingresar los días laborados")

            dias = int(dias_str)

            self.empleado = GestionEmpleados(
                identificacion=self.entry_id.get().strip(),
                nombre_completo=self.entry_nombre.get().strip(),
                genero=self.genero_var.get(),
                cargo=self.cargo_var.get(),
                dias_laborados=dias,
            )
            messagebox.showinfo(
                "Registro Exitoso",
                f"Los datos del empleado {self.empleado.nombre_completo} han sido guardados.",
            )
            # Limpiar los campos después de guardar
            self.limpiar_campos()
        except ValueError as e:
            messagebox.showerror("Error de Validación", str(e))
        except Exception as e:
            messagebox.showerror("Error Inesperado", f"Ocurrió un error: {str(e)}")

    # ================================================
    # METODO PARA MOSTRAR EL REPORTE
    # ================================================
    def mostrar_reporte(self):
        if self.empleado is None:
            messagebox.showwarning(
                "Faltan Datos",
                "Primero debe completar y guardar el registro del empleado.",
            )
            return

        ReporteApp(self.empleado, parent=self.ventana)

    # ================================================
    # METODO PARA SALIR
    # ================================================
    def salir(self):
        if messagebox.askyesno(
            "Confirmar Salida",
            "¿Está seguro que desea cerrar la Fase 2 y volver al menú principal?",
        ):
            self.ventana.destroy()

    # ================================================
    # METODO PARA LIMPIAR LOS CAMPOS
    # ================================================
    def limpiar_campos(self):
        self.entry_id.delete(0, tk.END)
        self.entry_nombre.delete(0, tk.END)
        self.genero_var.set("Masculino")
        self.combo_cargo.set("")
        self.entry_dias.delete(0, tk.END)
        self.entry_valor_dia.config(state="normal")
        self.entry_valor_dia.delete(0, tk.END)
        self.entry_valor_dia.config(state="disabled")
