# Elias Amaru Carreño Arriagada 22.382.218-5
# Benedick Anthony Mamani Mamani 27.608.499-2
# INGRESAR SUS NOMBRES COMPLETOS Y SUS RUTS AQUI PORFAVOR.

plan_impresion = []
PRECIO_REVISTA = 3820
MAX_IMPRESIONES = 2300

def interfaz_menu():
    print("\nMENÚ\n")
    print("""SISTEMA DE PLANIFICACIÓN DE IMPRESIÓN DE REVISTAS ESPECIALIZADAS\n
1. Generar plan de impresión
2. Ingresar cantidad de impresiones por revista especializada y día
3. Visualizar el ingreso total de una revista especializada específica
4. Visualizar el ingreso total de todas las revistas especializadas en un día específico
5. Salir del programa\n""")

def generar_impresion():
    print("\nGenerar plan de impresión\n")
    num_revistas = int(input("Ingrese número de tipos de revistas especializadas: "))
    num_dias = int(input("Ingrese número de días de impresión: "))
    for i in range(num_revistas):
        plan_impresion.append([0]*num_dias)
    print("\nPlan de impresión inicial:")
    mostrar_plan_impresion()

def ingresar_impresiones():
    for i in range(len(plan_impresion)):
        print(f"\nRevista {i + 1}")
        for j in range(len(plan_impresion[i])):
            while True:
                cantidad = int(input(f"Ingrese cantidad de revistas a imprimir en el día {j + 1}: "))
                if cantidad < 0:
                    print("Ingresaste un valor negativo, intente otra vez")
                elif cantidad > MAX_IMPRESIONES:
                    print(f"Superaste el limite de las impreciones {MAX_IMPRESIONES}, intenta otra vez")
                else:
                    plan_impresion[i][j] = cantidad
                    break
    mostrar_plan_impresion()

def mostrar_plan_impresion():
    print("\nPlan de impresión:")
    print("*" * 50)
    print("      Dia: ", end="")
    for dia in range(1, len(plan_impresion[0]) + 1):
        print(f"{dia:^8}", end="")
    for i, revista in enumerate(plan_impresion, 1):
        print(f"\nRevista {i}: ", end="")
        for cantidad in revista:
            print(f"{cantidad:^8}", end="")
    print("\n" + "*" * 50)

while True:
    interfaz_menu()
    opcion = int(input("Seleccione su opción: "))

    if opcion == 1:
        generar_impresion()
    elif opcion == 2:
        ingresar_impresiones()
    elif opcion == 3:
        pass
    elif opcion == 4:
        pass
    elif opcion == 5:
        break
    else:
        print("La Opcion es Invalida, intentelo denuevo.")