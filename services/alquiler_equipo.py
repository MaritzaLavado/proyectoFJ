from models.servicio import Servicio

class AlquilerEquipo(Servicio):

    def __init__(self, tipo_equipo="", horas=0):
        """
        Constructor de la clase.
        Dependiendo del tipo de equipo se asigna una tarifa diferente.
        """

        # CORRECCIÓN: validar horas antes de crear el servicio
        if horas <= 0:
            raise ValueError("La cantidad de horas debe ser mayor a cero.")

        # Validación del tipo de equipo
        tipos_validos = ["tablet", "portatil"]

        if tipo_equipo.lower() not in tipos_validos:
            raise ValueError(
                "Tipo de equipo inválido. Solo se permite: Tablet o Portátil."
            )

        # CORRECCIÓN: normalizar el nombre antes de usarlo
        tipo_equipo = tipo_equipo.lower()

        # CORRECCIÓN: definir tarifa antes de llamar al constructor padre
        if tipo_equipo == "tablet":
            tarifa = 8000
        else:
            tarifa = 15000

        # CORRECCIÓN: enviar correctamente nombre, tarifa y horas al padre
        super().__init__(tipo_equipo, tarifa, horas)

    def descripcion(self):
        """
        Descripción personalizada del servicio
        """

        return (
            # CORRECCIÓN: usar getters heredados en lugar de atributos inexistentes
            f"\nServicio de alquiler de {self.get_nombre().capitalize()}"
            f"\n Tarifa por hora: ${self.get_tarifa()}"
            f"\n Horas solicitadas: {self.get_horas()}"
            "\n Equipos en excelente estado"
            "\n Soporte técnico incluido"
        )

    def calcular_costo(self, iva=0.19, cupon=None):
        """
        Calcula el costo total del alquiler.
        """

        # Cálculo base
        subtotal = self.get_tarifa() * self.get_horas()

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
