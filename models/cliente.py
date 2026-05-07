import re          # Librería para trabajar con expresiones regulares (validar email)
import logging     # Librería para registrar errores en un archivo de logs

# Excepción personalizada para manejar errores específicos de Cliente
class ClienteError(Exception):
    pass

class Cliente:
    def __init__(self, nombre="", email=""):
        # Constructor: inicializa el objeto Cliente con nombre y email
        try:
            self.set_nombre(nombre)   # Valida y asigna el nombre
            self.set_email(email)     # Valida y asigna el email
        except ClienteError as e:
            # Si ocurre un error, se registra en el log y se relanza la excepción
            logging.error(f"Error al crear cliente: {e}")
            raise

    # Getter para obtener el nombre del cliente
    def get_nombre(self):
        return self.__nombre

    # Setter para asignar el nombre con validaciones
    def set_nombre(self, nombre):
        if not nombre or not nombre.strip():
            # Validación: el nombre no puede estar vacío
            raise ClienteError("El nombre no puede estar vacío.")
        if len(nombre) < 3:
            # Validación: el nombre debe tener mínimo 3 caracteres
            raise ClienteError("El nombre debe tener al menos 3 caracteres.")
        # Se guarda el nombre con formato limpio (sin espacios y con mayúscula inicial)
        self.__nombre = nombre.strip().title()

    # Getter para obtener el email del cliente
    def get_email(self):
        return self.__email

    # Setter para asignar el email con validación de formato
    def set_email(self, email):
        patron = r"^[\w\.-]+@[\w\.-]+\.\w+$"   # Expresión regular para validar email
        if not re.match(patron, email):
            # Validación: si no cumple el patrón, se lanza excepción
            raise ClienteError("Formato de correo electrónico inválido.")
        # Se guarda el email en minúsculas
        self.__email = email.lower()

    # Método especial para mostrar el cliente en texto legible
    def __str__(self):
        return f"Cliente: {self.__nombre}, Email: {self.__email}"

