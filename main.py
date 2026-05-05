from models.cliente import Cliente
from models.reserva import Reserva

from services.reserva_sala import ReservaSala
from services.alquiler_equipo import AlquilerEquipo
from services.asesoria import Asesoria

from utils.logger import log_error


def main():
    clientes = []
    servicios = []
    reservas = []

    try:
        # Crear objetos base (sin lógica aún)
        cliente = Cliente()
        servicio1 = ReservaSala()
        servicio2 = AlquilerEquipo()
        servicio3 = Asesoria()

        reserva = Reserva(cliente, servicio1, 1)

        # Guardar en listas
        clientes.append(cliente)
        servicios.extend([servicio1, servicio2, servicio3])
        reservas.append(reserva)

        # Operaciones básicas
        reserva.confirmar()

    except Exception as e:
        log_error(str(e))


if __name__ == "__main__":
    main()