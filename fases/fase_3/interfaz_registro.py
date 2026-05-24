# ============================
# IMPORTACIONES
# ============================
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from tkcalendar import DateEntry

# ? Estructura de datos del afiliado (modelo principal)
from fases.fase_3.estructura_datos_afiliado import EstructuraDatosAfiliado


# ============================
# CLASE PRINCIPAL: REGISTRO DE AFILIADOS
# ============================
class RegistroApp:

    # ? Colores del tema de la interfaz
    COLOR_FONDO = "#f8f9fa"
    COLOR_PRIMARIO = "#1a73e8"
    COLOR_EXITO = "#34a853"
    COLOR_PELIGRO = "#ea4335"
    COLOR_BLANCO = "#ffffff"

    # ============================
    # INICIALIZACIÓN DE LA VENTANA
    # ============================
    def __init__(self):

        # * Crear ventana secundaria
        self.ventana = tk.Toplevel()
        self.ventana.title("Caja Compensándote - Afiliados")

        # * Intento de maximizar ventana (Windows) o tamaño fijo alternativo
        try:
            self.ventana.state("zoomed")
        except:
            self.ventana.geometry("1100x800")

        self.ventana.configure(bg=self.COLOR_FONDO)

        # ============================
        # ESTRUCTURAS DE DATOS (FASE 3)
        # ============================
        self.pila = []
        self.cola = []
        self.lista = []

        # * Construcción de interfaz
        self.centrar_ventana()
        self.crear_widgets()

    # ============================
    # CENTRAR VENTANA
    # ============================
    def centrar_ventana(self):

        # * Centra la ventana en pantalla
        self.ventana.update_idletasks()

        w = self.ventana.winfo_width()
        h = self.ventana.winfo_height()

        x = (self.ventana.winfo_screenwidth() // 2) - (w // 2)
        y = (self.ventana.winfo_screenheight() // 2) - (h // 2)

        self.ventana.geometry(f"{w}x{h}+{x}+{y}")

    # ============================
    # INTERFAZ PRINCIPAL
    # ============================
    def crear_widgets(self):

        # ============================
        # HEADER
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
        # FORMULARIO PRINCIPAL
        # ============================
        form = tk.LabelFrame(
            self.ventana,
            text="Formulario de Registro",
            bg=self.COLOR_BLANCO,
        )
        form.pack(fill="x", padx=20, pady=15)

        form.columnconfigure((1, 3), weight=1)

        # ============================
        # FILA 1: IDENTIFICACIÓN
        # ============================
        tk.Label(form, text="Tipo de Identificación", bg=self.COLOR_BLANCO).grid(
            row=0, column=0, sticky="w", padx=10, pady=5
        )

        self.tipo_id = ttk.Combobox(form, values=["CC", "CE", "TI", "PAS"])
        self.tipo_id.grid(row=0, column=1, sticky="ew", padx=10)

        tk.Label(form, text="Nro. de Identificación", bg=self.COLOR_BLANCO).grid(
            row=0, column=2, sticky="w", padx=10
        )

        self.num_id = tk.Entry(form)
        self.num_id.grid(row=0, column=3, sticky="ew", padx=10)

        # ============================
        # FILA 2: DATOS PERSONALES
        # ============================
        tk.Label(form, text="Nombre Completo", bg=self.COLOR_BLANCO).grid(
            row=1, column=0, sticky="w", padx=10, pady=5
        )

        self.nombre = tk.Entry(form)
        self.nombre.grid(row=1, column=1, sticky="ew", padx=10)

        tk.Label(form, text="Ingresos Actuales", bg=self.COLOR_BLANCO).grid(
            row=1, column=2, sticky="w", padx=10
        )

        self.ingresos_var = tk.StringVar()
        self.ingresos = tk.Entry(form, textvariable=self.ingresos_var)
        self.ingresos.grid(row=1, column=3, sticky="ew", padx=10)

        # * Actualiza tarifa automáticamente al cambiar ingresos
        self.ingresos_var.trace_add("write", self.actualizar_tarifa)

        # ============================
        # FILA 3: SERVICIOS Y MODALIDAD
        # ============================
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

        # * Recalcula tarifa al seleccionar servicio
        self.servicio.bind("<<ComboboxSelected>>", self.actualizar_tarifa)

        tk.Label(form, text="Modalidad de Empleo", bg=self.COLOR_BLANCO).grid(
            row=2, column=2, sticky="w", padx=10
        )

        mode_frame = tk.Frame(form, bg=self.COLOR_BLANCO)
        mode_frame.grid(row=2, column=3, sticky="w")

        # * Variable para modalidad laboral
        self.modalidad = tk.StringVar(value="None")

        # * Radio: Empleado
        tk.Radiobutton(
            mode_frame,
            text="Empleado",
            variable=self.modalidad,
            value="Empleado",
            bg=self.COLOR_BLANCO,
            command=self.actualizar_tarifa,
        ).pack(side="left")

        # * Radio: Independiente
        tk.Radiobutton(
            mode_frame,
            text="Independiente",
            variable=self.modalidad,
            value="Independiente",
            bg=self.COLOR_BLANCO,
            command=self.actualizar_tarifa,
        ).pack(side="left")

        # ============================
        # FILA 4: ESTRUCTURA Y FECHA
        # ============================
        tk.Label(form, text="Estructura de Datos", bg=self.COLOR_BLANCO).grid(
            row=3, column=0, sticky="w", padx=10, pady=5
        )

        self.estructura = ttk.Combobox(form, values=["Pila", "Cola", "Lista"])
        self.estructura.grid(row=3, column=1, sticky="ew", padx=10)

        tk.Label(form, text="Fecha de Afiliación", bg=self.COLOR_BLANCO).grid(
            row=3, column=2, sticky="w", padx=10
        )

        # * Selector de fecha con calendario
        self.fecha = DateEntry(
            form,
            width=12,
            background="darkblue",
            foreground="white",
            borderwidth=2,
            date_pattern="yyyy-mm-dd",
        )
        self.fecha.grid(row=3, column=3, sticky="w", padx=10)

        # ============================
        # FILA 5: TARIFA AUTOMÁTICA
        # ============================
        tk.Label(
            form,
            text="Tarifa de Afiliación $",
            font=("Segoe UI", 10, "bold"),
            fg=self.COLOR_PRIMARIO,
            bg=self.COLOR_BLANCO,
        ).grid(row=4, column=0, sticky="w", padx=10, pady=10)

        # * Variable que muestra la tarifa calculada
        self.tarifa_calc = tk.StringVar(value="0")

        self.entry_tarifa = tk.Entry(
            form,
            textvariable=self.tarifa_calc,
            state="readonly",
            font=("Segoe UI", 10, "bold"),
        )
        self.entry_tarifa.grid(row=4, column=1, sticky="ew", padx=10)

        # ============================
        # FILA 5: REPORTE
        # ============================
        tk.Label(form, text="Resultado Reporte:", bg=self.COLOR_BLANCO).grid(
            row=4, column=2, sticky="w", padx=10
        )

        self.reporte_var = tk.StringVar(value="")
        self.entry_reporte = tk.Entry(
            form,
            textvariable=self.reporte_var,
            state="readonly",
            width=30,
        )
        self.entry_reporte.grid(row=4, column=3, sticky="ew", padx=10)

        # * Fondo blanco para campo de solo lectura
        self.entry_reporte.config(readonlybackground="white")

        # ============================
        # BOTONES DE ACCIÓN
        # ============================
        btns = tk.Frame(self.ventana, bg=self.COLOR_FONDO)
        btns.pack(fill="x", pady=10)

        # * Botón: Registrar afiliado
        tk.Button(
            btns,
            text="Registrar",
            bg=self.COLOR_PRIMARIO,
            fg="white",
            command=self.registrar,
        ).pack(side="left", expand=True, fill="x", padx=5)

        # * Botón: Limpiar campos del formulario
        tk.Button(
            btns,
            text="Limpiar",
            bg="#f0ad4e",
            fg="white",
            command=self.limpiar_campos,
        ).pack(side="left", expand=True, fill="x", padx=5)

        # * Botón: Eliminar registro seleccionado
        tk.Button(
            btns,
            text="Eliminar",
            bg=self.COLOR_PELIGRO,
            fg="white",
            command=self.eliminar,
        ).pack(side="left", expand=True, fill="x", padx=5)

        # * Botón: Generar reporte
        tk.Button(
            btns,
            text="Reporte",
            bg=self.COLOR_EXITO,
            fg="white",
            command=self.reporte,
        ).pack(side="left", expand=True, fill="x", padx=5)

        # * Botón: Salir del sistema
        tk.Button(
            btns,
            text="Salir",
            bg=self.COLOR_PELIGRO,
            fg="white",
            command=self.salir,
        ).pack(side="left", expand=True, fill="x", padx=5)

        # ============================
        # TABLA PRINCIPAL (TREEVIEW)
        # ============================

        # * Columnas de la tabla
        cols = (
            "tipo_id",
            "numero_id",
            "nombre",
            "ingresos",
            "servicio",
            "modalidad",
            "tarifa",
            "estructura",
            "fecha",
        )

        # * Crear tabla de visualización
        self.tree = ttk.Treeview(self.ventana, columns=cols, show="headings")

        # * Encabezados visibles de la tabla
        headings = {
            "tipo_id": "Tipo de Identificación",
            "numero_id": "Nro. de Identificación",
            "nombre": "Nombre Completo",
            "ingresos": "Ingresos Actuales",
            "servicio": "Servicios Deseados",
            "modalidad": "Modalidad de Empleo",
            "estructura": "Estructura de Datos",
            "tarifa": "Tarifa de Afiliación",
            "fecha": "Fecha de Afiliación",
        }

        # * Configuración de columnas y títulos
        for c in cols:
            self.tree.heading(c, text=headings[c])
            self.tree.column(c, width=140)

        # * Mostrar tabla en pantalla
        self.tree.pack(fill="both", expand=True, padx=15, pady=10)

        # * Evento: cargar datos al seleccionar una fila
        self.tree.bind("<<TreeviewSelect>>", self.cargar_datos_seleccion)

    # ============================
    # VALIDACIÓN - método de clase
    # ============================
    def validar(self):

        # * Validar que el ID sea numérico
        if not self.num_id.get().isdigit():
            messagebox.showerror("Error", "ID inválido")
            return False

        # * Validar nombre obligatorio
        if not self.nombre.get():
            messagebox.showerror("Error", "Nombre obligatorio")
            return False

        # * Validar ingresos numéricos (permite decimales)
        if not self.ingresos.get().replace(".", "").isdigit():
            messagebox.showerror("Error", "Ingresos inválidos")
            return False

        # * Validar selección de modalidad
        if not self.modalidad.get():
            messagebox.showerror("Error", "Seleccione modalidad")
            return False

        return True

    # ============================
    # REGISTRAR AFILIADO (CÁLCULO AUTOMÁTICO)
    # ============================
    def registrar(self):

        # * Validar formulario antes de registrar
        if not self.validar():
            return

        # * Crear objeto afiliado con los datos del formulario
        obj = EstructuraDatosAfiliado(
            self.tipo_id.get(),
            int(self.num_id.get()),
            self.nombre.get(),
            float(self.ingresos.get()),
            self.servicio.get(),
            self.modalidad.get(),
            self.estructura.get(),
        )

        # * Calcular tarifa automáticamente según reglas del sistema
        obj.calcular_tarifa_afiliacion()

        # * Asignar fecha seleccionada en el calendario
        obj.fecha_afiliacion = self.fecha.get()

        # ============================
        # INSERTAR EN ESTRUCTURA ELEGIDA
        # ============================

        if self.estructura.get() == "Pila":
            self.pila.append(obj)

        elif self.estructura.get() == "Cola":
            self.cola.append(obj)

        else:
            self.lista.append(obj)

        # ============================
        # INSERTAR EN TABLA (TREEVIEW)
        # ============================
        self.tree.insert(
            "",
            "end",
            values=(
                obj.tipo_identificacion,
                obj.numero_identificacion,
                obj.nombre_completo,
                f"${obj.ingresos:,.0f}",
                obj.servicio,
                obj.modalidad,
                f"${obj.tarifa_afiliacion:,.0f}",
                obj.estructura,
                self.fecha.get(),
            ),
        )

        # * Limpiar formulario después del registro
        self.limpiar_campos()

        # * Confirmación de éxito
        messagebox.showinfo("Éxito", "Afiliado registrado correctamente")

    # ============================
    # ELIMINAR AFILIADO (SEGÚN ESTRUCTURA)
    # ============================
    def eliminar(self):

        # * Obtener estructura seleccionada
        estr = self.estructura.get()

        # * Validar selección de estructura
        if not estr:
            messagebox.showwarning(
                "Atención", "Seleccione una estructura para eliminar"
            )
            return

        # * Confirmación del usuario
        if not messagebox.askyesno(
            "Confirmar", f"¿Está seguro de eliminar de la {estr}?"
        ):
            return

        id_a_borrar = None

        # ============================
        # CASO PILA (LIFO)
        # ============================
        if estr == "Pila":

            if not self.pila:
                messagebox.showinfo("Vacía", "La pila está vacía")
                return

            obj_borrado = self.pila.pop()
            id_a_borrar = obj_borrado.numero_identificacion

        # ============================
        # CASO COLA (FIFO)
        # ============================
        elif estr == "Cola":

            if not self.cola:
                messagebox.showinfo("Vacía", "La cola está vacía")
                return

            obj_borrado = self.cola.pop(0)
            id_a_borrar = obj_borrado.numero_identificacion

        # ============================
        # CASO LISTA (ELIMINACIÓN POR ID)
        # ============================
        else:

            id_buscado = self.num_id.get()

            if not id_buscado:
                messagebox.showerror(
                    "Error",
                    "Ingrese ID en el formulario para eliminar de la lista",
                )
                return

            # * Filtrar lista eliminando el elemento
            original_len = len(self.lista)
            self.lista = [
                x for x in self.lista if str(x.numero_identificacion) != id_buscado
            ]

            if len(self.lista) == original_len:
                messagebox.showinfo(
                    "No encontrado",
                    f"No se encontró ID {id_buscado} en la lista",
                )
                return

            id_a_borrar = int(id_buscado)

        # ============================
        # ELIMINAR DE LA TABLA (TREEVIEW)
        # ============================

        for item in self.tree.get_children():

            # * La columna 1 contiene el ID del afiliado
            if self.tree.item(item)["values"][1] == id_a_borrar:
                self.tree.delete(item)

                # * En pila y cola solo se elimina un elemento
                if estr in ["Pila", "Cola"]:
                    break

        # * Limpiar formulario
        self.limpiar_campos()

        # * Confirmación final
        messagebox.showinfo("Éxito", "Eliminación completada correctamente")

    # ============================
    # REPORTE DINÁMICO
    # ============================
    def reporte(self):

        # * Obtener estructura seleccionada
        estr = self.estructura.get()

        # * Validar selección
        if not estr:
            messagebox.showwarning(
                "Atención",
                "Seleccione una estructura para el reporte",
            )
            return

        resultado = ""

        # ============================
        # REPORTE PARA PILA
        # ============================
        if estr == "Pila":

            # * Suma total de tarifas en la pila
            total = sum(x.tarifa_afiliacion for x in self.pila)
            resultado = f"Tarifas: ${total:,.0f}"

        # ============================
        # REPORTE PARA COLA
        # ============================
        elif estr == "Cola":

            # * Cantidad de registros en cola
            resultado = f"Cantidad: {len(self.cola)} registros"

        # ============================
        # REPORTE PARA LISTA
        # ============================
        else:

            # * Promedio de ingresos si hay datos
            if self.lista:
                prom = sum(x.ingresos for x in self.lista) / len(self.lista)
                resultado = f"Promedio: ${prom:,.0f}"
            else:
                resultado = "Lista vacía"

        # * Mostrar resultado en campo de solo lectura
        self.reporte_var.set(resultado)

    # ============================
    # CÁLCULO DINÁMICO DE TARIFA
    # ============================
    def actualizar_tarifa(self, *args):

        try:
            # * Limpiar formato de ingreso (puntos y comas)
            ingresos_str = self.ingresos_var.get().replace(".", "").replace(",", "")

            # * Si no hay datos, resetear tarifa
            if not ingresos_str:
                self.tarifa_calc.set("$0")
                return

            modalidad = self.modalidad.get()

            # * Validar modalidad seleccionada
            if modalidad == "None":
                self.tarifa_calc.set("Esperando modalidad...")
                return

            # ============================
            # USO DE CLASE PRINCIPAL (POO)
            # ============================

            # * Crear objeto temporal para cálculo
            obj_temp = EstructuraDatosAfiliado(
                "CC",
                0,
                "TEMP",
                float(ingresos_str),
                self.servicio.get(),
                modalidad,
                "Lista",
            )

            # * Calcular tarifa usando lógica central
            tarifa = obj_temp.calcular_tarifa_afiliacion()

            # * Mostrar resultado formateado
            self.tarifa_calc.set(f"${tarifa:,.0f}")

        except ValueError:
            # * Error en conversión de ingresos
            self.tarifa_calc.set("Error en ingresos")

    # ============================
    # UTILIDADES
    # ============================
    def limpiar_campos(self):

        # * Resetear campos del formulario
        self.tipo_id.set("")
        self.num_id.delete(0, tk.END)
        self.nombre.delete(0, tk.END)
        self.ingresos_var.set("")
        self.servicio.set("")
        self.modalidad.set("None")
        self.tarifa_calc.set("0")
        self.reporte_var.set("")

    def cargar_datos_seleccion(self, event):

        # * Obtener selección de la tabla
        seleccion = self.tree.selection()
        if not seleccion:
            return

        item = self.tree.item(seleccion[0])
        v = item["values"]

        # ============================
        # RELLENAR CAMPOS DEL FORMULARIO
        # ============================

        self.tipo_id.set(v[0])

        self.num_id.delete(0, tk.END)
        self.num_id.insert(0, v[1])

        self.nombre.delete(0, tk.END)
        self.nombre.insert(0, v[2])

        # * Limpiar formato de moneda en ingresos
        ingresos_clean = str(v[3]).replace("$", "").replace(",", "")
        self.ingresos_var.set(ingresos_clean)

        self.servicio.set(v[4])
        self.modalidad.set(v[5])

        # * Limpiar formato de moneda en tarifa
        tarifa_clean = str(v[6]).replace("$", "").replace(",", "")
        self.tarifa_calc.set(tarifa_clean)

        self.estructura.set(v[7])

        # * Convertir fecha desde string
        try:
            self.fecha.set_date(datetime.strptime(str(v[8]), "%Y-%m-%d"))
        except:
            pass

    # ============================
    # SALIR DEL SISTEMA
    # ============================
    def salir(self):

        # * Confirmación antes de cerrar
        if messagebox.askyesno(
            "Confirmar Salida",
            "¿Está seguro que desea cerrar la Fase 3 y volver al menú principal?",
        ):
            self.ventana.destroy()
