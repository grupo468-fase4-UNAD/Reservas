# Sistema Integral de Gestión de Clientes, Servicios y Reservas

Proyecto desarrollado para la Fase 4 del curso de Programación de la Universidad Nacional Abierta y a Distancia (UNAD).

---
## Integrantes

Carlos Alberto Vargas Soler 

Angelica Cristina Ortiz Paternina

---
## Descripción

El sistema permite gestionar clientes, servicios y reservas para la empresa ficticia Software FJ, utilizando Programación Orientada a Objetos (POO) en Python y manejo avanzado de excepciones.

El proyecto fue desarrollado sin bases de datos, utilizando estructuras de objetos, listas y archivos de texto para el registro de eventos y errores del sistema.

---
## Características principales

✔️ **Programación Orientada a Objetos** — El sistema está estructurado mediante cuatro clases principales: `Cliente`, `Servicio`, `Reserva` y la clase base abstracta `Entidad`, proporcionando una arquitectura modular y escalable.

✔️ **Clases abstractas** — Las clases `Entidad` y `Servicio` definen contratos que las subclases deben implementar, garantizando una interfaz consistente en todo el proyecto.

✔️ **Herencia** — `Cliente` hereda de `Entidad` para implementar `mostrar_info()`; mientras que `ReservaSala`, `AlquilerEquipo` y `Asesoria` heredan de `Servicio` para implementar comportamientos específicos.

✔️ **Polimorfismo** — Los métodos `calcular_costo()` y `descripcion()` se adaptan según el tipo de servicio, permitiendo que cada uno tenga su propia lógica de cálculo y descripción.

✔️ **Encapsulación** — Los datos sensibles del cliente (nombre, cédula, teléfono) se protegen como atributos privados (`__nombre`, `__cedula`), accesibles únicamente a través de getters y setters validados.

✔️ **Manejo avanzado de excepciones** — El sistema implementa bloques `try/except/else/finally` en `reserva.py` (en el método `procesar()`) y en `main.py` para capturar y gestionar errores sin interrumpir la ejecución.

✔️ **Excepciones personalizadas** — Se definen tres excepciones específicas en `excepciones.py`: `ClienteError`, `ServicioError` y `ReservaError`, proporcionando mensajes de error contextualizados.

✔️ **Registro de logs** — La función `guardar_log()` en `main.py` registra automáticamente todos los errores y excepciones en el archivo `logs.txt`, manteniendo un histórico de problemas.

✔️ **Gestión de clientes** — El sistema valida y almacena clientes en una lista interna, verificando que nombre, cédula y teléfono cumplan requisitos mínimos antes de registrarlos.

✔️ **Gestión de servicios** — Se crean y gestionan tres tipos de servicios especializados (sala, equipo, asesoría) en una lista, cada uno con parámetros y lógica de cálculo única.

✔️ **Gestión de reservas** — El sistema procesa reservas vinculando cliente, servicio y duración, confirmando el estado y calculando el costo correspondiente según parámetros específicos.

