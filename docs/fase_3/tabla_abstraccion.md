# Tabla de Abstracción - Fase 3

**Nombre del Estudiante:** Cristian Andrés Castro Rojas

**Planteamiento del problema:**
La Caja de Compensación Familiar Compensándote requiere una aplicación que permita gestionar el registro de afiliados mediante una interfaz gráfica desarrollada en Python. El sistema debe permitir el ingreso, almacenamiento y procesamiento de datos de los usuarios utilizando estructuras de datos lineales (pila, cola y lista), además de calcular la tarifa de afiliación según los ingresos, tipo de empleo y servicio seleccionado. La aplicación debe generar reportes según la estructura utilizada y permitir operaciones como insertar, eliminar y visualizar los datos.

### Tabla de Abstracción Lógica

| Nombre de la Clase y su Ámbito de Visibilidad ya Sea (public o Private)                   | Nombre de Las Propiedades Y/o atributos De la clase Con sus tipos De datos.                                                                                                                                                                                                                                                                                                                                | Nombre del método Para utilizar para Realizar el cálculo.                             | Fórmula Matemática Para utilizar En el Método Para Realizar el Calculo                         |
| :---------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------ | :--------------------------------------------------------------------------------------------- |
| **Clase:** `EstructuraDatosAfiliado`<br><br>**Ámbito de Visibilidad:** `Public` (Pública) | <ul><li>`tipo_identificacion` (String / str)</li><li>`numero_identificacion` (Entero / int)</li><li>`nombre_completo` (String / str)</li><li>`ingresos` (Flotante / float)</li><li>`servicio` (String / str)</li><li>`modalidad` (String / str)</li><li>`tarifa_afiliacion` (Flotante / float)</li><li>`fecha_afiliacion` (String / str)</li><li>`estructura` (String / str: pila, cola o lista)</li></ul> | `calcular_tarifa()`<br><br>_(Calcula la tarifa según ingresos, modalidad y servicio)_ | **Cálculo de Tarifa:**<br><br>`Tarifa Base (según ingresos y modalidad) + Ajuste por servicio` |

---

### Métodos adicionales (comportamiento de estructuras)

- `apilar()` → Inserta datos en la pila (LIFO)
- `desapilar()` → Elimina el último elemento de la pila

- `encolar()` → Inserta datos en la cola (FIFO)
- `desencolar()` → Elimina el primer elemento de la cola

- `agregar_lista()` → Agrega elementos al final de la lista
- `eliminar_lista(id)` → Elimina un afiliado por identificación

---

### Métodos de reporte

- `reporte_pila()` → Suma total de tarifas
- `reporte_cola()` → Cantidad de registros
- `reporte_lista()` → Promedio de ingresos
