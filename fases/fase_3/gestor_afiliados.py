# ============================
# GESTOR DE AFILIADOS
# ============================


class GestionAfiliados:
    """
    Clase encargada de gestionar las estructuras de datos:
    Pila, Cola y Lista para el sistema de afiliados.
    """

    def __init__(self):
        """
        Inicializa las estructuras de datos en memoria:
        - Pila (LIFO)
        - Cola (FIFO)
        - Lista (colección general)
        """
        self.pila = []
        self.cola = []
        self.lista = []

    # ============================
    # PILA (LIFO)
    # ============================

    def apilar(self, afiliado):
        """
        Inserta un afiliado en la estructura tipo Pila (LIFO).

        Parámetros:
            afiliado (EstructuraDatosAfiliado): objeto afiliado a registrar.
        """
        self.pila.append(afiliado)

    def desapilar(self):
        """
        Elimina y retorna el último afiliado agregado en la Pila.

        Retorna:
            afiliado (EstructuraDatosAfiliado | None)
        """
        if len(self.pila) > 0:
            return self.pila.pop()
        return None

    # ============================
    # COLA (FIFO)
    # ============================

    def encolar(self, afiliado):
        """
        Inserta un afiliado en la estructura tipo Cola (FIFO).

        Parámetros:
            afiliado (EstructuraDatosAfiliado): objeto afiliado a registrar.
        """
        self.cola.append(afiliado)

    def desencolar(self):
        """
        Elimina y retorna el primer afiliado de la Cola (FIFO).

        Retorna:
            afiliado (EstructuraDatosAfiliado | None)
        """
        if len(self.cola) > 0:
            return self.cola.pop(0)
        return None

    # ============================
    # LISTA
    # ============================

    def agregar_lista(self, afiliado):
        """
        Agrega un afiliado al final de la lista.

        Parámetros:
            afiliado (EstructuraDatosAfiliado): objeto afiliado a registrar.
        """
        self.lista.append(afiliado)

    def eliminar_lista(self, numero_identificacion):
        """
        Elimina un afiliado de la lista buscando por número de identificación.

        Parámetros:
            numero_identificacion (int): ID del afiliado a eliminar.

        Retorna:
            afiliado eliminado o None si no se encuentra.
        """
        for i, afiliado in enumerate(self.lista):
            if afiliado.numero_identificacion == numero_identificacion:
                return self.lista.pop(i)
        return None

    # ============================
    # REPORTES
    # ============================

    def reporte_pila(self):
        """
        Calcula la suma total de tarifas de los afiliados en la pila.

        Retorna:
            float: suma de tarifas.
        """
        return sum(a.tarifa_afiliacion for a in self.pila)

    def reporte_cola(self):
        """
        Retorna la cantidad de afiliados en la cola.

        Retorna:
            int: número de registros.
        """
        return len(self.cola)

    def reporte_lista(self):
        """
        Calcula el promedio de ingresos de los afiliados en la lista.

        Retorna:
            float: promedio de ingresos o 0 si está vacía.
        """
        if len(self.lista) == 0:
            return 0
        return sum(a.ingresos for a in self.lista) / len(self.lista)
