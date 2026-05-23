# ============================
# * IMPORTACIONES
# ============================

# * Importa constantes globales utilizadas
# * para restricciones y mensajes del árbol.
from config.fase_4.constantes_arbol import (
    MAX_NIVELES,
    ERROR_MAX_NIVELES,
    ERROR_DUPLICADO,
)

# ============================
# * CLASE NODO
# ============================


# ? Representa cada elemento individual
# ? dentro del árbol binario.
class Nodo:

    # ! CONSTRUCTOR:
    # ? Inicializa valor y conexiones
    # ? izquierda / derecha.
    def __init__(self, valor):

        # * Dato almacenado en el nodo
        self.valor = valor

        # * Referencia al hijo izquierdo
        self.izquierda = None

        # * Referencia al hijo derecho
        self.derecha = None


# ============================
# * CLASE ÁRBOL BINARIO DE BÚSQUEDA
# ============================


# ? Implementa estructura ABB:
# ? izquierda < raíz < derecha
class ArbolBinarioBusqueda:

    # ! CONSTRUCTOR PRINCIPAL
    def __init__(self):

        # * Nodo principal del árbol
        self.raiz = None

    # ============================
    # * INSERTAR NODOS
    # ============================

    # ? Método público utilizado
    # ? para insertar nuevos valores.
    def insertar(self, valor):

        self.raiz = self._insertar(
            self.raiz,
            valor,
            1,
        )

    # ! MÉTODO RECURSIVO:
    # ? Inserta siguiendo reglas
    # ? del Árbol Binario de Búsqueda.
    def _insertar(
        self,
        nodo,
        valor,
        nivel,
    ):

        # ! VALIDACIÓN:
        # ? Evita superar profundidad máxima.
        if nivel > MAX_NIVELES:
            raise Exception(ERROR_MAX_NIVELES)

        # * Si posición vacía:
        # * crear nuevo nodo.
        if nodo is None:
            return Nodo(valor)

        # ! VALIDACIÓN:
        # ? No permitir valores duplicados.
        if valor == nodo.valor:
            raise Exception(ERROR_DUPLICADO)

        # ? Si es menor:
        # ? insertar lado izquierdo.
        if valor < nodo.valor:

            nodo.izquierda = self._insertar(
                nodo.izquierda,
                valor,
                nivel + 1,
            )

        # ? Si es mayor:
        # ? insertar lado derecho.
        else:

            nodo.derecha = self._insertar(
                nodo.derecha,
                valor,
                nivel + 1,
            )

        # * Retornar nodo actualizado
        return nodo

    # ============================
    # * BÚSQUEDA DE DATOS
    # ============================

    # ? Método público encargado
    # ? de iniciar la búsqueda.
    def buscar(self, valor):

        return self._buscar(
            self.raiz,
            valor,
        )

    # ! MÉTODO RECURSIVO:
    # ? Busca valor recorriendo
    # ? izquierda o derecha.
    def _buscar(
        self,
        nodo,
        valor,
    ):

        # * Nodo inexistente
        if nodo is None:
            return False

        # * Valor encontrado
        if nodo.valor == valor:
            return True

        # ? Buscar izquierda
        if valor < nodo.valor:

            return self._buscar(
                nodo.izquierda,
                valor,
            )

        # ? Buscar derecha
        return self._buscar(
            nodo.derecha,
            valor,
        )

    # ============================
    # * RECORRIDO PREORDEN
    # ============================

    # ? Orden:
    # ? Raíz → Izquierda → Derecha
    def preorden(self):

        res = []

        self._pre(
            self.raiz,
            res,
        )

        return res

    # ! MÉTODO RECURSIVO
    def _pre(
        self,
        nodo,
        res,
    ):

        if nodo:

            # * Procesar raíz
            res.append(nodo.valor)

            # * Recorrer izquierda
            self._pre(
                nodo.izquierda,
                res,
            )

            # * Recorrer derecha
            self._pre(
                nodo.derecha,
                res,
            )

    # ============================
    # * RECORRIDO INORDEN
    # ============================

    # ? Orden:
    # ? Izquierda → Raíz → Derecha
    # ? Produce datos ordenados.
    def inorden(self):

        res = []

        self._ino(
            self.raiz,
            res,
        )

        return res

    def _ino(
        self,
        nodo,
        res,
    ):

        if nodo:

            self._ino(
                nodo.izquierda,
                res,
            )

            res.append(nodo.valor)

            self._ino(
                nodo.derecha,
                res,
            )

    # ============================
    # * RECORRIDO POSORDEN
    # ============================

    # ? Orden:
    # ? Izquierda → Derecha → Raíz
    def posorden(self):

        res = []

        self._pos(
            self.raiz,
            res,
        )

        return res

    def _pos(
        self,
        nodo,
        res,
    ):

        if nodo:

            self._pos(
                nodo.izquierda,
                res,
            )

            self._pos(
                nodo.derecha,
                res,
            )

            res.append(nodo.valor)

    # ============================
    # * LIMPIAR ÁRBOL
    # ============================

    # ? Elimina toda la estructura
    # ? dejando raíz vacía.
    def limpiar(self):

        self.raiz = None
