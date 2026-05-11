from abc import ABC, abstractmethod
from clases.excepciones import ServicioError


class Servicio(ABC):

    def __init__(self, nombre, precio):

        if not nombre.strip():
            raise ServicioError("Nombre del servicio vacío")

        if precio <= 0:
            raise ServicioError("El precio debe ser mayor a 0")

        self.nombre = nombre
        self.precio = precio

    @abstractmethod
    def calcular_costo(self):
        pass

    @abstractmethod
    def descripcion(self):
        pass


# ==========================
# CLASE HIJA 1
# ==========================

class ReservaSala(Servicio):

    def __init__(self, nombre, precio, capacidad):

        super().__init__(nombre, precio)

        if capacidad <= 0:
            raise ServicioError("Capacidad inválida")

        self.capacidad = capacidad

    def calcular_costo(self, horas=1, impuesto=0):

        subtotal = self.precio * horas

        total = subtotal + (subtotal * impuesto)

        return total

    def descripcion(self):

        return (
            f"Reserva de Sala: {self.nombre} "
            f"| Capacidad: {self.capacidad}"
        )


# ==========================
# CLASE HIJA 2
# ==========================

class AlquilerEquipo(Servicio):

    def __init__(self, nombre, precio, tipo):

        super().__init__(nombre, precio)

        self.tipo = tipo

    def calcular_costo(self, dias=1, descuento=0):

        subtotal = self.precio * dias

        total = subtotal - (subtotal * descuento)

        return total

    def descripcion(self):

        return (
            f"Alquiler de Equipo: {self.nombre} "
            f"| Tipo: {self.tipo}"
        )


# ==========================
# CLASE HIJA 3
# ==========================

class Asesoria(Servicio):

    def __init__(self, nombre, precio, especialista):

        super().__init__(nombre, precio)

        self.especialista = especialista

    def calcular_costo(self, sesiones=1):

        return self.precio * sesiones

    def descripcion(self):

        return (
            f"Asesoría: {self.nombre} "
            f"| Especialista: {self.especialista}"
        )