from models.servicio import Servicio
from models.cliente import Cliente 

class Reserva:
    def __init__(self, cliente, servicio, cupon=None):
        # Valida que tenga los datos de clase cliente y clase servicio
        if not isinstance(cliente, Cliente):
            raise TypeError("Se requiere un objeto de la clase Cliente")
        if not isinstance(servicio, Servicio):
            raise TypeError("Se requiere un objeto de la clase Servicio")
        
        self._cliente = cliente      # Objeto Cliente
        self._servicio = servicio    # Objeto Servicio (o sus hijas)
        self._cupon = cupon          # Valor decimal (Ej: 0.1) o None
        self._estado = "Pendiente"   # Valor predeterminado

    def confirmar_reserva(self):
        # Manejo de excepciones para la lógica de negocio
        if self._servicio.get_horas() <= 0:
            raise ValueError("No se puede confirmar una reserva con 0 horas.")
        
        if self._estado == "Cancelada":
            raise RuntimeError("No se puede confirmar una reserva que ya fue cancelada.")
            
        self._estado = "Confirmada"

    def cancelar_reserva(self):
        self._estado = "Cancelada"

    def mostrar_detalle(self):
        # Extraemos la información usando los getters de las otras clases
        nombre_cliente = self._cliente.get_nombre()
        email_cliente = self._cliente.get_email()
        
        nombre_serv = self._servicio.get_nombre()
        desc_serv = self._servicio.descripcion()
        horas = self._servicio.get_horas()
        
        # Determinamos qué mostrar respecto al cupón
        info_cupon = "No aplicado"
        if self._cupon is not None:
            info_cupon = f"Aplicado ({int(self._cupon * 100)}%)"
        
        # Polimorfismo: el cálculo depende de la lógica de las hijas
        # Pasamos el parámetro opcional 'cupon' que recibimos en el constructor
        total = self._servicio.calcular_costo(cupon=self._cupon) #Pasamos el parametro opcional obtenido en el main y se calcula a traves de servicio
        
        return (
            f"\n=========================================="
            f"\n          RESUMEN DE LA RESERVA           "
            f"\n=========================================="
            f"\nCLIENTE: {nombre_cliente}"
            f"\nEMAIL: {email_cliente}"
            f"\n------------------------------------------"
            f"\nSERVICIO: {nombre_serv}"
            f"\n{desc_serv}" # La descripción ya trae los saltos de línea de la hija
            f"\nDURACIÓN: {horas} horas"
            f"\nCUPÓN: {info_cupon}"
            f"\n------------------------------------------"
            f"\nESTADO: {self._estado}"
            f"\nTOTAL A PAGAR (IVA Inc): ${total:,}"
            f"\n==========================================\n"
        )