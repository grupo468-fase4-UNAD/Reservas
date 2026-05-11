from clases.entidad import Entidad
from clases.excepciones import ClienteError


class Cliente(Entidad):

    def __init__(self, nombre, cedula, telefono):

        if not nombre.strip():
            raise ClienteError("El nombre del cliente está vacío")

        if len(str(cedula)) < 5:
            raise ClienteError("La cédula no es válida")

        if len(str(telefono)) < 7:
            raise ClienteError("El teléfono no es válido")

        self.__nombre = nombre
        self.__cedula = cedula
        self.__telefono = telefono

    # GETTERS
    def get_nombre(self):
        return self.__nombre

    def get_cedula(self):
        return self.__cedula

    def get_telefono(self):
        return self.__telefono

    # SETTERS
    def set_telefono(self, telefono):

        if len(str(telefono)) < 7:
            raise ClienteError("Teléfono inválido")

        self.__telefono = telefono

    def mostrar_info(self):

        return (
            f"Cliente: {self.__nombre} | "
            f"Cédula: {self.__cedula} | "
            f"Teléfono: {self.__telefono}"
        )