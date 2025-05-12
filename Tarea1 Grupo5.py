# Elias Amaru Carreño Arriagada 22.382.218-5
# INGRESAR SUS NOMBRES COMPLETOS Y SUS RUTS AQUI PORFAVOR.
#

def interfaz_menu():
    print("""SISTEMA DE PLANIFICACIÓN DE IMPRESIÓN DE REVISTAS ESPECIALIZADAS\n
1. Generar plan de impresión
2. Ingresar cantidad de impresiones por revista especializada y día
3. Visualizar el ingreso total de una revista especializada específica
4. Visualizar el ingreso total de todas las revistas especializadas en un día específico
5. Salir del programa\n""")
# Utilizamos el comando "\n" para separar el texto y que sea más agradable a la vista del usuario.
# Interfaz del menu solicitado, trabajaremos todas las opciones con funciones que seran llamadas con  la variable "opcion".

def generar_impresion():
    print("Generar plan de impresión\n")
    num_revistas = int(input("Ingrese número de tipos de revistas especializadas: "))
    num_dias = int(input("Ingrese número de días de impresión: "))
    plan_impresion = []
    for i in range(num_revistas):
        # Cada fila es una revista y cada columna un dia.
        plan_impresion.append([0]*num_dias)
        # Esta linea de codigo crea una lista de "num_dias" elementos, y cada uno de esos elementos es el número 0.
        print("\nPlan de impresión inicial:")
    for fila in plan_impresion:
        print(fila)
    


while True:
    interfaz_menu()
    opcion = int(input("Seleccione su opción: "))

    if opcion == 1:
        generar_impresion()
    
    elif opcion == 2:
        #funcion2() PENDIENTE CREAR
        pass
    
    elif opcion == 3:
        #funcion3() PENDIENTE CREAR
        pass
    
    elif opcion == 4:
        #funcion4() PENDIENTE CREAR
        pass
    
    elif opcion == 5:
        break
    
    else:
        print("La Opcion es Invalida, intentelo denuevo.")

    

