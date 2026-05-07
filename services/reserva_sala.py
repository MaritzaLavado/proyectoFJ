from models.servicio import Servicio

#ACA VALIDAR QUE SEA SUPERIOR A 2 HORAS
class reserva_sala(Servicio):
    def __init__(self, horas):
        # Modifique el nombre de esta hija y la tarifa  (Por hora)
        super().__init__("Asesoría", 200000, horas)

    def descripcion(self):
        
        mensaje_base = super().descripcion()  # Usamos el mensaje base del padre (EN CADA CLASE)
        # Le concatenamos los detalles especificos por clase hija (tipo de asesoria)
        pass

    def calcular_costo(self, iva=0.19, cupon=None):
        # Validamos que sea mayor a 0
        if self.get_horas() <= 0:
            raise ValueError("La cantidad de horas debe ser mayor a cero.")

        # Calculo base con IVA
        subtotal = self.get_tarifa() * self.get_horas() #Multiplicamos valor tarifa por cantidad de horas
        total = subtotal * (1 + iva) #Si no tiene cupon se devuelve el total mas el iva predeterminado

        # Lógica del Cupón (Sobrecarga)
        # Si cupon es None, no se hace este proceso. Si tiene un cupón, o sea un valor, lo hace.
        if cupon is not None:
            total = total * (1 - cupon) # Le resta la cantidad necesaria segun la catidad del cupon
            
        return round(total) # Devuelve el total redondeado, sin ningun decimal