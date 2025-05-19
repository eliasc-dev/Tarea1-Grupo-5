# Elias Amaru Carreño Arriagada 22.382.218-5
# Joaquin Alejandro Alarcon Jara 22.241.272-2
# Benedick Anthony Mamani Mamani 27.608.499-2

plan_impresion = []
PRECIO_REVISTA = 3820
MAX_IMPRESIONES = 2300

def interfaz_menu():
    print("""\nSISTEMA DE PLANIFICACIÓN DE IMPRESIÓN DE REVISTAS ESPECIALIZADAS\n
1. Generar plan de impresión
2. Ingresar cantidad de impresiones por revista especializada y día
3. Visualizar el ingreso total de una revista especializada específica
4. Visualizar el ingreso total de todas las revistas especializadas en un día específico
5. Salir del programa\n""")

def generar_impresion():
    print("\nGenerar plan de impresión\n")
    while True:
        try:
            num_revistas = int(input("Ingrese número de tipos de revistas especializadas: "))
            num_dias = int(input("Ingrese número de días de impresión: "))
            if num_revistas > 0 and num_dias > 0:
                for i in range(num_revistas):
                    plan_impresion.append([0]*num_dias)
                mostrar_plan_impresion()
                break
            else:
                print("\nDebes ingresar un numero positivo y mayor a 0\n")
        except ValueError:
            print("\nDebes ingresar un valor valido\n")

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

def ingresar_impresiones():
    print("\nIngresar cantidad de impresiones por revista especializada y día\n")
    if not plan_impresion:
        print("\nPrimero debes generar el plan de imprecion")
        return
    while True:
        try:
            for i in range(len(plan_impresion)):
                print(f"\nRevista {i + 1}")
                for j in range(len(plan_impresion[i])):
                    while True:
                        cantidad = int(input(f"Ingrese cantidad de revistas a imprimir en el día {j + 1}: "))
                        if cantidad <= 0:
                            print("\nIngresaste un valor negativo o 0, intente otra vez\n")
                        elif cantidad > MAX_IMPRESIONES:
                            print(f"\nSuperaste el limite de las impreciones {MAX_IMPRESIONES}, intenta otra vez\n")
                        else:
                            plan_impresion[i][j] = cantidad
                            break
            mostrar_plan_impresion()
            break
        except ValueError:
            print("\nDebes ingresar un valor valido")

def ingreso_total_revista_especifica():
    print("\nVisualizar el ingreso total de una revista especializada específica")
    if not plan_impresion:
        print("Primero debe generar el plan de impresión (opción 1).")
        return
    while True:
        try:
            num_revista = int(input(f"\nIngrese la revista a calcular y visualizar (1 a {len(plan_impresion)}): "))
            if 1 <= num_revista <= len(plan_impresion):
                total_ingresos = 0
                print()
                for dia, impresiones in enumerate(plan_impresion[num_revista - 1], start=1):
                    ingresos_dia = impresiones * PRECIO_REVISTA
                    total_ingresos += ingresos_dia
                    print(f"Revista {num_revista}, día {dia}: {impresiones} impresiones para un total de ingresos $: {ingresos_dia:,}")
                print(f"\nTotal ingresos de la Revista {num_revista} $: {total_ingresos:,}")
                break
            else:
                print("\nNúmero de revista fuera de rango.")
        except ValueError:
            print("\nDebe ingresar un número válido.")

def ingreso_total_por_dia():
    print("\nVisualizar el ingreso total de todas las revistas especializadas en un día específico")
    if not plan_impresion:
        print("Primero debe generar el plan de impresión (opción 1).")
        return
    while True:
        try:
            num_dia = int(input(f"\nIngrese el día a calcular y visualizar (1 a {len(plan_impresion[0])}): "))
            if 1 <= num_dia <= len(plan_impresion[0]):
                total_ingresos = 0
                for i, revista in enumerate(plan_impresion, start=1):
                    impresiones = revista[num_dia - 1]
                    ingreso = impresiones * PRECIO_REVISTA
                    total_ingresos += ingreso
                    print(f"Revista {i}, día {num_dia}: {impresiones} impresiones para un total de ingresos $: {ingreso:,}")
                print(f"\nTotal ingresos del día {num_dia} $: {total_ingresos:,}")
                break
            else:
                print("\nNúmero de día fuera de rango.")
        except ValueError:
            print("\nDebe ingresar un número válido.")

while True:
    try:
        interfaz_menu()
        opcion = int(input("Seleccione su opción: "))
        
        if opcion == 1:
            generar_impresion()
        elif opcion == 2:
            ingresar_impresiones()
        elif opcion == 3:
            ingreso_total_revista_especifica()
        elif opcion == 4:
            ingreso_total_por_dia()
        elif opcion == 5:
            print("Fin de la ejecución del programa")
            break
        else:
            print("\nLa Opcion es Invalida, intentelo denuevo.")
    except ValueError:
        print("\nDebes ingresas un numero valido.")