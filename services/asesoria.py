from models.servicio import Servicio
    
class Asesoria(Servicio):
    def __init__(self, horas):
        # El nombre para esta hija siempre será "Asesoría" y la tarifa siempre 200.000 (Por hora)
        super().__init__("Asesoría", 200000, horas)

    def descripcion(self):
        
        mensaje_base = super().descripcion()  # Usamos el mensaje base del padre (EN CADA CLASE)
        # Le concatenamos los detalles especificos por clase hija (tipo de asesoria)
        detalles = (f". \nPara este servicio se cobra por hora ${self.get_tarifa():,}\n"
                   f"Pues, te guiamos paso a paso en soluciones de software y buenas\n" 
                   f"prácticas, resolviendo todas tus dudas de manera 100% personalizada\n")
        return mensaje_base + detalles

    def calcular_costo(self, iva=0.19, cupon=None):


        # Calculo base con IVA
        subtotal = self.get_tarifa() * self.get_horas() #Multiplicamos valor tarifa por cantidad de horas
        total = subtotal * (1 + iva) #Si no tiene cupon se devuelve el total mas el iva predeterminado

        # Lógica del Cupón (Sobrecarga)
        # Si cupon es None, no se hace este proceso. Si tiene un cupón, o sea un valor, lo hace.
        if cupon is not None:
            total = total * (1 - cupon) # Le resta la cantidad necesaria segun la catidad del cupon
            
        return round(total) # Devuelve el total redondeado, sin ningun decimal