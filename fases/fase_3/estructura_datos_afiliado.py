# * IMPORTACIÓN FECHA SISTEMA
# ? Permite registrar fecha automática afiliación
from datetime import datetime


# * CLASE ESTRUCTURA DATOS AFILIADO
# ? Representa información afiliado y cálculo tarifa
class EstructuraDatosAfiliado:
    """
    Clase que representa la estructura de datos de un afiliado.
    """

    # * CONSTRUCTOR PRINCIPAL
    # ? Inicializa atributos objeto afiliado
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

        # * DATOS PERSONALES AFILIADO
        self.tipo_identificacion = tipo_identificacion

        self.numero_identificacion = numero_identificacion

        self.nombre_completo = nombre_completo

        # * INFORMACIÓN FINANCIERA
        self.ingresos = ingresos

        # * INFORMACIÓN SERVICIO
        self.servicio = servicio

        self.modalidad = modalidad

        self.estructura = estructura

        # ? Inicialización valor tarifa
        self.tarifa_afiliacion = 0

        # * FECHA REGISTRO AUTOMÁTICA
        self.fecha_afiliacion = datetime.now().strftime("%d/%m/%Y")

    # * CALCULAR TARIFA AFILIACIÓN
    # ? Determina costo según modalidad ingresos y servicio
    def calcular_tarifa_afiliacion(self):

        ingresos = self.ingresos

        tarifa = 0

        # * TARIFA SEGÚN MODALIDAD
        # ? Diferencia empleado e independiente

        if self.modalidad.lower() == "empleado":

            # ? Primer rango salarial
            if 1_000_000 <= ingresos < 2_000_000:

                tarifa = 45000

            # ? Segundo rango salarial
            elif 2_000_000 <= ingresos < 3_000_000:

                tarifa = 60000

            # ? Tercer rango salarial
            elif 3_000_000 <= ingresos < 4_000_000:

                tarifa = 75000

            # ? Cuarto rango salarial
            elif 4_000_000 <= ingresos < 5_000_000:

                tarifa = 90000

            # ? Ingresos superiores
            else:

                tarifa = 150000

        else:

            # * MODALIDAD INDEPENDIENTE

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

        # * AJUSTE VALOR SERVICIO
        # ? Incrementa tarifa servicio seleccionado

        if self.servicio == "Ingreso a parque":

            tarifa += 2500

        elif self.servicio == "Curso de formación":

            tarifa += 7500

        elif self.servicio == "Paquete de viaje":

            tarifa += 10000

        elif self.servicio == "Medicina preventiva":

            # ! Medicina preventiva usa porcentaje ingreso
            tarifa += ingresos * 0.10

        # * GUARDAR RESULTADO FINAL
        self.tarifa_afiliacion = tarifa

        # ? Retorna valor calculado
        return tarifa
