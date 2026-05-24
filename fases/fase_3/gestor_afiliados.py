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

        # * Estructura tipo pila (último en entrar, primero en salir)
        self.pila = []

        # * Estructura tipo cola (primero en entrar, primero en salir)
        self.cola = []

        # * Lista general de afiliados
        self.lista = []

    # ============================
    # PILA (LIFO)
    # ============================

    def apilar(self, afiliado):
        """
        Inserta un afiliado en la estructura tipo Pila (LIFO).
        """

        # * Agrega al final de la pila
        self.pila.append(afiliado)

    def desapilar(self):
        """
        Elimina y retorna el último afiliado agregado en la Pila.
        """

        # * Verifica que la pila no esté vacía
        if len(self.pila) > 0:
            return self.pila.pop()
        return None

    # ============================
    # COLA (FIFO)
    # ============================

    def encolar(self, afiliado):
        """
        Inserta un afiliado en la estructura tipo Cola (FIFO).
        """

        # * Agrega al final de la cola
        self.cola.append(afiliado)

    def desencolar(self):
        """
        Elimina y retorna el primer afiliado de la Cola (FIFO).
        """

        # * Verifica que la cola no esté vacía
        if len(self.cola) > 0:
            return self.cola.pop(0)
        return None

    # ============================
    # LISTA
    # ============================

    def agregar_lista(self, afiliado):
        """
        Agrega un afiliado al final de la lista.
        """

        # * Inserta en la lista general
        self.lista.append(afiliado)

    def eliminar_lista(self, numero_identificacion):
        """
        Elimina un afiliado de la lista buscando por número de identificación.
        """

        # * Buscar afiliado por ID
        for i, afiliado in enumerate(self.lista):
            if afiliado.numero_identificacion == numero_identificacion:
                return self.lista.pop(i)
        return None

    # ============================
    # REPORTES
    # ============================

    def reporte_pila(self):
        """
        Suma total de tarifas en la pila.
        """

        # * Suma todas las tarifas de los afiliados en la pila
        return sum(a.tarifa_afiliacion for a in self.pila)

    def reporte_cola(self):
        """
        Cantidad de afiliados en la cola.
        """

        # * Retorna el número de elementos en la cola
        return len(self.cola)

    def reporte_lista(self):
        """
        Promedio de ingresos de la lista de afiliados.
        """

        # * Validación de lista vacía
        if len(self.lista) == 0:
            return 0

        # * Cálculo del promedio de ingresos
        return sum(a.ingresos for a in self.lista) / len(self.lista)
