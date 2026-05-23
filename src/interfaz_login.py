import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# * IMPORTACIÓN DE CONSTANTES GLOBALES
# * Variables compartidas de apariencia y configuración.
from config.fase_5.constantes_globales import (
    CLAVE_ACCESO,
    COLOR_BLANCO,
    COLOR_BORDE,
    COLOR_ERROR,
    COLOR_FONDO,
    COLOR_PRIMARIO,
    COLOR_TEXTO_SECUNDARIO,
    NOMBRE_ESTUDIANTE,
    TEXTO_FOOTER,
    TITULO_APP,
)

# * IMPORTACIÓN DE CONSTANTES LOGIN
# * Configuración específica del formulario de acceso.
from config.fase_5.constantes_login import (
    ALTO_FRAME,
    ALTO_VENTANA,
    ANCHO_FRAME,
    ANCHO_VENTANA,
    FUENTE_BOTON,
    FUENTE_FOOTER,
    FUENTE_NORMAL,
    FUENTE_TITULO,
    MENSAJE_ACCESO_OK,
    MENSAJE_ERROR_CLAVE,
    MENSAJE_ERROR_VACIO,
    TEXTO_BOTON_LOGIN,
    TEXTO_BOTON_SALIR,
    TEXTO_CREDENCIAL,
)


# * CLASE PRINCIPAL LOGIN
# * Gestiona la interfaz y validación de acceso.
class LoginApp:

    def __init__(self):

        # * CREACIÓN DE VENTANA PRINCIPAL
        self.ventana = tk.Tk()

        # * CONFIGURACIÓN VISUAL
        self.ventana.title(f"Acceso - {TITULO_APP}")
        self.ventana.geometry(f"{ANCHO_VENTANA}x{ALTO_VENTANA}")
        self.ventana.resizable(False, False)
        self.ventana.configure(bg=COLOR_FONDO)

        # * CONSTRUCCIÓN INICIAL
        self.crear_interfaz()
        self.centrar()

    # ==================================================
    # * CENTRAR VENTANA
    # ==================================================

    def centrar(self):

        # ? Calcula posición central usando resolución pantalla
        self.ventana.update_idletasks()

        x = (self.ventana.winfo_screenwidth() // 2) - (ANCHO_VENTANA // 2)

        y = (self.ventana.winfo_screenheight() // 2) - (ALTO_VENTANA // 2)

        self.ventana.geometry(f"{ANCHO_VENTANA}x{ALTO_VENTANA}+{x}+{y}")

    # ==================================================
    # * CONSTRUCCIÓN INTERFAZ
    # ==================================================

    def crear_interfaz(self):

        # * CONTENEDOR PRINCIPAL
        frame = tk.Frame(
            self.ventana,
            bg=COLOR_BLANCO,
            highlightthickness=1,
            highlightbackground=COLOR_BORDE,
        )

        frame.place(
            relx=0.5,
            rely=0.5,
            anchor="center",
            width=ANCHO_FRAME,
            height=ALTO_FRAME,
        )

        # ==================================================
        # * TÍTULO SISTEMA
        # ==================================================

        tk.Label(
            frame,
            text=TITULO_APP,
            font=FUENTE_TITULO,
            bg=COLOR_BLANCO,
            fg=COLOR_PRIMARIO,
        ).pack(pady=10)

        # ==================================================
        # * DATOS INFORMATIVOS
        # ==================================================

        tk.Label(
            frame,
            text=f"Estudiante: {NOMBRE_ESTUDIANTE}",
            font=FUENTE_NORMAL,
            bg=COLOR_BLANCO,
            fg=COLOR_TEXTO_SECUNDARIO,
        ).pack()

        tk.Label(
            frame,
            text=f"Fecha: {datetime.now().strftime('%d/%m/%Y')}",
            font=FUENTE_NORMAL,
            bg=COLOR_BLANCO,
            fg=COLOR_TEXTO_SECUNDARIO,
        ).pack()

        # ==================================================
        # * INGRESO DE CREDENCIAL
        # ==================================================

        tk.Label(
            frame,
            text=TEXTO_CREDENCIAL,
            font=FUENTE_NORMAL,
            bg=COLOR_BLANCO,
        ).pack(pady=(10, 0))

        self.entry = tk.Entry(
            frame,
            show="*",
            font=FUENTE_NORMAL,
            justify="center",
        )

        self.entry.pack(pady=5)

        # ? Posiciona cursor automáticamente
        self.entry.focus()

        # ? Permite validar con ENTER
        self.entry.bind("<Return>", lambda event: self.validar())

        # ==================================================
        # * BOTONES ACCIÓN
        # ==================================================

        btn_frame = tk.Frame(frame, bg=COLOR_BLANCO)

        btn_frame.pack(
            pady=15,
            fill="x",
            padx=20,
        )

        tk.Button(
            btn_frame,
            text=TEXTO_BOTON_LOGIN,
            command=self.validar,
            bg=COLOR_PRIMARIO,
            fg="white",
            font=FUENTE_BOTON,
            bd=0,
            height=2,
        ).pack(
            side="left",
            expand=True,
            fill="x",
            padx=5,
        )

        tk.Button(
            btn_frame,
            text=TEXTO_BOTON_SALIR,
            command=self.ventana.destroy,
            bg=COLOR_ERROR,
            fg="white",
            font=FUENTE_BOTON,
            bd=0,
            height=2,
        ).pack(
            side="left",
            expand=True,
            fill="x",
            padx=5,
        )

        # ==================================================
        # * PIE DE PÁGINA
        # ==================================================

        tk.Label(
            self.ventana,
            text=TEXTO_FOOTER,
            bg=COLOR_FONDO,
            fg=COLOR_TEXTO_SECUNDARIO,
            font=FUENTE_FOOTER,
        ).pack(side="bottom", pady=10)

    # ==================================================
    # * VALIDACIÓN LOGIN
    # ==================================================

    def validar(self):

        # * Obtener valor ingresado
        clave = self.entry.get()

        # ! Validación campo vacío
        if clave.strip() == "":
            messagebox.showerror("Error", MENSAJE_ERROR_VACIO)
            return

        # ! Validación credencial incorrecta
        if clave != CLAVE_ACCESO:

            messagebox.showerror(
                "Acceso denegado",
                MENSAJE_ERROR_CLAVE,
            )

            self.entry.delete(0, tk.END)
            return

        # * Acceso exitoso
        messagebox.showinfo(
            "Acceso permitido",
            MENSAJE_ACCESO_OK,
        )

        self.ventana.withdraw()

        self.abrir_menu_principal()

    # ==================================================
    # * ABRIR MENÚ PRINCIPAL
    # ==================================================

    def abrir_menu_principal(self):

        from src.interfaz_principal import AppIntegracion

        AppIntegracion(self.ventana)

    # ==================================================
    # * EJECUCIÓN PRINCIPAL
    # ==================================================

    def ejecutar(self):

        # * Mantener interfaz en funcionamiento
        self.ventana.mainloop()
