#**********************************DICCIONARIO PARA GUARDAR PROCESOS******************************************
procesos_guardados = []  # Lista para almacenar todos los procesos cargados


#****************************************Función para calcular glucosa***********************************

#prueba
#**************************Función para calcular horas de trabajo por operario***************************

#********************************Función para cargar datos:**********************************************

#************************FUNCIÓN PARA CALCULAR VOLUMEN DE MEDIO DE EXPANCIÓN*****************************
#prueba?
def cargar_datos_proceso():
   #Se crea un diccionario que será completado con las características de la molécula.
    proceso = []
    # Ingresar el nombre de la molécula
    nombre_molecula = input("Ingrese el nombre de la molécula: ")
    proceso.append([nombre_molecula]) 

    etapas = []
    for i in range(5):
        duracion = int(input(f"Ingrese la duración en días de la etapa {i + 1}: "))
        etapas.append(duracion)
    
    solucion_extra = input("¿Se debe agregar solución extra en la quinta etapa? (sí/no): ").strip().lower()
    if solucion_extra == "sí":
        dias_extra = int(input("Ingrese la cantidad de días adicionales para la solución extra: "))
        etapas[4] += dias_extra
    # Agregamos las duraciones de las etapas como una fila en la matriz
    proceso.append(etapas)
    
    # Retornar el proceso cargado
    return proceso

#**************FUNCIÓN PARA MOSTRAR LAS CARACTERÍSTICAS DEL PROCESO********************************
def mostrar_proceso(proceso):
    """Función para mostrar un proceso individual"""
    print(f"\nNombre de la molécula: {proceso[0][0]}")
    print("Duraciones de las etapas:")
    for i, duracion in enumerate(proceso[1]):
        print(f"Etapa {i + 1}: {duracion} días")

#**************FUNCIÓN PARA MOSTRAR TODOS LOS PROCESOS*********************************************
def mostrar_todos_los_procesos():
    """Función para mostrar todos los procesos guardados"""
    if not procesos_guardados:
        print("No hay procesos almacenados.")
    else:
        for i, proceso in enumerate(procesos_guardados):
            print(f"\nProceso {i + 1}:")
            mostrar_proceso(proceso)

#******************FUNCIÓN PARA CALCULAR COSTOS: EN FUNCIÓN DE LA DURACIÓN DEL PROCESO*****************
def calcular_costos():
    """Función para calcular costos (se puede expandir más adelante)"""
    if not procesos_guardados:
        print("No hay procesos guardados para calcular costos.")
        return
    
    for i, proceso in enumerate(procesos_guardados):
        total_dias = sum(proceso[1])  # Sumamos las duraciones de las etapas
        costo_total = total_dias * 100  # Ejemplo: supongamos que cada día cuesta $100 (A DEFINÍR)
        print(f"El costo total del proceso {proceso[0][0]} es: ${costo_total}")
    
#***********************************MENÚ PRINCIPAL******************************************
def menu_principal():
    while True:
        print("\nBienvenido al menú principal, seleccione una opción para continuar\n")
        print("1. Cargar nuevo proceso")
        print("2. Ver procesos guardados")
        print("3. Calcular costos del proceso")
        print("4. Salir")
        
        opcion = int(input("Ingrese el número de la opción seleccionada: "))
        
        if opcion == 1:
            print("SE ENCUENTRA EN LA SECCIÓN DE CARGA DE DATOS PARA GENERAR UN NUEVO PROCESO")
            proceso = cargar_datos_proceso()
            procesos_guardados.append(proceso)  # Guardamos el proceso en la lista global
            print(f"Proceso para {proceso[0][0]} guardado exitosamente.\n")
        
        elif opcion == 2:
            print("Los procesos almacenados son:")
            mostrar_todos_los_procesos()
        
        elif opcion == 3:
            print("Calculando costos de los procesos...")
            calcular_costos()
        
        elif opcion == 4:
            print("Saliendo del menú principal :)...")
            break
        
        else:
            print("Opción no válida. Por favor, intente nuevamente.")

# Ejecución del menú
menu_principal()