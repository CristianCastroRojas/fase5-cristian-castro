# ============================
# CONFIGURACIÓN DE VENTANA PRINCIPAL
# ============================

# * Ancho de la ventana principal de la aplicación
ANCHO_VENTANA = 900

# * Alto de la ventana principal de la aplicación
ALTO_VENTANA = 650


# ============================
# PALETA DE COLORES DE LA INTERFAZ
# ============================

# * Color de fondo general de la aplicación
COLOR_FONDO = "#f8f9fa"

# * Color principal usado en botones y encabezados
COLOR_PRIMARIO = "#1a73e8"

# * Color para acciones exitosas o positivas
COLOR_EXITO = "#34a853"

# * Color para acciones de peligro o eliminación
COLOR_PELIGRO = "#ea4335"

# * Color blanco para tarjetas y fondos internos
COLOR_BLANCO = "#ffffff"

# * Color del borde del canvas del árbol
COLOR_CANVAS_BORDE = "#ddd"

# * Color de las líneas de conexión del árbol
COLOR_LINEA = "#999"


# ============================
# COLORES POR NIVEL DEL ÁRBOL
# ============================

# * Nivel 1 del árbol (raíz o nivel superior)
COLOR_NIVEL_1 = "#ea4335"

# * Nivel 2 del árbol
COLOR_NIVEL_2 = "#1a73e8"

# * Nivel 3 del árbol
COLOR_NIVEL_3 = "#34a853"

# * Nivel 4 del árbol
COLOR_NIVEL_4 = "#f29900"

# * Color por defecto para niveles mayores o no definidos
COLOR_NIVEL_DEFAULT = "gray"

# * Color de resaltado para nodo recién agregado
COLOR_BORDE_NUEVO = "gold"


# ============================
# TEXTOS DE LA INTERFAZ
# ============================

# * Texto del campo de entrada del usuario
TEXTO_INPUT = "Ingrese un número entero:"

# * Etiqueta del recorrido en preorden
TEXTO_PREORDEN = "PREORDEN"

# * Etiqueta del recorrido en inorden
TEXTO_INORDEN = "INORDEN"

# * Etiqueta del recorrido en posorden
TEXTO_POSORDEN = "POSORDEN"


# ============================
# MENSAJES DEL SISTEMA
# ============================

# * Error cuando el campo está vacío
ERROR_VACIO = "El campo no puede estar vacío"

# * Error cuando el usuario ingresa algo que no es entero
ERROR_SOLO_ENTEROS = "Solo se permiten números enteros"

# * Error cuando el valor está fuera del rango permitido
ERROR_RANGO_EXCEDIDO = (
    "El valor excede el rango de un entero de 32 bits (-2147483648 a 2147483647)"
)

# * Error genérico del sistema
ERROR_GENERAL = "Error"


# ============================
# MENSAJES DE RESULTADO
# ============================

# * Mensaje cuando el nodo existe en el árbol
MSG_EXISTE = "El nodo {valor} existe en el árbol"

# * Mensaje cuando el nodo no existe en el árbol
MSG_NO_EXISTE = "El nodo {valor} NO existe"
