# Sistema Integral de Gestión de Clientes, Servicios y Reservas

Proyecto desarrollado en Python para la empresa ficticia Software FJ, enfocado en la aplicación de Programación Orientada a Objetos (POO) y manejo avanzado de excepciones.

El sistema permite gestionar clientes, servicios y reservas sin utilizar bases de datos, implementando almacenamiento mediante objetos, listas y registro de eventos en archivos de logs.

## Características principales

- Gestión de clientes.
- Implementación de clases abstractas y herencia.
- Servicios especializados:
  - Reserva de salas
  - Alquiler de equipos (Tablets y portatiles)
  - Asesorías 
- Manejo de reservas, confirmaciones y cancelaciones.
- Polimorfismo y encapsulación.
- Manejo avanzado de excepciones personalizadas.
- Registro de errores y eventos en archivos de logs.
- Simulación de operaciones válidas e inválidas garantizando la estabilidad del sistema.

## Tecnologías utilizadas

- Python
- Git
- GitHub

## Estructura del proyecto

```text
/PROYECTOFJ
│
├── models/
│   ├── cliente.py
│   ├── reserva.py
│   └── servicio.py
│
├── services/
│   ├── alquiler_equipo.py
│   ├── asesoria.py
│   └── reserva_sala.py
│
├── utils/
│   └── logger.py
│
├── .gitignore
├── logs.txt
├── main.py
└── README.md
```

### Descripción de módulos

- `cliente.py` → Gestiona la información y validación de clientes.
- `reserva.py` → Administra reservas, confirmaciones y cancelaciones.
- `servicio.py` → Clase abstracta base para los servicios del sistema.
- `alquiler_equipo.py` → Implementa el servicio de alquiler de equipos.
- `asesoria.py` → Implementa asesorías.
- `reserva_sala.py` → Gestiona reservas de salas.
- `logger.py` → Registra eventos y excepciones en el archivo de logs.
- `logs.txt` → Almacena errores y eventos relevantes del sistema.
- `.gitignore` → Excluye archivos temporales y compilados del control de versiones.
- `main.py` → Punto principal de ejecución y simulación del sistema.


## Ejecución

Para ejecutar el sistema:

```bash
python main.py
```
## Integrantes

- Yudy Maritza Lavado Cañón
- Wilmer Danilo Ordoñez Galindo
- Maicol Yesid Rodriguez Beltrán
- Maryuri Alexandra Reyes Sanabria