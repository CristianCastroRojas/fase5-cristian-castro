# ============================
# IMPORTACIONES
# ============================
import tkinter as tk

from config.fase_4.constantes_interfaz import (
    COLOR_LINEA,
    COLOR_NIVEL_1,
    COLOR_NIVEL_2,
    COLOR_NIVEL_3,
    COLOR_NIVEL_4,
    COLOR_NIVEL_DEFAULT,
    COLOR_BORDE_NUEVO,
)


# ============================
# CLASE: RENDERIZADOR DEL ÁRBOL
# ============================
class RenderizadorArbol:

    # ============================
    # INICIALIZACIÓN
    # ============================
    def __init__(self, canvas):

        # * Canvas donde se dibuja el árbol
        self.canvas = canvas

        # * Último nodo agregado (para animación/resaltado)
        self.ultimo_agregado = None

    # ============================
    # FUNCIÓN PRINCIPAL DE DIBUJO
    # ============================
    def dibujar(self, arbol, ultimo_agregado=None):

        # * Guardar referencia del último nodo insertado
        self.ultimo_agregado = ultimo_agregado

        # * Limpiar canvas antes de redibujar
        self.canvas.delete("all")

        # * Si el árbol tiene raíz, iniciar render
        if arbol.raiz:
            self._dibujar_conexiones(arbol.raiz, 0, 850, 35)
            self._dibujar_nodos(arbol.raiz, 0, 850, 35)

    # ============================
    # COLOR SEGÚN NIVEL DEL ÁRBOL
    # ============================
    def _color_nivel(self, nivel):

        # * Mapeo de colores por profundidad
        return {
            1: COLOR_NIVEL_1,
            2: COLOR_NIVEL_2,
            3: COLOR_NIVEL_3,
            4: COLOR_NIVEL_4,
        }.get(nivel, COLOR_NIVEL_DEFAULT)

    # ============================
    # DIBUJAR CONEXIONES ENTRE NODOS
    # ============================
    def _dibujar_conexiones(self, nodo, izq, der, y, nivel=1):

        # * Caso base: nodo vacío
        if not nodo:
            return

        # * Coordenada central del nodo actual
        x = (izq + der) // 2
        y_next = y + 75

        # ============================
        # CONEXIÓN HACIA HIJO IZQUIERDO
        # ============================
        if nodo.izquierda:
            x_hijo = (izq + x) // 2
            self.canvas.create_line(x, y, x_hijo, y_next, fill=COLOR_LINEA)
            self._dibujar_conexiones(nodo.izquierda, izq, x, y_next, nivel + 1)

        # ============================
        # CONEXIÓN HACIA HIJO DERECHO
        # ============================
        if nodo.derecha:
            x_hijo = (x + der) // 2
            self.canvas.create_line(x, y, x_hijo, y_next, fill=COLOR_LINEA)
            self._dibujar_conexiones(nodo.derecha, x, der, y_next, nivel + 1)

    # ============================
    # DIBUJAR NODOS
    # ============================
    def _dibujar_nodos(self, nodo, izq, der, y, nivel=1):

        # * Caso base: nodo vacío
        if not nodo:
            return

        # * Coordenadas del nodo
        x = (izq + der) // 2
        r = 24

        # * Color según nivel
        color = self._color_nivel(nivel)

        # * Verificar si es el nodo recién agregado
        es_nuevo = self.ultimo_agregado == nodo.valor

        # ============================
        # NODO NUEVO (ANIMADO)
        # ============================
        if es_nuevo:
            self._animar_crecimiento(x, y, color, str(nodo.valor), nivel, 2)

        # ============================
        # NODO NORMAL
        # ============================
        else:
            self.canvas.create_oval(
                x - r, y - r, x + r, y + r, fill=color, outline=color
            )

            self.canvas.create_text(
                x,
                y,
                text=f"{nodo.valor}\n(N{nivel})",
                fill="white",
                font=("Segoe UI", 8, "bold"),
                justify="center",
            )

        # * Recursión izquierda
        self._dibujar_nodos(nodo.izquierda, izq, x, y + 75, nivel + 1)

        # * Recursión derecha
        self._dibujar_nodos(nodo.derecha, x, der, y + 75, nivel + 1)

    # ============================
    # ANIMACIÓN DE CRECIMIENTO
    # ============================
    def _animar_crecimiento(self, x, y, color, valor_texto, nivel, r_actual):

        # * Tag único para controlar el nodo en canvas
        tag = f"nodo_{valor_texto}"

        # * Limpiar frame anterior del nodo
        self.canvas.delete(tag)

        # ============================
        # ANIMACIÓN PROGRESIVA
        # ============================
        if r_actual <= 24:

            self.canvas.create_oval(
                x - r_actual,
                y - r_actual,
                x + r_actual,
                y + r_actual,
                fill=color,
                outline="white",
                width=2,
                tags=tag,
            )

            # * Repetición de animación
            self.canvas.after(
                15,
                self._animar_crecimiento,
                x,
                y,
                color,
                valor_texto,
                nivel,
                r_actual + 3,
            )

        # ============================
        # ESTADO FINAL DEL NODO
        # ============================
        else:

            self.canvas.create_oval(
                x - 24,
                y - 24,
                x + 24,
                y + 24,
                fill=color,
                outline=COLOR_BORDE_NUEVO,
                width=3,
                tags=tag,
            )

            self.canvas.create_text(
                x,
                y,
                text=f"{valor_texto}\n(N{nivel})",
                fill="white",
                font=("Segoe UI", 8, "bold"),
                justify="center",
                tags=tag,
            )
