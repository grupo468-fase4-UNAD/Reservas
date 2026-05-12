from clases.cliente import Cliente
from clases.reserva import Reserva
from clases.servicio import Servicio
from clases.excepciones import SistemaError


class SistemaFJ:

    def __init__(self):
        self.clientes = []
        self.servicios = []
        self.reservas = []

    def registrar_cliente(self, nombre, cedula, telefono):
        try:
            cliente = Cliente(nombre, cedula, telefono)
        except Exception as error:
            raise SistemaError(
                "No se pudo registrar el cliente"
            ) from error

        if any(c.get_cedula() == cliente.get_cedula()
               for c in self.clientes):
            raise SistemaError("Cliente ya registrado")

        self.clientes.append(cliente)
        return cliente

    def registrar_servicio(self, servicio):
        if servicio is None or not isinstance(servicio, Servicio):
            raise SistemaError("Servicio inválido")

        if any(s.nombre == servicio.nombre
               for s in self.servicios):
            raise SistemaError("Servicio ya existe")

        self.servicios.append(servicio)
        return servicio

    def crear_reserva(self, cliente, servicio, duracion):
        if cliente not in self.clientes:
            raise SistemaError("Cliente no registrado en el sistema")

        if servicio not in self.servicios:
            raise SistemaError("Servicio no disponible en el sistema")

        try:
            reserva = Reserva(cliente, servicio, duracion)
        except Exception as error:
            raise SistemaError(
                "No se pudo crear la reserva"
            ) from error

        self.reservas.append(reserva)
        return reserva

    def cancelar_reserva(self, reserva):
        if reserva not in self.reservas:
            raise SistemaError("Reserva no encontrada")

        reserva.cancelar()
        return reserva

    def buscar_cliente_por_cedula(self, cedula):
        for cliente in self.clientes:
            if cliente.get_cedula() == cedula:
                return cliente
        return None

    def buscar_servicio_por_nombre(self, nombre):
        for servicio in self.servicios:
            if servicio.nombre == nombre:
                return servicio
        return None
