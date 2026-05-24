from config.fase_4.constantes_arbol import (
    MAX_NIVELES,
    ERROR_MAX_NIVELES,
    ERROR_DUPLICADO,
)


# ============================
# NODO DEL ÁRBOL BINARIO
# ============================
class Nodo:
    """
    Representa un nodo del árbol binario de búsqueda.
    """

    def __init__(self, valor):

        # * Valor almacenado en el nodo
        self.valor = valor

        # * Referencia al hijo izquierdo
        self.izquierda = None

        # * Referencia al hijo derecho
        self.derecha = None


# ============================
# ÁRBOL BINARIO DE BÚSQUEDA (BST)
# ============================
class ArbolBinarioBusqueda:
    """
    Implementación de un Árbol Binario de Búsqueda (BST)
    con inserción, búsqueda, recorridos y limpieza.
    """

    def __init__(self):

        # * Nodo raíz del árbol
        self.raiz = None

    # ============================
    # INSERTAR
    # ============================
    def insertar(self, valor):
        """
        Inserta un valor en el árbol respetando las reglas del BST.
        """

        # * Inserción recursiva desde la raíz
        self.raiz = self._insertar(self.raiz, valor, 1)

    def _insertar(self, nodo, valor, nivel):
        """
        Lógica recursiva de inserción con control de niveles.
        """

        # * Validación de profundidad máxima
        if nivel > MAX_NIVELES:
            raise Exception(ERROR_MAX_NIVELES)

        # * Caso base: posición vacía
        if nodo is None:
            return Nodo(valor)

        # * Evitar duplicados en el árbol
        if valor == nodo.valor:
            raise Exception(ERROR_DUPLICADO)

        # * Insertar en subárbol izquierdo
        if valor < nodo.valor:
            nodo.izquierda = self._insertar(nodo.izquierda, valor, nivel + 1)

        # * Insertar en subárbol derecho
        else:
            nodo.derecha = self._insertar(nodo.derecha, valor, nivel + 1)

        return nodo

    # ============================
    # BUSCAR
    # ============================
    def buscar(self, valor):
        """
        Busca un valor en el árbol.
        Retorna True si existe, False si no.
        """

        # * Inicio de búsqueda desde la raíz
        return self._buscar(self.raiz, valor)

    def _buscar(self, nodo, valor):
        """
        Lógica recursiva de búsqueda.
        """

        # * Nodo vacío → no encontrado
        if nodo is None:
            return False

        # * Valor encontrado
        if nodo.valor == valor:
            return True

        # * Buscar en subárbol izquierdo
        if valor < nodo.valor:
            return self._buscar(nodo.izquierda, valor)

        # * Buscar en subárbol derecho
        return self._buscar(nodo.derecha, valor)

    # ============================
    # RECORRIDOS
    # ============================

    def preorden(self):
        """
        Recorrido Preorden: Raíz → Izquierda → Derecha
        """
        res = []
        self._pre(self.raiz, res)
        return res

    def _pre(self, nodo, res):
        """Recursión preorden"""
        if nodo:
            res.append(nodo.valor)
            self._pre(nodo.izquierda, res)
            self._pre(nodo.derecha, res)

    def inorden(self):
        """
        Recorrido Inorden: Izquierda → Raíz → Derecha
        """
        res = []
        self._ino(self.raiz, res)
        return res

    def _ino(self, nodo, res):
        """Recursión inorden"""
        if nodo:
            self._ino(nodo.izquierda, res)
            res.append(nodo.valor)
            self._ino(nodo.derecha, res)

    def posorden(self):
        """
        Recorrido Postorden: Izquierda → Derecha → Raíz
        """
        res = []
        self._pos(self.raiz, res)
        return res

    def _pos(self, nodo, res):
        """Recursión postorden"""
        if nodo:
            self._pos(nodo.izquierda, res)
            self._pos(nodo.derecha, res)
            res.append(nodo.valor)

    # ============================
    # LIMPIAR ÁRBOL
    # ============================
    def limpiar(self):
        """
        Elimina todos los nodos del árbol reiniciando la raíz.
        """

        # * Reinicio del árbol
        self.raiz = None
