import sys
import os

# * CONFIGURACIÓN
# * Agrega la carpeta raíz del proyecto al PATH
# * para permitir importar módulos internos.
sys.path.insert(0, os.path.dirname(__file__))

# * IMPORTACIÓN
# * Clase principal de la interfaz de inicio de sesión.
from src.interfaz_login import LoginApp

# ! PUNTO DE ENTRADA PRINCIPAL
# ? Solo se ejecuta cuando este archivo se inicia directamente.
# ? Evita ejecución automática al importarlo desde otro módulo.
if __name__ == "__main__":

    # * Crear instancia principal de la aplicación
    app = LoginApp()

    # * Iniciar interfaz gráfica
    app.ejecutar()
