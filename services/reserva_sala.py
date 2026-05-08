from models.servicio import Servicio

# Clase hija que hereda de la clase abstracta Servicio
class ReservaSala(Servicio):

    def __init__(self, horas):
        # Se define automáticamente:
        # nombre del servicio
        # tarifa por hora
        # horas ingresadas por el usuario
        super().__init__("Reserva de sala", 50000, horas)

    # Implementación obligatoria del método abstracto
    def calcular_costo(self, iva=0.19, cupon=None):

        # Validación:
        # La reserva debe ser superior a 2 horas
        if self.get_horas() <= 2:
            raise ValueError("La reserva de sala debe ser superior a 2 horas.")

        # Cálculo del costo base
        subtotal = self.get_tarifa() * self.get_horas()

        # Se agrega el IVA
        total = subtotal + (subtotal * iva)

        # Si existe un cupón, se descuenta
        if cupon:
            total -= cupon

        # Retorna el valor final
        return total

    # Polimorfismo:
    # Se sobrescribe el método descripcion de la clase padre
    def descripcion(self):
        return f"El servicio seleccionado es reserva de sala por {self.get_horas()} horas."