# ============================
# IMPORTACIONES
# ============================
from datetime import datetime


# ============================
# CLASE: ESTRUCTURA DE DATOS AFILIADO
# ============================
class EstructuraDatosAfiliado:
    """
    Clase que representa la estructura de datos de un afiliado.
    """

    def __init__(
        self,
        tipo_identificacion: str,
        numero_identificacion: int,
        nombre_completo: str,
        ingresos: float,
        servicio: str,
        modalidad: str,
        estructura: str,
    ):

        # ============================
        # ASIGNACIÓN DE ATRIBUTOS
        # ============================
        self.tipo_identificacion = tipo_identificacion
        self.numero_identificacion = numero_identificacion
        self.nombre_completo = nombre_completo
        self.ingresos = ingresos
        self.servicio = servicio
        self.modalidad = modalidad
        self.estructura = estructura

        # * Resultado del cálculo de afiliación
        self.tarifa_afiliacion = 0

        # * Fecha en la que se registra el afiliado
        self.fecha_afiliacion = datetime.now().strftime("%d/%m/%Y")

    # ============================
    # MÉTODO: CALCULAR TARIFA DE AFILIACIÓN
    # ============================
    def calcular_tarifa_afiliacion(self):

        # * Ingreso base del afiliado
        ingresos = self.ingresos
        tarifa = 0

        # ============================
        # TARIFA SEGÚN MODALIDAD
        # ============================

        # * Caso: empleado
        if self.modalidad.lower() == "empleado":

            if 1_000_000 <= ingresos < 2_000_000:
                tarifa = 45000
            elif 2_000_000 <= ingresos < 3_000_000:
                tarifa = 60000
            elif 3_000_000 <= ingresos < 4_000_000:
                tarifa = 75000
            elif 4_000_000 <= ingresos < 5_000_000:
                tarifa = 90000
            else:
                tarifa = 150000

        # * Caso: independiente
        else:

            if 1_000_000 <= ingresos < 2_000_000:
                tarifa = 10000
            elif 2_000_000 <= ingresos < 3_000_000:
                tarifa = 20000
            elif 3_000_000 <= ingresos < 4_000_000:
                tarifa = 30000
            elif 4_000_000 <= ingresos < 5_000_000:
                tarifa = 40000
            else:
                tarifa = 80000

        # ============================
        # AJUSTE SEGÚN SERVICIO
        # ============================

        if self.servicio == "Ingreso a parque":
            tarifa += 2500

        elif self.servicio == "Curso de formación":
            tarifa += 7500

        elif self.servicio == "Paquete de viaje":
            tarifa += 10000

        elif self.servicio == "Medicina preventiva":
            tarifa += ingresos * 0.10

        # * Guardar resultado final
        self.tarifa_afiliacion = tarifa

        return tarifa
