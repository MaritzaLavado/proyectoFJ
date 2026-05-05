from models.servicio import Servicio

class AlquilerEquipo(Servicio):
    def __init__(self, nombre="", precio_dia=0):
        super().__init__(nombre)
        self.precio_dia = precio_dia

    def calcular_costo(self, dias=1):
        return 0

    def descripcion(self):
        return "Alquiler de equipo"