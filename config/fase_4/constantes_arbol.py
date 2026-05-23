# ============================
# CONFIGURACIÓN DEL ÁRBOL BINARIO
# ============================

# Este archivo almacena constantes relacionadas
# con las reglas de funcionamiento del árbol
# y los mensajes de validación del sistema.

# Tener estos valores centralizados permite
# modificar reglas sin cambiar la lógica principal.


# ============================
# REGLAS DEL ÁRBOL
# ============================

# Cantidad máxima de niveles permitidos
# en el Árbol Binario de Búsqueda.
#
# Nivel 1 → raíz
# Nivel 2 → hijos de la raíz
# Nivel 3 → nietos
# Nivel 4 → último nivel permitido
#
# Si se intenta insertar un nodo más profundo,
# el sistema genera una excepción.
MAX_NIVELES = 4


# ============================
# MENSAJES DE ERROR
# ============================

# Mensaje mostrado cuando el árbol
# supera el límite permitido de niveles.
ERROR_MAX_NIVELES = "No se puede exceder los 4 niveles"

# Mensaje mostrado cuando se intenta
# insertar un valor que ya existe.
#
# El Árbol Binario de Búsqueda implementado
# no admite valores repetidos.
ERROR_DUPLICADO = "No se permiten duplicados"
