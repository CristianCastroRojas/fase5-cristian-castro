# * GESTOR DE AFILIADOS
# ? Administra estructuras de datos del sistema
class GestionAfiliados:
    """
    Clase encargada de gestionar las estructuras de datos:
    Pila, Cola y Lista para el sistema de afiliados.
    """

    # * CONSTRUCTOR PRINCIPAL
    # ? Inicializa estructuras en memoria
    def __init__(self):
        """
        Inicializa las estructuras de datos en memoria:
        - Pila (LIFO)
        - Cola (FIFO)
        - Lista (colección general)
        """

        # * ESTRUCTURA PILA
        # ? Último en entrar primero en salir
        self.pila = []

        # * ESTRUCTURA COLA
        # ? Primero en entrar primero en salir
        self.cola = []

        # * ESTRUCTURA LISTA
        # ? Almacenamiento general afiliados
        self.lista = []

    # ==================================
    # * PILA (LIFO)
    # ==================================

    # * APILAR AFILIADO
    # ? Agrega elemento al final pila
    def apilar(self, afiliado):
        """
        Inserta un afiliado en la estructura tipo Pila (LIFO).

        Parámetros:
            afiliado (EstructuraDatosAfiliado)
        """

        self.pila.append(afiliado)

    # * DESAPILAR AFILIADO
    # ? Extrae último elemento agregado
    def desapilar(self):
        """
        Elimina y retorna el último afiliado agregado.
        """

        # ! Validar pila con elementos
        if len(self.pila) > 0:

            return self.pila.pop()

        return None

    # ==================================
    # * COLA (FIFO)
    # ==================================

    # * ENCOLAR AFILIADO
    # ? Agrega afiliado al final cola
    def encolar(self, afiliado):
        """
        Inserta un afiliado en Cola.
        """

        self.cola.append(afiliado)

    # * DESENCOLAR AFILIADO
    # ? Extrae primer elemento registrado
    def desencolar(self):
        """
        Elimina y retorna el primer afiliado.
        """

        # ! Validar cola con registros
        if len(self.cola) > 0:

            return self.cola.pop(0)

        return None

    # ==================================
    # * LISTA
    # ==================================

    # * AGREGAR REGISTRO LISTA
    # ? Inserta afiliado colección general
    def agregar_lista(self, afiliado):
        """
        Agrega afiliado al final lista.
        """

        self.lista.append(afiliado)

    # * ELIMINAR REGISTRO LISTA
    # ? Busca afiliado por identificación
    def eliminar_lista(self, numero_identificacion):
        """
        Elimina afiliado usando identificación.
        """

        # ? Recorrido lista completa
        for i, afiliado in enumerate(self.lista):

            # ? Comparación identificación
            if afiliado.numero_identificacion == numero_identificacion:

                return self.lista.pop(i)

        # ! Afiliado no encontrado
        return None

    # ==================================
    # * REPORTES
    # ==================================

    # * REPORTE PILA
    # ? Suma tarifas afiliación registradas
    def reporte_pila(self):
        """
        Calcula total tarifas afiliación.
        """

        return sum(a.tarifa_afiliacion for a in self.pila)

    # * REPORTE COLA
    # ? Cuenta registros almacenados
    def reporte_cola(self):
        """
        Retorna cantidad afiliados cola.
        """

        return len(self.cola)

    # * REPORTE LISTA
    # ? Calcula promedio ingresos
    def reporte_lista(self):
        """
        Calcula promedio ingresos afiliados.
        """

        # ! Evitar división entre cero
        if len(self.lista) == 0:

            return 0

        return sum(a.ingresos for a in self.lista) / len(self.lista)
