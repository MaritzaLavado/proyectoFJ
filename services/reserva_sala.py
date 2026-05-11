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

         # Calculo base con IVA
        subtotal = self.get_tarifa() * self.get_horas() #Multiplicamos valor tarifa por cantidad de horas
        total = subtotal * (1 + iva) #Si no tiene cupon se devuelve el total mas el iva predeterminado

        # Lógica del Cupón (Sobrecarga)
        # Si cupon es None, no se hace este proceso. Si tiene un cupón, o sea un valor, lo hace.
        if cupon is not None:
            total = total * (1 - cupon) # Le resta la cantidad necesaria segun la catidad del cupon
            
        return round(total) # Devuelve el total redondeado, sin ningun decimal

    # Polimorfismo:
    # Se sobrescribe el método descripcion()
    # para explicar brevemente en qué consiste el servicio
    
    def descripcion(self):
        
        mensaje_base = super().descripcion()  # Usamos el mensaje base del padre (EN CADA CLASE)
        # Le concatenamos los detalles especificos por clase hija (tipo de asesoria)
        detalles = (f". \nPara este servicio se cobra por hora ${self.get_tarifa():,}\n"
                   f"El servicio de reserva de sala está disponible para reservas superiores a 2 horas\n" 
                   f"y acceder a espacios adecuados para reuniones, eventos o actividades empresariales\n")
        return mensaje_base + detalles