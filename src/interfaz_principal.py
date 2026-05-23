import tkinter as tk
from tkinter import messagebox

# * IMPORTACIÓN MÓDULOS FASES
# * Interfaces disponibles dentro del sistema.
from fases.fase_2.interfaz_registro import RegistroApp as RegistroAppFase2
from fases.fase_3.interfaz_registro import RegistroApp as RegistroAppFase3
from fases.fase_4.interfaz_principal import Ventana

# * IMPORTACIÓN CONFIGURACIÓN GLOBAL
# * Colores, textos y datos compartidos.
from config.fase_5.constantes_globales import (
    TEXTO_FOOTER,
    TITULO_APP,
    NOMBRE_ESTUDIANTE,
    COLOR_FONDO,
    COLOR_PRIMARIO,
    COLOR_BLANCO,
    COLOR_ERROR,
    COLOR_BORDE,
    COLOR_TEXTO_SECUNDARIO,
)

# * IMPORTACIÓN CONFIGURACIÓN MENÚ
# * Dimensiones, fuentes y textos del menú principal.
from config.fase_5.constantes_menu import (
    ANCHO_VENTANA_MENU,
    ALTO_VENTANA_MENU,
    ANCHO_FRAME_MENU,
    ALTO_FRAME_MENU,
    FUENTE_TITULO_MENU,
    FUENTE_SUBTITULO_MENU,
    FUENTE_BOTON_MENU,
    FUENTE_FOOTER_MENU,
    TEXTO_TITULO_MENU,
    TEXTO_SUBTITULO_MENU,
    TEXTO_FASE2,
    TEXTO_FASE3,
    TEXTO_FASE4,
    TEXTO_SALIR,
)


# * CLASE MENÚ INTEGRADOR
# * Permite navegar entre las diferentes fases.
class AppIntegracion:

    def __init__(self, root):

        # * CREACIÓN VENTANA SECUNDARIA
        self.ventana = tk.Toplevel(root)

        # * CONFIGURACIÓN PRINCIPAL
        self.ventana.title(TITULO_APP)

        self.ventana.geometry(f"{ANCHO_VENTANA_MENU}x{ALTO_VENTANA_MENU}")

        self.ventana.resizable(False, False)

        self.ventana.configure(bg=COLOR_FONDO)

        # ! Captura cierre manual desde la X
        self.ventana.protocol("WM_DELETE_WINDOW", self.salir)

        # * CONSTRUCCIÓN INICIAL
        self.crear_interfaz()

        self.centrar()

    # ==================================================
    # * CENTRAR VENTANA
    # ==================================================

    def centrar(self):

        self.ventana.update_idletasks()

        # ? Calcular posición central pantalla
        x = (self.ventana.winfo_screenwidth() // 2) - (ANCHO_VENTANA_MENU // 2)

        y = (self.ventana.winfo_screenheight() // 2) - (ALTO_VENTANA_MENU // 2)

        self.ventana.geometry(f"{ANCHO_VENTANA_MENU}x" f"{ALTO_VENTANA_MENU}+{x}+{y}")

    # ==================================================
    # * CREACIÓN INTERFAZ
    # ==================================================

    def crear_interfaz(self):

        # * CONTENEDOR PRINCIPAL
        frame = tk.Frame(
            self.ventana,
            bg=COLOR_BLANCO,
            highlightbackground=COLOR_BORDE,
            highlightthickness=1,
            padx=10,
            pady=10,
        )

        frame.place(
            relx=0.5,
            rely=0.5,
            anchor="center",
            width=ANCHO_FRAME_MENU,
            height=ALTO_FRAME_MENU,
        )

        # ==================================================
        # * ENCABEZADO
        # ==================================================

        tk.Label(
            frame,
            text=TEXTO_TITULO_MENU,
            font=FUENTE_TITULO_MENU,
            bg=COLOR_BLANCO,
            fg=COLOR_PRIMARIO,
        ).pack(
            padx=10,
            pady=10,
        )

        tk.Label(
            frame,
            text=NOMBRE_ESTUDIANTE,
            font=FUENTE_SUBTITULO_MENU,
            bg=COLOR_BLANCO,
            fg=COLOR_TEXTO_SECUNDARIO,
        ).pack(
            padx=10,
            pady=5,
        )

        tk.Label(
            frame,
            text=TEXTO_SUBTITULO_MENU,
            font=FUENTE_SUBTITULO_MENU,
            bg=COLOR_BLANCO,
            fg=COLOR_TEXTO_SECUNDARIO,
        ).pack(
            padx=10,
            pady=(0, 20),
        )

        # ==================================================
        # * BOTONES MENÚ
        # ==================================================

        self.crear_boton(
            frame,
            TEXTO_FASE2,
            self.abrir_fase2,
            COLOR_PRIMARIO,
        )

        self.crear_boton(
            frame,
            TEXTO_FASE3,
            self.abrir_fase3,
            COLOR_PRIMARIO,
        )

        self.crear_boton(
            frame,
            TEXTO_FASE4,
            self.abrir_fase4,
            COLOR_PRIMARIO,
        )

        self.crear_boton(
            frame,
            TEXTO_SALIR,
            self.salir,
            COLOR_ERROR,
        )

        # ==================================================
        # * PIE DE PÁGINA
        # ==================================================

        tk.Label(
            self.ventana,
            text=TEXTO_FOOTER,
            bg=COLOR_FONDO,
            fg=COLOR_TEXTO_SECUNDARIO,
            font=FUENTE_FOOTER_MENU,
        ).pack(
            side="bottom",
            pady=10,
        )

    # ==================================================
    # * BOTÓN ESTÁNDAR
    # ==================================================

    def crear_boton(
        self,
        parent,
        texto,
        comando,
        color,
    ):

        # ? Método reutilizable para evitar repetir código
        tk.Button(
            parent,
            text=texto,
            command=comando,
            bg=color,
            fg="white",
            font=FUENTE_BOTON_MENU,
            bd=0,
            width=25,
            height=2,
            cursor="hand2",
        ).pack(
            padx=10,
            pady=8,
        )

    # ==================================================
    # * EVENTOS MENÚ
    # ==================================================

    def abrir_fase2(self):

        try:

            RegistroAppFase2(self.ventana)

        # ! Captura errores apertura Fase 2
        except Exception as e:

            messagebox.showerror(
                "Error Fase 2",
                str(e),
            )

    def abrir_fase3(self):

        try:

            RegistroAppFase3()

        # ! Captura errores apertura Fase 3
        except Exception as e:

            messagebox.showerror(
                "Error Fase 3",
                str(e),
            )

    def abrir_fase4(self):

        try:

            Ventana(self.ventana)

        # ! Captura errores apertura Fase 4
        except Exception as e:

            messagebox.showerror(
                "Error Fase 4",
                str(e),
            )

    # ==================================================
    # * CERRAR SISTEMA
    # ==================================================

    def salir(self):

        # ! Finaliza completamente la aplicación
        self.ventana.master.destroy()
