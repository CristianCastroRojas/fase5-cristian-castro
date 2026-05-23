# =========================
# CONFIGURACIÓN DE LA VENTANA PRINCIPAL
# =========================

# Ancho fijo de la interfaz principal
ANCHO_VENTANA = 900

# Alto fijo de la interfaz principal
ALTO_VENTANA = 650


# =========================
# COLORES DE LA INTERFAZ (UI)
# =========================

# Color de fondo general de la aplicación
COLOR_FONDO = "#f8f9fa"

# Color principal usado en botones y encabezados
COLOR_PRIMARIO = "#1a73e8"

# Color utilizado para acciones exitosas
COLOR_EXITO = "#34a853"

# Color utilizado para botones de peligro o eliminación
COLOR_PELIGRO = "#ea4335"

# Color blanco para fondos y textos
COLOR_BLANCO = "#ffffff"

# Color del borde del canvas donde se dibuja el árbol
COLOR_CANVAS_BORDE = "#ddd"

# Color de las líneas que conectan los nodos
COLOR_LINEA = "#999"


# =========================
# COLORES POR NIVEL DEL ÁRBOL
# =========================

# Nodo raíz (nivel 1)
COLOR_NIVEL_1 = "#ea4335"

# Segundo nivel del árbol
COLOR_NIVEL_2 = "#1a73e8"

# Tercer nivel del árbol
COLOR_NIVEL_3 = "#34a853"

# Cuarto nivel del árbol
COLOR_NIVEL_4 = "#f29900"

# Color por defecto si se supera la configuración definida
COLOR_NIVEL_DEFAULT = "gray"

# Color especial para resaltar el último nodo agregado
COLOR_BORDE_NUEVO = "gold"


# =========================
# TEXTOS DE LA INTERFAZ
# =========================

# Texto mostrado sobre el campo de entrada
TEXTO_INPUT = "Ingrese un número entero:"

# Título del recorrido Preorden
TEXTO_PREORDEN = "PREORDEN"

# Título del recorrido Inorden
TEXTO_INORDEN = "INORDEN"

# Título del recorrido Posorden
TEXTO_POSORDEN = "POSORDEN"


# =========================
# MENSAJES DE VALIDACIÓN Y ERROR
# =========================

# Mensaje cuando el usuario no escribe ningún dato
ERROR_VACIO = "El campo no puede estar vacío"

# Mensaje cuando se ingresa algo distinto a números enteros
ERROR_SOLO_ENTEROS = "Solo se permiten números enteros"

# Mensaje cuando el número supera el rango permitido
ERROR_RANGO_EXCEDIDO = (
    "El valor excede el rango de un entero de 32 bits " "(-2147483648 a 2147483647)"
)

# Título general para ventanas de error
ERROR_GENERAL = "Error"


# =========================
# MENSAJES DE BÚSQUEDA EN EL ÁRBOL
# =========================

# Mensaje cuando el nodo sí existe
MSG_EXISTE = "El nodo {valor} existe en el árbol"

# Mensaje cuando el nodo no se encuentra
MSG_NO_EXISTE = "El nodo {valor} NO existe"
