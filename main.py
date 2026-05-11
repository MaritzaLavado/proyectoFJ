# main.py - Punto de entrada del software
#importamos las clases necesarias para el funcionamiento del software
from models.cliente import Cliente
from models.reserva import Reserva

#Ls de services en teorian son las hijas aun que en models se ayuden mutuamente
from services.reserva_sala import ReservaSala
from services.alquiler_equipo import AlquilerEquipo
from services.asesoria import Asesoria

#Asi podemos usar los loggs del archivo logger.py para registrar eventos y errores en el sistema
#Aun asi no estoy muy seguor de agregar exepciones.py ya que tendria que renombrar todsa las excepciones que hayan hecho mis compañeros una por una....
#Ese archivo basicamente daria orden mas no funcionalidad ya que solo es como un rename para cad tipo de error
#CAso tal lo podemos agregar peeeero sin el el programa funciona ya que la cantidad de errores que manejamos se pueden dividir facilmente en:
#-Errores de validación de datos (como el caso del cliente o las horas)
#-Errores de operación (como el caso de confirmar o cancelar una reserva)
#-Errores de sistema (como el caso de leer o escribir en el archivo de logs)
#-Errores X que no esperemos pero al menos en pruebas no encontre no se jaja
from utils.logger import log_error, log_evento


# =============================================================
# SIMULACIÓN AUTOMÁTICA
# =============================================================
#Con el fin de que el tutor pueda ver los 10 loggs sin necesidad de escribilos uno por uno si no quiere

def ejecutar_simulacion():

    print("\n" + "=" * 60)#decoración del menú
    print("      INICIANDO SIMULACIÓN AUTOMÁTICA")
    print("=" * 60)

    #Lista de puebas con datos estandarizados para generar logs de éxito y error
    pruebas = [

        ("Juan Perez", "juan@gmail.com", "asesoria", 2),
        ("Maria Lopez", "maria@gmail.com", "sala", 4),
        ("Carlos Ruiz", "carlos@gmail.com", "equipo", 3),

        ("Al", "correo@gmail.com", "asesoria", 2),
        ("Pedro", "pedrogmail.com", "sala", 4),
        ("Laura", "laura@gmail.com", "sala", 1),
        ("Camilo", "camilo@gmail.com", "equipo", -5),

        ("Sofia", "sofia@gmail.com", "asesoria", 5),
        ("Miguel", "miguel@gmail.com", "sala", 6),

        ("Ana", "ana@gmail.com", "equipo", 0)

    ]

    #Se recorre cada prueba segun el indice
    for i, prueba in enumerate(pruebas, start=1):

        print("\n" + "-" * 60)
        print(f"PRUEBA #{i}")
        print("-" * 60)

        try:

            #Desempaquetamos los datos de las pruebas
            nombre, email, tipo, horas = prueba

            #se valida segun el caso del cliente y el servicio, si hay un error se captura en el except y se genera un log de error, si no, se genera un log de éxito   

            cliente = Cliente(nombre, email)

            if tipo == "asesoria":

                servicio = Asesoria(horas)

            elif tipo == "sala":

                servicio = ReservaSala(horas)

            else:

                servicio = AlquilerEquipo("tablet", horas)

            reserva = Reserva(cliente, servicio)

            reserva.confirmar_reserva()

            print(">> OPERACIÓN EXITOSA")

            print(reserva.mostrar_detalle())

            log_evento(
                f"Simulación exitosa para {cliente.get_nombre()}"
            )

        except Exception as e:

            print(f">> ERROR DETECTADO: {e}")

            log_error(str(e))

    print("\nSIMULACIÓN FINALIZADA.\n")


# =============================================================
# FUNCIÓN PRINCIPAL
# =============================================================
#Funcion para ejecutar el codigo
def main():

    clientes = [] #Lista para ver clientes registrados


    # =============================================================
    # REGISTRO INICIAL OBLIGATORIO
    # =============================================================

    #ciclo para regitrar un cliente valido
    while True:

        try:

            print("\n" + "=" * 60)
            print("           REGISTRO DE CLIENTE")
            print("=" * 60)

            nombre = input("\nIngrese su nombre: ")
            email = input("Ingrese su correo: ")

            #Se valida creando el objeto y llamando a la validación de cliente.py
            cliente_actual = Cliente(nombre, email)

            #Se agrega el cliente a la lista del main
            clientes.append(cliente_actual)

            print("\n>> Registro exitoso.")

            log_evento(
                f"Cliente registrado: {cliente_actual.get_nombre()}"
            )

            break

        #preprara logg de error
        except Exception as e:

            print(f"\n[ERROR]: {e}")

            log_error(str(e))

    # =============================================================
    # MENÚ PRINCIPAL
    # =============================================================

    #Ciclo del sistema principal
    while True:

        print("\n" + "=" * 60)
        print("        SOFTWARE FJ - MENÚ PRINCIPAL")
        print("=" * 60)

        print("1. Reservar sala")
        print("2. Alquiler de equipo")
        print("3. Asesoría")
        print("4. Clientes registrados")
        print("5. Ejecutar simulación automática")
        print("6. Ver logs")
        print("7. Cambiar de cliente")
        print("8. Salir")

        #Recibimos la opción del usuario
        opcion = input("\nSeleccione una opción: ")

        # =====================================================
        # RESERVA DE SALA
        # =====================================================

        #Validamos una por una las opcines psibles a elejit
        if opcion == "1":

            try:

                cliente = cliente_actual

                horas = int(
                    input("\nIngrese cantidad de horas: ")
                )

                servicio = ReservaSala(horas)

                # =====================================================
                # CUPÓN
                # =====================================================

                #Este tipo de logica se desrrolla en función a los forms de mis compañeros asi quesolo es cuestion de validadr y usar lo .lower
                cupon = None

                tiene_cupon = input(
                    "\n¿Tiene cupón de descuento? (si/no): "
                ).strip().lower()

                if tiene_cupon == "si":

                    try:
                        porcentaje = float(
                        input("Ingrese porcentaje del cupón: ")
                        )

                        if porcentaje < 0 or porcentaje > 100:
                            raise ValueError(
                                "El porcentaje debe estar entre 0 y 100."
                        )

                        cupon = porcentaje / 100

        
                        log_evento(f"Cupón aplicado: {porcentaje}%")

                        print(f">> Cupón del {porcentaje}% aplicado correctamente.")

                    except ValueError as e:
                        log_error(f"Error en cupón: {e}")
                        raise

                # =====================================================
                # CREAR RESERVA
                # =====================================================

                reserva = Reserva(cliente, servicio, cupon)

                # =====================================================
                # CONFIRMAR
                # =====================================================

                decision = input(
                    "\n¿Desea confirmar la reserva? (si/no): "
                ).strip().lower()

                if decision == "si":

                    reserva.confirmar_reserva()

                    print("\n>> Reserva confirmada.")

                    log_evento(
                        f"Reserva de sala confirmada para {cliente.get_nombre()}"
                    )

                else:

                    reserva.cancelar_reserva()

                    print("\n>> Reserva cancelada.")

                    log_evento(
                        f"Reserva de sala cancelada para {cliente.get_nombre()}"
                    )

             

                print(reserva.mostrar_detalle())

            except Exception as e:

                print(f"\n[ERROR]: {e}")

                log_error(str(e))

        # =====================================================
        # ALQUILER DE EQUIPO
        # =====================================================

        elif opcion == "2":

            try:

                cliente = cliente_actual

                tipo = input(
                    "\nIngrese tipo de equipo (tablet/portatil): "
                )

                horas = int(
                    input("Ingrese cantidad de horas: ")
                )

                servicio = AlquilerEquipo(tipo, horas)

                # =====================================================
                # CUPÓN
                # =====================================================

                cupon = None

                tiene_cupon = input(
                    "\n¿Tiene cupón de descuento? (si/no): "
                ).strip().lower()

                if tiene_cupon == "si":

                    porcentaje = float(
                        input("Ingrese porcentaje del cupón: ")
                    )

                    if porcentaje < 0 or porcentaje > 100:

                        raise ValueError(
                            "El porcentaje debe estar entre 0 y 100."
                        )

                    cupon = porcentaje / 100

                # =====================================================
                # CREAR RESERVA
                # =====================================================

                reserva = Reserva(cliente, servicio, cupon)

                # =====================================================
                # CONFIRMAR
                # =====================================================

                decision = input(
                    "\n¿Desea confirmar la reserva? (si/no): "
                ).strip().lower()

                if decision == "si":

                    reserva.confirmar_reserva()

                    print("\n>> Reserva confirmada.")

                    log_evento(
                        f"Alquiler confirmado para {cliente.get_nombre()}"
                    )

                else:

                    reserva.cancelar_reserva()

                    print("\n>> Reserva cancelada.")

                    log_evento(
                        f"Alquiler cancelado para {cliente.get_nombre()}"
                    )

               

                print(reserva.mostrar_detalle())

            except Exception as e:

                print(f"\n[ERROR]: {e}")

                log_error(str(e))

        # =====================================================
        # ASESORÍA
        # =====================================================

        elif opcion == "3":

            try:

                cliente = cliente_actual

                horas = int(
                    input("\nIngrese cantidad de horas: ")
                )

                servicio = Asesoria(horas)

                # =====================================================
                # CUPÓN
                # =====================================================

                cupon = None

                tiene_cupon = input(
                    "\n¿Tiene cupón de descuento? (si/no): "
                ).strip().lower()

                if tiene_cupon == "si":

                    porcentaje = float(
                        input("Ingrese porcentaje del cupón: ")
                    )

                    if porcentaje < 0 or porcentaje > 100:

                        raise ValueError(
                            "El porcentaje debe estar entre 0 y 100."
                        )

                    cupon = porcentaje / 100

                # =====================================================
                # CREAR RESERVA
                # =====================================================

                reserva = Reserva(cliente, servicio, cupon)

                # =====================================================
                # CONFIRMAR
                # =====================================================

                decision = input(
                    "\n¿Desea confirmar la reserva? (si/no): "
                ).strip().lower()

                if decision == "si":

                    reserva.confirmar_reserva()

                    print("\n>> Reserva confirmada.")

                    log_evento(
                        f"Asesoría confirmada para {cliente.get_nombre()}"
                    )

                else:

                    reserva.cancelar_reserva()

                    print("\n>> Reserva cancelada.")

                    log_evento(
                        f"Asesoría cancelada para {cliente.get_nombre()}"
                    )



                print(reserva.mostrar_detalle())

            except Exception as e:

                print(f"\n[ERROR]: {e}")

                log_error(str(e))

        # =====================================================
        # CLIENTES REGISTRADOS
        # =====================================================

        elif opcion == "4":

            if len(clientes) == 0:

                print("\nNo hay clientes registrados.")

            else:

                print("\n" + "=" * 60)
                print("           CLIENTES REGISTRADOS")
                print("=" * 60)

                for i, cliente in enumerate(clientes, start=1):

                    print(f"{i}. {cliente}")

        # =====================================================
        # SIMULACIÓN
        # =====================================================

        elif opcion == "5":

            #Aca solo es necesario llamar a la función que hicimos al inicio del main

            ejecutar_simulacion()

        # =====================================================
        # VER LOGS
        # =====================================================

        #Llamamos a el archivo para que se ejecute en consola tal y como se haria en un cmd o terminal de linux
        elif opcion == "6":

            archivo = None

            try:

                archivo = open("logs.txt", "r", encoding="utf-8")

                print(archivo.read())

            except FileNotFoundError:

                print("No existen logs.")

            finally:

               if archivo:
                archivo.close()

        # =====================================================
        # CAMBIAR CLIENTE
        # =====================================================

        elif opcion == "7":

            while True:

                try:

                    print("\n" + "=" * 60)
                    print("            CAMBIO DE CLIENTE")
                    print("=" * 60)

                    nombre = input("\nIngrese su nombre: ")
                    email = input("Ingrese su correo: ")

                    cliente_actual = Cliente(nombre, email)

                    clientes.append(cliente_actual)

                    print("\n>> Cliente cambiado correctamente.")

                    log_evento(
                        f"Cambio de cliente: {cliente_actual.get_nombre()}"
                    )

                    break

                except Exception as e:

                    print(f"\n[ERROR]: {e}")

                    log_error(str(e))

        # =====================================================
        # SALIR
        # =====================================================

        elif opcion == "8":

            print("\nSaliendo del sistema...")

            break

        # =====================================================
        # OPCIÓN INVÁLIDA
        # =====================================================

        else:

            print("\nOpción inválida.")


# =============================================================
# EJECUCIÓN PRINCIPAL
# =============================================================

if __name__ == "__main__":

    main()