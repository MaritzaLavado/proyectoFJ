import re
import logging

# Configuración básica del logger
logging.basicConfig(
    filename="logger.txt",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Excepción personalizada
class ClienteError(Exception):
    pass

class Cliente:
    def __init__(self, nombre="", email=""):
        try:
            self.set_nombre(nombre)
            self.set_email(email)
        except ClienteError as e:
            logging.error(f"Error al crear cliente: {e}")
            raise

    # Getter y Setter con validaciones
    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        if not nombre or not nombre.strip():
            raise ClienteError("El nombre no puede estar vacío.")
        if len(nombre) < 3:
            raise ClienteError("El nombre debe tener al menos 3 caracteres.")
        self._nombre = nombre.strip().title()

    def get_email(self):
        return self._email

    def set_email(self, email):
        patron = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if not re.match(patron, email):
            raise ClienteError("Formato de correo electrónico inválido.")
        self._email = email.lower()

    def __str__(self):
        return f"Cliente: {self._nombre}, Email: {self._email}"
