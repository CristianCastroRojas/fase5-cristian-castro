# Requisitos del Usuario

Gestión de Afiliados - Caja Compensándote
Curso: 301305 - Estructura de Datos
Fase 3 - Componente práctico - Prácticas Simuladas

---

## 1. Requisitos Funcionales

RF1. El sistema debe mostrar una interfaz gráfica inicial de acceso con el título "Login - Compensándote".

RF2. El sistema debe validar el acceso mediante una contraseña enmascarada con el carácter (\*).

RF3. La contraseña de acceso será: "Caja".

RF4. El sistema debe contar con un botón "Acerca de" que muestre la información del curso, nombre del estudiante y grupo.

RF5. El sistema debe contar con un botón "Salir" que cierre la aplicación en cualquier momento.

RF6. El sistema debe contar con un botón "Ingresar" que permita acceder al formulario principal si la contraseña es correcta.

RF7. El sistema debe permitir registrar los siguientes datos del afiliado:

- Tipo de identificación (CC, CE, NUIP, PAS)
- Número de identificación (solo números)
- Nombre completo (solo letras)
- Ingresos actuales (solo números)
- Servicio deseado (Subsidio de desempleo, Ingreso a parque, Curso de formación, Paquete de viaje, Medicina preventiva)
- Modalidad de empleo (Empleado o Independiente)
- Fecha de afiliación (formato dd/mm/aaaa)

RF8. El sistema debe calcular automáticamente la tarifa de afiliación según los ingresos, modalidad de empleo y servicio seleccionado.

RF9. El sistema debe permitir seleccionar la estructura de datos a utilizar (Pila, Cola o Lista).

RF10. El sistema debe registrar los datos en un componente tipo Treeview según la estructura seleccionada.

RF11. El sistema debe contar con un botón "Registrar" para almacenar los datos en la estructura seleccionada.

RF12. El sistema debe contar con un botón "Limpiar" que borre los campos del formulario sin afectar los datos almacenados.

RF13. El sistema debe contar con un botón "Eliminar" que elimine registros según el comportamiento de la estructura:

- Pila: desapilar
- Cola: desencolar
- Lista: eliminar por identificación

RF14. El sistema debe solicitar confirmación antes de eliminar un registro.

RF15. El sistema debe contar con un botón "Reporte" que muestre:

- Pila: suma de tarifas
- Cola: cantidad de registros
- Lista: promedio de ingresos

RF16. El sistema debe mostrar los resultados del reporte en un campo no editable.

---

## 2. Requisitos No Funcionales

RNF1. La aplicación debe desarrollarse en lenguaje Python.

RNF2. La aplicación debe utilizar programación orientada a objetos (POO).

RNF3. La aplicación debe implementar estructuras de datos lineales (Pila, Cola y Lista).

RNF4. La aplicación debe utilizar una interfaz gráfica de usuario (GUI).

RNF5. La aplicación no debe usar bases de datos ni archivos; los datos se almacenan en memoria.

RNF6. La aplicación debe validar correctamente los datos ingresados por el usuario.

RNF7. La interfaz debe ser clara, intuitiva y fácil de usar.

RNF8. Los campos calculados no deben ser editables por el usuario.

RNF9. La aplicación debe contener una clase principal llamada `EstructuraDatosAfiliado` para gestionar los datos.

---

## 3. Reglas de Negocio

RN1. El acceso al sistema solo es permitido si la contraseña es exactamente "Caja".

RN2. La tarifa de afiliación depende de la modalidad de empleo:

### Empleado:

- $1.000.000 - $2.000.000 → $45.000
- $2.000.000 - $3.000.000 → $60.000
- $3.000.000 - $4.000.000 → $75.000
- $4.000.000 - $5.000.000 → $90.000
- Menor $5.000.000 → $150.000

### Independiente:

- $1.000.000 - $2.000.000 → $10.000
- $2.000.000 - $3.000.000 → $20.000
- $3.000.000 - $4.000.000 → $30.000
- $4.000.000 - $5.000.000 → $40.000
- Menor $5.000.000 → $80.000

RN3. La tarifa se ajusta según el servicio:

- Subsidio de desempleo: sin cambio
- Ingreso a parque: + $2.500
- Curso de formación: + $7.500
- Paquete de viaje: + $10.000
- Medicina preventiva: + 10% de los ingresos

RN4. Los datos deben almacenarse en memoria usando estructuras de datos:

- Pila: comportamiento LIFO
- Cola: comportamiento FIFO
- Lista: colección ordenada

RN5. La fecha de afiliación debe ser seleccionada por el usuario mediante un control de fecha.

RN6. La eliminación de datos debe respetar la estructura seleccionada.

---
