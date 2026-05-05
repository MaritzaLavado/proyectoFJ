from models.servicio import Servicio

class Asesoria(Servicio):
    def __init__(self, nombre="", tarifa_hora=0):
        super().__init__(nombre)
        self.tarifa_hora = tarifa_hora

    def calcular_costo(self, horas=1):
        return 0

    def descripcion(self):
        return "Asesoría especializada"