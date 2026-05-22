# Requisitos del Usuario

# Aplicación Integradora – Fase 5 Validación Integral y Sustentación

**Curso:** 301305 – Estructura de Datos
**Fase:** 5 – Validación Integral y Sustentación

---

# 1. Requisitos Funcionales

**RF1.** El sistema debe mostrar una interfaz gráfica inicial con el título:

```text
Evaluación Final
```

**RF2.** La interfaz inicial debe mostrar:

- Nombre de la aplicación
- Nombre del estudiante

**RF3.** El sistema debe disponer de una caja de texto para ingresar una contraseña de acceso.

**RF4.** La contraseña debe visualizarse de forma enmascarada mediante caracteres (\*).

**RF5.** La contraseña genérica del sistema debe ser:

```text
8246
```

**RF6.** El sistema debe contar con un botón **"Ingresar"** para validar la contraseña.

**RF7.** El sistema debe mostrar un mensaje de error cuando la contraseña sea incorrecta.

**RF8.** El sistema debe permitir el acceso al menú principal cuando la contraseña sea correcta.

**RF9.** El sistema debe mostrar un menú principal con las siguientes opciones:

```text
Opción 1: Llamar aplicación Fase 2

Opción 2: Llamar aplicación Fase 3

Opción 3: Llamar aplicación Fase 4

Opción 4: Salir
```

**RF10.** El sistema debe permitir acceder directamente a la aplicación correspondiente de la Fase 2.

**RF11.** El sistema debe permitir acceder directamente a la aplicación correspondiente de la Fase 3.

**RF12.** El sistema debe permitir acceder directamente a la aplicación correspondiente de la Fase 4.

**RF13.** Las aplicaciones integradas no deben volver a solicitar contraseña de acceso.

**RF14.** El sistema debe permitir cerrar completamente la aplicación mediante la opción **"Salir"**.

**RF15.** El sistema debe integrar las tres aplicaciones en una única solución funcional.

---

# 2. Requisitos No Funcionales

**RNF1.** La aplicación debe desarrollarse en lenguaje Python.

**RNF2.** La aplicación debe utilizar Programación Orientada a Objetos (POO).

**RNF3.** La aplicación debe utilizar una interfaz gráfica de usuario (GUI).

**RNF4.** La aplicación debe ejecutarse localmente sin conexión a internet.

**RNF5.** La aplicación no debe utilizar bases de datos.

**RNF6.** Los datos deben mantenerse en memoria durante la ejecución.

**RNF7.** La interfaz debe ser clara, organizada e intuitiva.

**RNF8.** El sistema debe manejar adecuadamente errores y excepciones.

**RNF9.** El código debe estar organizado en clases y módulos independientes.

**RNF10.** La solución debe integrar las aplicaciones desarrolladas en las fases 2, 3 y 4 en un único proyecto.

---

# 3. Reglas de Negocio

**RN1.** El acceso al sistema solo será permitido si la contraseña ingresada es exactamente:

```text
8246
```

**RN2.** Una vez autenticado el usuario, no debe solicitarse nuevamente contraseña al ingresar a las aplicaciones integradas.

**RN3.** La aplicación debe permitir únicamente acceder a las opciones disponibles en el menú principal.

**RN4.** La opción **"Salir"** debe finalizar completamente la ejecución del sistema.

**RN5.** La integración debe conservar el funcionamiento original de las aplicaciones desarrolladas en las fases 2, 3 y 4.

**RN6.** Las aplicaciones deben ejecutarse desde una única interfaz integradora.

---

# Estructura esperada de la aplicación

```text
Evaluación Final
│
├── Acceso con contraseña (8246)
│
└── Menú principal
    │
    ├── Fase 2
    ├── Fase 3
    ├── Fase 4
    └── Salir
```
