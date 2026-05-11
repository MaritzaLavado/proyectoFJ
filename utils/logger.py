import logging

# CONFIGURACIÓN DEL ARCHIVO DE LOGS

logging.basicConfig(
    filename="logs.txt",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

# FUNCIÓN PARA REGISTRAR ERRORES

def log_error(error):

    logging.error(error)

# FUNCIÓN PARA REGISTRAR EVENTOS IMPORTANTES

def log_evento(evento):

    with open("logs.txt", "a", encoding="utf-8") as archivo:

        archivo.write(f"EVENTO: {evento}\n")