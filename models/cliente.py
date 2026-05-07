import re
from utils.logger import logger   # Importa el logger global

# Excepción personalizada para manejar errores específicos de Cliente
class ClienteError(Exception):
    pass

class Cliente:
    def __init__(self, nombre="", email=""):
        try:
            self.set_nombre(nombre)  # Valida y asigna el nombre
            self.set_email(email)    # Valida y asigna el email
        except ClienteError as e:
            # Usa el logger global de utils
            logger.error(f"Error al crear cliente: {e}")
            raise

    # Getter para obtener el nombre del cliente
    def get_nombre(self):
        return self._nombre

    # Setter para asignar el nombre con validaciones
    def set_nombre(self, nombre):
        if not nombre or not nombre.strip():
            raise ClienteError("El nombre no puede estar vacío.")
        if len(nombre.strip()) < 3:
            raise ClienteError("El nombre debe tener al menos 3 caracteres.")
        self._nombre = nombre.strip().title()

    # Getter para obtener el email del cliente
    def get_email(self):
        return self._email

    # Setter para asignar el email con validación de formato
    def set_email(self, email):
        patron = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if not re.match(patron, email):
            raise ClienteError("Formato de correo electrónico inválido.")
        self._email = email.strip().lower()

    # Método especial para mostrar el cliente en texto legible
    def __str__(self):
        return f"Cliente: {self._nombre}, Email: {self._email}"


