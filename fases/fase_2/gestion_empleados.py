# ============================
# IMPORTACIONES
# ============================
from datetime import datetime


# ============================
# CLASE ABSTRACTA EMPLEADO
# ============================
class GestionEmpleados:
    """Clase que representa un empleado y su lógica de nómina"""

    # ============================
    # DEFINICION DE CONSTANTES
    # ============================
    VALORES_POR_CARGO = {
        "Servicios Generales": 40000,
        "Administrativo": 50000,
        "Electricista": 60000,
        "Mecánico": 80000,
        "Soldador": 90000,
    }

    def __init__(
        self,
        identificacion: str,
        nombre_completo: str,
        genero: str,
        cargo: str,
        dias_laborados: int,
    ):

        # ============================
        # VALIDACIONES
        # ============================

        if not identificacion.isdigit() or len(identificacion) != 10:
            raise ValueError("La identificación debe ser numérica y tener 10 dígitos")

        if not nombre_completo.replace(" ", "").isalpha():
            raise ValueError("El nombre debe contener solo letras")

        if cargo not in self.VALORES_POR_CARGO:
            raise ValueError("Cargo no válido")

        if not isinstance(dias_laborados, int) or not (0 <= dias_laborados <= 31):
            raise ValueError("Los días laborados deben estar entre 0 y 31")

        # ============================
        # ASIGNACIÓN DE ATRIBUTOS
        # ============================

        self.identificacion = identificacion
        self.nombre_completo = nombre_completo
        self.genero = genero
        self.cargo = cargo
        self.dias_laborados = dias_laborados
        self.fecha_registro = datetime.now().strftime("%d/%m/%Y %H:%M")

        self.valor_dia = self.VALORES_POR_CARGO[cargo]
        self.total_pagar = self.calcular_nomina()

    # ============================
    # METODO PARA CALCULAR NOMINA
    # ============================
    def calcular_nomina(self) -> float:
        total_pagar = self.valor_dia * self.dias_laborados
        return total_pagar

    # ============================
    # METODO PARA GENERAR REPORTE
    # ============================
    def generar_reporte(self) -> dict:
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
