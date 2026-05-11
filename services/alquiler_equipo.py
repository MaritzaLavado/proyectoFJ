from models.servicio import Servicio

class AlquilerEquipo(Servicio):

    def __init__(self, tipo_equipo="", horas=0):
        """
        Constructor de la clase.
        Dependiendo del tipo de equipo se asigna una tarifa diferente.
        """

        super().__init__(tipo_equipo)

        # Validación del tipo de equipo
        tipos_validos = ["tablet", "portatil"]

        if tipo_equipo.lower() not in tipos_validos:
            raise ValueError(
                "Tipo de equipo inválido. Solo se permite: Tablet o Portátil."
            )

        self.tipo_equipo = tipo_equipo.lower()

        # Tarifas por hora según el equipo
        if self.tipo_equipo == "tablet":
            self.tarifa_hora = 8000
        else:
            self.tarifa_hora = 15000

        # Validación de horas
        if horas <= 0:
            raise ValueError("La cantidad de horas debe ser mayor a cero.")

        self.horas = horas

    def descripcion(self):
        """
        Descripción personalizada del servicio
        """

        return (
            f"\nServicio de alquiler de {self.tipo_equipo.capitalize()}"
            f"\n Tarifa por hora: ${self.tarifa_hora}"
            f"\n Horas solicitadas: {self.horas}"
            "\n Equipos en excelente estado"
            "\n Soporte técnico incluido"
        )

    def calcular_costo(self, iva=0.19, cupon=None):
        """
        Calcula el costo total del alquiler.
        """

        # Cálculo base
        subtotal = self.tarifa_hora * self.horas

        # Aplicar IVA
        total = subtotal + (subtotal * iva)

        # Aplicar cupón si existe
        if cupon is not None:

            # Validación del cupón
            if cupon < 0 or cupon > 1:
                raise ValueError(
                    "El cupón debe estar entre 0 y 1."
                )

            total = total * (1 - cupon)

        return round(total)
