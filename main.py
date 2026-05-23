import sys
import os

# Agregar la carpeta raíz del proyecto al path para importar todos los módulos
sys.path.insert(0, os.path.dirname(__file__))

from src.interfaz_login import LoginApp

if __name__ == "__main__":
    app = LoginApp()
    app.ejecutar()
