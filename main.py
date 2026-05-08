from models.cliente import Cliente
from models.reserva import Reserva

from services.reserva_sala import ReservaSala
from services.alquiler_equipo import AlquilerEquipo
from services.asesoria import Asesoria
#                                     ------------------------------------------------------------------------------------
# from utils.logger import log_error  #Comente lo que daba error, para fines de buenas practicas respecto al repositorio
#                                     ------------------------------------------------------------------------------------
# def capturar_datos_servicio():
#     nombre = input("Ingrese el nombre del servicio: ")
#     horas = int(input("Ingrese la cantidad de horas: "))
#     return nombre, tarifa, horas

#------------------------------------------------------------------------------------------------------
# HOLA MAICOL, ESO DE ARRIBA ⬆ es un ejemplo de como capturar datos (Para servicio en este caso) Hay qye agregar logica de capturar todos los datos teniendo en cuenta la guia de abajo
#------------------------------------------------------------------------------------------------------

# def ejecutar_sistema():

    
#     try:
#         # Este es un ejemplo donde predetermino la clasehija asesoria y pido las horas
#         print("\nServicio disponible: Asesoría")
#         horas_input = input("¿Cuántas horas de asesoría necesita? (Ej: 2): ")
        
#         # Validación de tipo de dato
#         if not horas_input.isdigit():
#             raise ValueError("La cantidad de horas debe ser un número entero.")
        
#         horas = int(horas_input)

#         # AQUI SE CREA EL OBJETO
#         mi_servicio = Asesoria(horas)

#         # AQUI MUESTRO LA DESCRIPCION DEL SERVICIO 
#         print("\n" + "="*70)  # ESTE Y EL DE ABAJO PRODUCE COMO UN MARCO PARA DIFERENCIAR LA DESCRIPCION
#         print(mi_servicio.descripcion())
#         print("="*70)  #ESTE ES EL DE ABAJO

#         #ESTO ES LO QUE MAS IMPORTA Y LA RAZON PRINCIPAL DE PONERLE ESTA GUIA
#         #PARA QUE USE LA LÓGICA DEL CUPON PARA CUMPLIR CON SOBRECARGA ES PARA TODOS LOS SERVICIOS

#         #LA LOGICA DEL CUPON QUE DEBE USAR 
#         tiene_cupon = input("\n¿Cuenta con un cupón de descuento? (si/no): ").strip().lower() #PRIMERO VALIDAR SI TIENE O NO CUPON
          #cupon_decimal=None

#         if tiene_cupon == "si":  #SI ESCRIBIO SI, DEBE INGRESAR EL PORCENTAJE DE SU CUPON
#             valor_cupon = float(input("Ingrese el porcentaje del cupón (Ej: 10 para el 10%): "))
            
# #             # Validación robusta solicitada
#             if valor_cupon < 0 or valor_cupon > 100:
#                 raise ValueError("El cupón debe estar entre 0 y 100.")
            
#             cupon_decimal = valor_cupon / 100
#             print(f">> Cupón del {round(valor_cupon)}% aplicado con exito.")

#         # Integración con la Clase Reserva
#         # Pasamos el cliente, el servicio y el cupón ya validado
#         mi_reserva = Reserva(mi_cliente, mi_servicio, cupon=cupon_decimal)
        
#         # Procesamiento
#         mi_reserva.confirmar_reserva() # Valida excepciones como horas <= 0

#          Aquí es donde se toma la decisión:
#          confirmar = input("¿Desea confirmar la reserva ahora? (si/no): ").lower()

#          if confirmar == "si":
#              mi_reserva.confirmar_reserva() # <--- Aquí el main le da la orden a la Reserva
#              print("El sistema ha marcado la reserva como CONFIRMADA.")
#          else:
#              mi_reserva.cancelar_reserva()  # <--- Aquí el main le dice que la cancele
#              print("La reserva ha sido CANCELADA por el usuario.")
        
#         # 5. Salida de datos final
#         print(mi_reserva.mostrar_detalle())

#         

#     #VALIDACIONES DE EJEMPLO
#     except ValueError as e:
#         print(f"\n[ERROR DE VALIDACIÓN]: {e}")
#     except Exception as e:
#         print(f"\n[ERROR INESPERADO]: {e}")

#------------------------------------------------------------------------------------------------
# ESTA ⬆ ES LA GUIA BASE PARA QUE PUEDA EJECUTAR LOS SERVICIOS CON LOGICA DE CUPÓN Y SERVICIOS
#------------------------------------------------------------------------------------------------

def main():
    clientes = []
    servicios = []
    reservas = []

    try:
        # Crear objetos base (sin lógica aún)
        cliente = Cliente()
        servicio1 = ReservaSala()
        servicio2 = AlquilerEquipo()
        servicio3 = Asesoria()

        reserva = Reserva(cliente, servicio1, 1)

        # Guardar en listas
        clientes.append(cliente)
        servicios.extend([servicio1, servicio2, servicio3])
        reservas.append(reserva)

        # Operaciones básicas
        reserva.confirmar()

    except Exception as e:
        # log_error(str(e))   #Comente lo que daba error, para fines de buenas practicas respecto al repositorio
        pass


if __name__ == "__main__":
    main()