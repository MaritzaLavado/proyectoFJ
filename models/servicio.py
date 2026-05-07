from abc import ABC, abstractmethod

class Servicio(ABC):
    def __init__(self, nombre, tarifa, horas):
        self.__nombre = nombre
        self.__tarifa = tarifa  # Este valor vendrá predefinido por las hijas
        self.__horas = horas

    @abstractmethod
    def calcularCosto(self, iva=0.19, descuento=None):
        #Cada Hija debe de llevar su cálculo especifico usando los atributos internos
        pass

    def descripcion(self):
        return f"El servicio que ha seleccionado es: {self.get_nombre()}"
    
    #Getters para obtener datos privados
    def get_nombre(self):
        return self.__nombre

    def get_tarifa(self):
        return self.__tarifa

    def get_horas(self):
        return self.__horas
