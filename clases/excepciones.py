class ClienteError(Exception):
    """Excepción para errores de clientes"""
    pass


class ServicioError(Exception):
    """Excepción para errores de servicios"""
    pass


class ReservaError(Exception):
    """Excepción para errores de reservas"""
    pass


class SistemaError(Exception):
    """Excepción para errores del sistema"""
    pass
