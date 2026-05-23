# ============================
# IMPORTACIONES
# ============================

# Librería gráfica utilizada para dibujar el árbol en pantalla
import tkinter as tk

# Importación de colores y configuraciones visuales
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
# CLASE RENDERIZADOR DEL ÁRBOL
# ============================


class RenderizadorArbol:

    def __init__(self, canvas):

        # Canvas donde se dibujará el árbol
        self.canvas = canvas

        # Guarda el último nodo agregado
        # para resaltarlo visualmente
        self.ultimo_agregado = None

    # ============================
    # MÉTODO PRINCIPAL DE DIBUJO
    # ============================

    def dibujar(self, arbol, ultimo_agregado=None):

        # Guardar referencia del último nodo insertado
        self.ultimo_agregado = ultimo_agregado

        # Limpiar canvas antes de volver a dibujar
        self.canvas.delete("all")

        # Dibujar solamente si existe raíz
        if arbol.raiz:

            # Primero se dibujan líneas de conexión
            self._dibujar_conexiones(arbol.raiz, 0, 850, 35)

            # Luego se dibujan los nodos
            self._dibujar_nodos(arbol.raiz, 0, 850, 35)

    # ============================
    # COLOR SEGÚN NIVEL
    # ============================

    def _color_nivel(self, nivel):

        # Diccionario que asigna un color
        # dependiendo de la profundidad del nodo

        return {
            1: COLOR_NIVEL_1,
            2: COLOR_NIVEL_2,
            3: COLOR_NIVEL_3,
            4: COLOR_NIVEL_4,
        }.get(nivel, COLOR_NIVEL_DEFAULT)

    # ============================
    # DIBUJAR CONEXIONES
    # ============================

    def _dibujar_conexiones(self, nodo, izq, der, y, nivel=1):

        # Caso base recursivo
        if not nodo:
            return

        # Calcular posición horizontal nodo actual
        x = (izq + der) // 2

        # Distancia vertical hacia hijos
        y_next = y + 75

        # ------------------------
        # HIJO IZQUIERDO
        # ------------------------

        if nodo.izquierda:

            # Posición horizontal hijo izquierdo
            x_hijo = (izq + x) // 2

            # Dibujar línea padre → hijo
            self.canvas.create_line(x, y, x_hijo, y_next, fill=COLOR_LINEA)

            # Recursividad izquierda
            self._dibujar_conexiones(nodo.izquierda, izq, x, y_next, nivel + 1)

        # ------------------------
        # HIJO DERECHO
        # ------------------------

        if nodo.derecha:

            # Posición horizontal hijo derecho
            x_hijo = (x + der) // 2

            # Dibujar línea padre → hijo
            self.canvas.create_line(x, y, x_hijo, y_next, fill=COLOR_LINEA)

            # Recursividad derecha
            self._dibujar_conexiones(nodo.derecha, x, der, y_next, nivel + 1)

    # ============================
    # DIBUJAR NODOS
    # ============================

    def _dibujar_nodos(self, nodo, izq, der, y, nivel=1):

        # Caso base recursivo
        if not nodo:
            return

        # Calcular posición horizontal
        x = (izq + der) // 2

        # Radio nodo
        r = 24

        # Obtener color según profundidad
        color = self._color_nivel(nivel)

        # Verificar si es el nodo recién agregado
        es_nuevo = self.ultimo_agregado == nodo.valor

        # ------------------------
        # ANIMACIÓN NUEVO NODO
        # ------------------------

        if es_nuevo:

            self._animar_crecimiento(x, y, color, str(nodo.valor), nivel, 2)

        # ------------------------
        # NODO NORMAL
        # ------------------------

        else:

            # Dibujar círculo nodo
            self.canvas.create_oval(
                x - r, y - r, x + r, y + r, fill=color, outline=color
            )

            # Dibujar texto interno
            self.canvas.create_text(
                x,
                y,
                text=f"{nodo.valor}\n(N{nivel})",
                fill="white",
                font=("Segoe UI", 8, "bold"),
                justify="center",
            )

        # Recursividad izquierda
        self._dibujar_nodos(nodo.izquierda, izq, x, y + 75, nivel + 1)

        # Recursividad derecha
        self._dibujar_nodos(nodo.derecha, x, der, y + 75, nivel + 1)

    # ============================
    # ANIMACIÓN CRECIMIENTO NODO
    # ============================

    def _animar_crecimiento(self, x, y, color, valor_texto, nivel, r_actual):

        # Etiqueta única nodo
        tag = f"nodo_{valor_texto}"

        # Eliminar dibujo anterior animación
        self.canvas.delete(tag)

        # Mientras radio sea pequeño
        if r_actual <= 24:

            # Dibujar círculo creciendo
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

            # Ejecutar nuevamente animación
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

        else:

            # Dibujo final nodo completo
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

            # Mostrar valor y nivel
            self.canvas.create_text(
                x,
                y,
                text=f"{valor_texto}\n(N{nivel})",
                fill="white",
                font=("Segoe UI", 8, "bold"),
                justify="center",
                tags=tag,
            )
