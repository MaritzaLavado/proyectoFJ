from abc import ABC, abstractmethod

class Servicio(ABC):
    def __init__(self, nombre=""):
        self._nombre = nombre

    @abstractmethod
    def calcular_costo(self, *args, **kwargs):
        return 0

    @abstractmethod
    def descripcion(self):
        return "Servicio base"