from datetime import datetime


# * CLASE GESTIÓN EMPLEADOS
# * Representa un empleado y administra
# * validaciones, nómina y generación de reportes.
class GestionEmpleados:

    # ==================================================
    # * CONSTANTES DE NEGOCIO
    # ==================================================

    # ? Valor pagado por día según cargo.
    VALORES_POR_CARGO = {
        "Servicios Generales": 40000,
        "Administrativo": 50000,
        "Electricista": 60000,
        "Mecánico": 80000,
        "Soldador": 90000,
    }

    # ==================================================
    # * CONSTRUCTOR
    # ==================================================

    def __init__(
        self,
        identificacion: str,
        nombre_completo: str,
        genero: str,
        cargo: str,
        dias_laborados: int,
    ):

        # ==================================================
        # * VALIDACIONES DATOS ENTRADA
        # ==================================================

        # ! Validar identificación
        if not identificacion.isdigit() or len(identificacion) != 10:

            raise ValueError(
                "La identificación debe ser numérica " "y tener 10 dígitos"
            )

        # ! Validar nombre
        if not nombre_completo.replace(
            " ",
            "",
        ).isalpha():

            raise ValueError("El nombre debe contener solo letras")

        # ! Validar cargo existente
        if cargo not in self.VALORES_POR_CARGO:

            raise ValueError("Cargo no válido")

        # ! Validar rango permitido días
        if not isinstance(
            dias_laborados,
            int,
        ) or not (0 <= dias_laborados <= 31):

            raise ValueError("Los días laborados " "deben estar entre 0 y 31")

        # ==================================================
        # * ASIGNACIÓN ATRIBUTOS
        # ==================================================

        self.identificacion = identificacion

        self.nombre_completo = nombre_completo

        self.genero = genero

        self.cargo = cargo

        self.dias_laborados = dias_laborados

        # ? Fecha automática registro sistema
        self.fecha_registro = datetime.now().strftime("%d/%m/%Y %H:%M")

        # ? Obtener valor diario según cargo
        self.valor_dia = self.VALORES_POR_CARGO[cargo]

        # * Calcular nómina automáticamente
        self.total_pagar = self.calcular_nomina()

    # ==================================================
    # * CALCULAR NÓMINA
    # ==================================================

    def calcular_nomina(self) -> float:

        # ? Multiplica días trabajados
        # ? por valor correspondiente cargo
        total_pagar = self.valor_dia * self.dias_laborados

        return total_pagar

    # ==================================================
    # * GENERAR REPORTE
    # ==================================================

    def generar_reporte(self) -> dict:

        # ? Retorna información estructurada
        # ? para interfaz o almacenamiento.
        return {
            "identificacion": self.identificacion,
            "nombre": self.nombre_completo,
            "genero": self.genero,
            "cargo": self.cargo,
            "dias_laborados": self.dias_laborados,
            "fecha_registro": self.fecha_registro,
            "valor_dia": self.valor_dia,
            "total_pagar": self.total_pagar,
        }
