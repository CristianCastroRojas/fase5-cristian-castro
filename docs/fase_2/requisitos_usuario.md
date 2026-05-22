# Requisitos del Usuario

Gestión de Nómina - Constructora Mejor
Curso: 301305_80  
Fase 2 - Abstracción y Diseño

---

## 1. Requisitos Funcionales

RF1. El sistema debe mostrar una interfaz gráfica inicial de acceso con el nombre del autor y de la aplicación.

RF2. La contraseña genérica de acceso será: 4682.

RF3. El sistema debe enmascarar la contraseña ingresada (\*\*\*\* ) para ocultar los caracteres mientras se digitan.

RF4. El sistema debe solicitar los siguientes datos del empleado en la interfaz de registro:

- Identificación
- Nombre completo
- Género (Masculino o Femenino) seleccionable mediante Radio Button o lista desplegable.
- Cargo Laboral (Servicios Generales, Administrativo, Electricista, Mecánico, Soldador) seleccionable de una lista desplegable.
- Número de días laborados

RF5. El sistema debe generar automáticamente la fecha de registro al momento de diligenciar el formulario.

RF6. El sistema debe mostrar automáticamente el valor del día de trabajo según el cargo seleccionado en una caja de texto deshabilitada.

RF7. El sistema debe contar con un botón "Guardar Registro" para almacenar los datos.

RF8. El sistema debe contar con un botón "Calcular Nómina/Mostrar Reporte" que abra una interfaz con el total a pagar.

RF9. El sistema debe contar con un botón "Salir" que solicite confirmación antes de cerrar la aplicación.

---

## 2. Requisitos No Funcionales

RNF1. La aplicación debe desarrollarse en lenguaje Python.

RNF2. El entorno de desarrollo utilizado debe ser Visual Code.

RNF3. La aplicación debe contar con una interfaz gráfica amigable (GUI).

RNF4. La aplicación debe validar el acceso mediante contraseña sin solicitar nombre de usuario.

RNF5. La aplicación debe ser clara, fácil de usar y los campos calculados no deben ser editables por el usuario.

RNF6. La aplicación debe tener una clase pública llamada `GestionEmpleados` para almacenar y procesar los datos ingresados en la interfaz, incluyendo un método para calcular el costo total de la nómina.

---

## 3. Reglas de Negocio

RN1. El acceso al sistema solo se permite si la contraseña ingresada es exactamente "4682".

RN2. El valor del día de trabajo se define según el cargo de la siguiente manera:

- Servicios Generales: $ 40.000
- Administrativo: $ 50.000
- Electricista: $ 60.000
- Mecánico: $ 80.000
- Soldador: $ 90.000

RN3. El costo total del pago se calcula multiplicando el valor del día de trabajo por los días laborados.

RN4. La fecha de registro debe ser capturada automáticamente por el sistema sin intervención del usuario.
