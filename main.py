# ? Librerías necesarias para manejar rutas del sistema
import sys
import os

# ? Agrega la raíz del proyecto al PATH
# ! Permite importar módulos desde cualquier carpeta del proyecto
sys.path.insert(0, os.path.dirname(__file__))

# ? Importa la aplicación de login
from src.interfaz_login import LoginApp

# ? Punto de entrada del programa
if __name__ == "__main__":
    # * Crea la app de login
    app = LoginApp()

    # * Ejecuta la aplicación
    app.ejecutar()
