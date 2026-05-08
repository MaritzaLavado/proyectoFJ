from models.servicio import Servicio

# Clase hija que hereda de la clase abstracta Servicio
class ReservaSala(Servicio):

    def __init__(self, horas):
        # Se define automáticamente el nombre del servicio,
        # la tarifa por hora y las horas ingresadas por el usuario
        super().__init__("Reserva de sala", 50000, horas)

    # Implementación del método abstracto de la clase padre
    def calcular_costo(self, iva=0.19, cupon=None):

        # Validación:
        # La reserva debe ser superior a 2 horas
        if self.get_horas() <= 2:
            raise ValueError("La reserva de sala debe ser superior a 2 horas.")

        # Se calcula el costo base
        subtotal = self.get_tarifa() * self.get_horas()

        # Se agrega el IVA al subtotal
        total = subtotal + (subtotal * iva)

        # Si existe un cupón, se aplica descuento
        if cupon:
            total -= cupon

        # Retorna el costo final
        return total

    # Polimorfismo:
    # Se sobrescribe el método descripcion()
    # para explicar brevemente en qué consiste el servicio
    def descripcion(self):
        return (
            "El servicio de reserva de sala está disponible "
            "para reservas superiores a 2 horas y permite "
            "acceder a espacios adecuados para reuniones, "
            "eventos o actividades empresariales."
        )