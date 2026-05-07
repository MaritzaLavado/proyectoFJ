from abc import ABC, abstractmethod

class Servicio(ABC):
    def __init__(self, nombre, tarifa, horas):
        self.__nombre = nombre  # Este nombre sera predefinido por las hijas
        self.__tarifa = tarifa  # Este valor será predefinido por las hijas
        self.__horas = horas    # Las define el usuario, pedirlas en el main

    @abstractmethod  # Es un método abstracto
    def calcular_costo(self, iva=0.19, cupon=None):
        # Cada Hija debe de llevar su cálculo especifico usando los atributos internos
        # Todas las hijas deben usar IVA y un cupón opcional para hacer SOBRECARGA
        # Es posible cambiar el valor del IVA pero no lo haremos para mas fidelidad a la realidad
        pass

    def descripcion(self):
        return f"El servicio que ha seleccionado es: {self.get_nombre()}" # Mensaje base para cada hija
    
    #Getters para obtener datos privados
    def get_nombre(self):
        return self.__nombre

    def get_tarifa(self):
        return self.__tarifa

    def get_horas(self):
        return self.__horas
