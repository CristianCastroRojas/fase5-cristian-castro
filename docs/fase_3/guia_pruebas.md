# Guía de Pruebas - Sistema de Gestión de Afiliados

Esta guía describe los pasos necesarios para validar el correcto funcionamiento de las estructuras de datos lineales y la lógica de negocio del sistema.

---

## 1. Prueba de Estructura: PILA (LIFO - Last In, First Out)
El último elemento en entrar debe ser el primero en salir al eliminar.

1.  **Registro 1**: Selecciona "Pila", llena los datos y pulsa **Registrar**.
2.  **Registro 2**: Llena datos para un segundo afiliado y pulsa **Registrar**.
3.  **Verificación de Orden**: Observa que ambos aparecen en la tabla.
4.  **Eliminación**: Pulsa el botón **Eliminar**.
5.  **Resultado Esperado**: El sistema debe eliminar al **segundo** afiliado (el último que registraste).
6.  **Reporte**: Pulsa **Reporte**. Debe mostrar la sumatoria exacta de las tarifas de los afiliados que aún quedan en la pila.

---

## 2. Prueba de Estructura: COLA (FIFO - First In, First Out)
El primer elemento en entrar debe ser el primero en salir al eliminar.

1.  **Registro 1**: Selecciona "Cola", llena los datos (ej: ID 100) y pulsa **Registrar**.
2.  **Registro 2**: Llena datos para otro afiliado (ej: ID 200) y pulsa **Registrar**.
3.  **Eliminación**: Pulsa el botón **Eliminar**.
4.  **Resultado Esperado**: El sistema debe eliminar al **primer** afiliado (ID 100), respetando el orden de llegada.
5.  **Reporte**: Pulsa **Reporte**. Debe mostrar la cantidad exacta de afiliados que quedan haciendo fila (ej: `Cantidad: 1 registros`).

---

## 3. Prueba de Estructura: LISTA (Colección Indexada)
Permite gestionar los datos de forma general y eliminar por búsqueda específica.

1.  **Registros múltiples**: Selecciona "Lista" y registra al menos 3 afiliados con diferentes IDs.
2.  **Selección**: Haz clic en el segundo afiliado directamente en la tabla (grilla).
3.  **Verificación de Precarga**: Comprueba que sus datos suben automáticamente al formulario.
4.  **Eliminación Específica**: Con el ID cargado en el formulario, pulsa **Eliminar**.
5.  **Resultado Esperado**: Solo se debe borrar ese registro específico de la tabla, sin importar el orden en que fue creado.
6.  **Reporte**: Pulsa **Reporte**. Debe mostrar el promedio de los ingresos actuales de los afiliados restantes.

---
