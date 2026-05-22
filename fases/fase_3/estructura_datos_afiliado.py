# ============================
# CLASE ESTRUCTURA DE DATOS AFILIADO
# ============================

from datetime import datetime


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
        self.tipo_identificacion = tipo_identificacion
        self.numero_identificacion = numero_identificacion
        self.nombre_completo = nombre_completo
        self.ingresos = ingresos
        self.servicio = servicio
        self.modalidad = modalidad
        self.estructura = estructura

        self.tarifa_afiliacion = 0
        self.fecha_afiliacion = datetime.now().strftime("%d/%m/%Y")

    def calcular_tarifa_afiliacion(self):
        ingresos = self.ingresos
        tarifa = 0

        # Tarifa según modalidad y ingresos
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

        else:  # independiente
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

        # Ajuste por servicio
        if self.servicio == "Ingreso a parque":
            tarifa += 2500
        elif self.servicio == "Curso de formación":
            tarifa += 7500
        elif self.servicio == "Paquete de viaje":
            tarifa += 10000
        elif self.servicio == "Medicina preventiva":
            tarifa += ingresos * 0.10

        self.tarifa_afiliacion = tarifa
        return tarifa
