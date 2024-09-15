
#######################################################################################
#Con la combinación de las siguientes funciones se establece el volúmen final a utilizar de medio de expansión, de acuerdo a los requerimientos del cliente.
def listaVCDtarget(cantPasajes):
     #Generar una lista en la que se almacene la VCD que se desea alcanzar en cada pasaje.
    VCDstarget=[]
    for i in range(cantPasajes):
        VCDtargetIngreso=input(f"Ingrese el valor de VCD target para el pasaje {i+1}: ").replace(',', '.')
        VCDtarget=float(VCDtargetIngreso)
    return VCDstarget

def calcularVolFinalPasajes(VCDi,VCDstarget,cantPasajes,volInicial):
    #Generar una lista en la que se almacene el volumen final de cada pasaje.
    listavolFinalPasajes=[]
    for i in range(cantPasajes):
        volFinalPasaje=(VCDi*volInicial)/VCDstarget[i]
        listavolFinalPasajes.append(volFinalPasaje)
        VCDi=VCDstarget[i]
        volInicial=volFinalPasaje 
    return listavolFinalPasajes

def calcularMedioExp(listavolFinalPasajes):
    #Sumar los pesos de los volumenes finales de cada pasaje para calcular el volumen final de medio necesario.
    volMedioExp=sum(listavolFinalPasajes)
    return volMedioExp

#######################################################################################
def MatrizComoTabla(matriz,ancho_columna):
    #Imprime una matriz en forma de tabla. Ingresos: una matriz y el ancho de la columna de la tabla(máximo de caracteres para que se ajusten las columnas)
    for fila in matriz:
        for elemento in fila:
            print(f"{elemento:>{ancho_columna}}",end=" | ")
        print()
#######################################################################################
def agregar_solucion_adicional():
    # Preguntar si se desea agregar una solución adicional durante la etapa productiva
    agregar_solucion = input("¿Desea agregar una solución adicional durante la etapa productiva? (si/no): ").strip().lower().replace('í', 'i')
    # Remover acentos
    if agregar_solucion == "si":
        volumen_adicional = float(input("Ingrese el volumen de la solución adicional en ml: "))
        return volumen_adicional
    else:
        return None
#######################################################################################
#Combinación de funciones para calucular la glucosa necesaria para el proceso, durante la etapa productiva:
def tasa_crecimiento():
    pass
def calGlucConsumida():
    pass
def listaGlucEsperada():
    pass
def AgregadosGluc():
    pass
#######################################################################################
def calcular_costos():
    pass
#######################################################################################
def calcular_productividad():
    pass
#######################################################################################
def cargar_datos_proceso():
    # Se crea un diccionario que será completado con las características de la molécula.
    proceso = {}
    
    # Ingresar el nombre de la molécula
    nombre_molecula = input("Ingrese el nombre de la molécula: ")
    proceso["nombre_molecula"] = nombre_molecula 
    
    #Bloque estapa de expansión
    VCDinicial=input("Ingrese el valor de VCD con la que desea iniciar cada pasaje: ").replace(',', '.')
    VCDi=float(VCDinicial)
    cantPasajes=int(input("Ingrese la cantidad de pasajes que desea efectuar durante la etapa de expansión: "))
    diasxpasaje=int(input("Ingrese la cantidad de días que desea que tenga cada pasaje: "))
    calcular_dias_Exp=lambda diasxpasaje,cantPasajes: cantPasajes*diasxpasaje
    volInicial=int(input("Ingrese el volumen inicial del primer pasaje, en ml: "))
    VCDstarget=listaVCDtarget(cantPasajes)
    ListavolFinalPasajes=calcularVolFinalPasajes(VCDi,VCDstarget,cantPasajes,volInicial)
    # Calcular el volumen total de medio de expansión necesario
    proceso["Volumen de Medio de Expansión necesario"]="{:.1f}".format(calcularMedioExp(ListavolFinalPasajes))
    
    #Bloque de estapa productiva
    cantdiasFB=int(input("Ingrese la cantidad de días de la etapa productiva que tendrá su proceso: "))
    periodoFeed=int(input("Ingrese cada cuántos días se agregará el Feed: "))
    ###Creación de una matriz de forma estática:
    matrizBrx=[["Biorreactor","BRX500","BRX1000","BRX2000"],["Volúmen mínimo","150","300","600"],["Volúmen máximo","550","1100","2200"]]
    ANCHO_COLUMNA=15
    print("Considerando los siguientes volúmenes mínimos y máximos permitidos por los biorreactores disponibles: ")
    MatrizComoTabla(matrizBrx,ANCHO_COLUMNA)     
    volFinalFB=int(input("Ingrese el vólumen final al cual desea llegar en su etapa productiva en litros: "))
    Bandera=True
    while Bandera:
        if volFinalFB<=550:
            volInicialFB=150
            Bandera = False
        elif volFinalFB>550 and volFinalFB<=1100:
            volInicialFB=300
            Bandera = False
        elif volFinalFB>1100 and volFinalFB<=2200:
            volInicialFB=600
            Bandera = False  # Salir del bucle si el valor es válido
        else:
            print("El valor de volúmen Final ingresado no está dentro del rango permitido.")
            volFinalFB = float(input("Ingrese un nuevo valor para volFinalFB dentro del rango permitido: "))
    proceso["Volumen_Inicial"]=volInicialFB
    
    #Calculo de Cantidad de Medio Productivo por agregado necesario en el proceso:
    diasFB=(lambda n: list(range(n)))(cantdiasFB+1)
    diasAgregadoFeed=diasFB[1::periodoFeed]
    cantFeedPorAgregado= lambda diasAgregadoFeed,volFinalFB,volInicialFB: "{:.1f}".format((volFinalFB+volInicialFB)/(len(diasAgregadoFeed))) 
    proceso["Volumen_feed_por_agregado"]=cantFeedPorAgregado(diasAgregadoFeed,volFinalFB,volInicialFB)
    
    proceso["Duracion_Proceso"] = calcular_dias_Exp(diasxpasaje, cantPasajes) + cantdiasFB
    
    
    volumen_sol_adicional = agregar_solucion_adicional()
    if volumen_sol_adicional is not None:
        proceso["Volumen_Solución_Adicional"] = "{:.1f}".format(volumen_sol_adicional)
    else:
        proceso["Volumen_Solución_Adicional"] = "No se agrega solución adicional" 
     
    
    return proceso
    
         
#######################################################################################
#Función para mostrar procesos guardados:
def mostrar_todos_los_procesos():
    """Función para mostrar todos los procesos guardados"""
    if not procesos_guardados:
        print("No hay procesos almacenados.")
    else:
        for i, (nombre, proceso) in enumerate(procesos_guardados.items()):
            print(f"\nProceso {i + 1}:")
            mostrar_proceso(proceso)

def mostrar_proceso(proceso):
    """Función para mostrar los detalles de un proceso"""
    print(f"Nombre de la molécula: {proceso['nombre_molecula']}")
    print(f"Duración del Proceso: {proceso['Duracion_Proceso']}")
    print(f"Volumen de Medio de Expansión necesario: {proceso['Volumen de Medio de Expansión necesario']} ml")
    print(f"Volumen de Medio de Productivo con el que se debe iniciar el proceso: {proceso['Volumen_Inicial']} litros")
    print(f"Volumen de Solución Feed a añadir en cada agregado: {proceso['Volumen_feed_por_agregado']} litros")
    print(f"Volumen de Solución Adicional: {proceso['Volumen_Solución_Adicional']} ml")
    
#######################################################################################
#Programa Principal:
procesos_guardados={}
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
            procesos_guardados[proceso["nombre_molecula"]]=proceso # Guardamos el proceso en la lista global
            print(f"Proceso para {proceso['nombre_molecula']} guardado exitosamente.\n")
        
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

#######################################################################################
 
