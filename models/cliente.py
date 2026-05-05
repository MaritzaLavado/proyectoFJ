class Cliente:
    def __init__(self, nombre="", email=""):
        self._nombre = nombre
        self._email = email

    def get_nombre(self):
        return self._nombre

    def get_email(self):
        return self._email

    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_email(self, email):
        self._email = email