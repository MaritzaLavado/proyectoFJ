class Reserva:
    def __init__(self, cliente=None, servicio=None, duracion=0):
        self._cliente = cliente
        self._servicio = servicio
        self._duracion = duracion
        self._estado = "pendiente"

    def confirmar(self):
        self._estado = "confirmada"

    def cancelar(self):
        self._estado = "cancelada"

    def get_estado(self):
        return self._estado