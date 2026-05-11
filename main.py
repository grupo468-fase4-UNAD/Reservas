from clases.cliente import Cliente
from clases.servicio import (
    ReservaSala,
    AlquilerEquipo,
    Asesoria
)
from clases.reserva import Reserva


# ==========================================
# FUNCIÓN PARA GUARDAR ERRORES
# ==========================================

def guardar_log(mensaje):

    with open(
        "logs.txt",
        "a",
        encoding="utf-8"
    ) as archivo:

        archivo.write(f"{mensaje}\n")


# ==========================================
# FUNCIÓN PARA GUARDAR EVENTOS
# ==========================================

def guardar_evento(mensaje):

    with open(
        "datos/eventos.txt",
        "a",
        encoding="utf-8"
    ) as archivo:

        archivo.write(f"{mensaje}\n")


# ==========================================
# INICIO DEL SISTEMA
# ==========================================

print("\n========== SOFTWARE FJ ==========\n")

guardar_evento(
    "\n========== EVENTOS DEL SISTEMA ==========\n"
)

guardar_evento(
    "Sistema iniciado correctamente\n"
)

clientes = []
servicios = []
reservas = []


# ==========================================
# OPERACIÓN 1 - CLIENTE VÁLIDO
# ==========================================

try:

    cliente1 = Cliente(
        "Carlos Vargas",
        1095402120,
        "3184020351"
    )

    clientes.append(cliente1)

    print(cliente1.mostrar_info())

    guardar_evento(
        f"Cliente registrado: "
        f"{cliente1.get_nombre()}"
    )

except Exception as e:

    print("ERROR:", e)

    guardar_log(e)


# ==========================================
# OPERACIÓN 2 - CLIENTE INVÁLIDO
# ==========================================

try:

    cliente2 = Cliente(
        "",
        123,
        "111"
    )

    clientes.append(cliente2)

except Exception as e:

    print("ERROR:", e)

    guardar_log(e)


# ==========================================
# OPERACIÓN 3 - SERVICIO SALA
# ==========================================

try:

    sala = ReservaSala(
        "Sala VIP",
        100000,
        20
    )

    servicios.append(sala)

    print(sala.descripcion())

    guardar_evento(
        f"Servicio creado: {sala.nombre}"
    )

except Exception as e:

    print("ERROR:", e)

    guardar_log(e)


# ==========================================
# OPERACIÓN 4 - SERVICIO EQUIPO
# ==========================================

try:

    equipo = AlquilerEquipo(
        "Portátil Gamer",
        50000,
        "Tecnología"
    )

    servicios.append(equipo)

    print(equipo.descripcion())

    guardar_evento(
        f"Servicio creado: {equipo.nombre}"
    )

except Exception as e:

    print("ERROR:", e)

    guardar_log(e)


# ==========================================
# OPERACIÓN 5 - SERVICIO ASESORÍA
# ==========================================

try:

    asesoria = Asesoria(
        "Python Avanzado",
        80000,
        "Ingeniero Senior"
    )

    servicios.append(asesoria)

    print(asesoria.descripcion())

    guardar_evento(
        f"Servicio creado: {asesoria.nombre}"
    )

except Exception as e:

    print("ERROR:", e)

    guardar_log(e)


# ==========================================
# OPERACIÓN 6 - RESERVA EXITOSA
# ==========================================

try:

    reserva1 = Reserva(
        cliente1,
        sala,
        3
    )

    costo = reserva1.procesar()

    reservas.append(reserva1)

    print(reserva1.mostrar_reserva())

    print("Costo:", costo)

    guardar_evento(
        f"Reserva confirmada para "
        f"{cliente1.get_nombre()}"
    )

except Exception as e:

    print("ERROR:", e)

    guardar_log(e)


# ==========================================
# OPERACIÓN 7 - RESERVA FALLIDA
# ==========================================

try:

    reserva2 = Reserva(
        cliente1,
        asesoria,
        -1
    )

except Exception as e:

    print("ERROR:", e)

    guardar_log(e)


# ==========================================
# OPERACIÓN 8 - CÁLCULO POLIMÓRFICO
# ==========================================

try:

    costo_equipo = equipo.calcular_costo(
        dias=5,
        descuento=0.10
    )

    print("Costo equipo:", costo_equipo)

    guardar_evento(
        "Cálculo de costo realizado "
        "correctamente"
    )

except Exception as e:

    print("ERROR:", e)

    guardar_log(e)


# ==========================================
# OPERACIÓN 9 - OTRA RESERVA
# ==========================================

try:

    reserva3 = Reserva(
        cliente1,
        equipo,
        2
    )

    costo = reserva3.procesar()

    reservas.append(reserva3)

    print(reserva3.mostrar_reserva())

    guardar_evento(
        f"Reserva confirmada para "
        f"{cliente1.get_nombre()}"
    )

except Exception as e:

    print("ERROR:", e)

    guardar_log(e)


# ==========================================
# OPERACIÓN 10 - ERROR FORZADO
# ==========================================

try:

    division = 10 / 0

except Exception as e:

    print("ERROR CRÍTICO:", e)

    guardar_log(e)


# ==========================================
# MOSTRAR CLIENTES
# ==========================================

print("\n========== CLIENTES ==========\n")

for cliente in clientes:

    print(cliente.mostrar_info())


# ==========================================
# MOSTRAR SERVICIOS
# ==========================================

print("\n========== SERVICIOS ==========\n")

for servicio in servicios:

    print(servicio.descripcion())


# ==========================================
# MOSTRAR RESERVAS
# ==========================================

print("\n========== RESERVAS ==========\n")

for reserva in reservas:

    print(reserva.mostrar_reserva())


# ==========================================
# FINALIZAR SISTEMA
# ==========================================

guardar_evento(
    "\nSistema finalizado correctamente\n"
)

print("\nSistema finalizado correctamente")