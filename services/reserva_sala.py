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
    # concatenando el mensaje base del padre con el detalle específico
    def descripcion(self):
        mensaje_base = super().descripcion()  # Llama al método de la clase padre
        detalles = (
            f" Has reservado una sala de reuniones por "
            f"{self.get_horas()} horas con una tarifa de "
            f"{self.get_tarifa()} por hora."
        )
        return f"{mensaje_base}{detalles}"
