from models.servicio import Servicio

class ReservaSala(Servicio):
    def __init__(self, nombre="", precio_hora=0):
        super().__init__(nombre)
        self.precio_hora = precio_hora

    def calcular_costo(self, horas=1, descuento=0):
        return 0

    def descripcion(self):
        return "Reserva de sala"