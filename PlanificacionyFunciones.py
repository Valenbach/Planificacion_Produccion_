#################################FUNCIONES PARA CALCULAR VOLUMEN TOTAL DEL MEDIO################################################
""""
Con la combinación de las siguientes funciones se establece el volúmen final a utilizar de medio de expansión, 
de acuerdo a los requerimientos del cliente.
"""
def listaVCDtarget(cantPasajes):
    """"
    Generar una lista en la que se almacene la VCD que se desea alcanzar en cada pasaje, r
    ecibe como parámetro la cantidad de pasajes, la cual es ingresada por teclado (por el usuario).
    """
    VCDstarget=[]
    for i in range(cantPasajes):
        Bandera= False
        while not Bandera:
            try:
                VCDtargetIngreso=input(f"Ingrese el valor de VCD target para el pasaje {i+1}: ").replace(',', '.')
                VCDtarget=float(VCDtargetIngreso)
                VCDstarget.append(VCDtarget)
                Bandera=True
            except ValueError:
                print("Error: Debe ingresar un número válido para VCD target.")
    return VCDstarget

def calcularVolFinalPasajes(VCDi,VCDstarget,cantPasajes,volInicialExp):
    
    """"
    Realizar el cálculo del volumen final que tendrá cada pasaje y a su vez generar una lista en la que se almacenen estos volúmenes,
    recibe como parámetro VCD inicial de la etapa de expansión, cantidad de pasajes de la etapa de expansión y volúmen inicial del primer pasaje, todos ingresados por teclado (por el usuario); y VCD target (objetivo) que cada pasaje deberá alcanzar, este último dato se toma de la lista generada en la función anterior (listaVCDtarget).
    """
    listavolFinalPasajes=[]
    for i in range(cantPasajes):
        volFinalPasaje=(VCDi*volInicialExp)/VCDstarget[i]
        listavolFinalPasajes.append(volFinalPasaje)
        VCDi=VCDstarget[i]
        volInicialExp=volFinalPasaje 
    return listavolFinalPasajes

def calcularMedioExp(listavolFinalPasajes,volInicialExp):
    """"
    Sumar los pesos de los volumenes finales de cada pasaje para calcular el volumen final de medio de expansión necesario, 
    recibe como parámetro la lista de los volúmenes de los pasajes calculados en la función anterior (calcularVolFinalPasajes).
    """
    volMedioExp=sum(listavolFinalPasajes)+volInicialExp
    return volMedioExp

#######################################################################################
"""Funciones Auxiliares:
"""
def MatrizComoTabla(matriz,ancho_columna):
    """
    Imprimir una matriz en forma de tabla. Recibe como parámetros: una matriz y el ancho de la columna de la tabla
    (máximo de caracteres para que se ajusten las columnas).
    """
    for fila in matriz:
        for elemento in fila:
            print(f"{elemento:>{ancho_columna}}",end=" | ")
        print()
#######################################################################################
def agregar_solucion_adicional():
    """"
    Preguntar si se desea agregar una solución adicional durante la etapa productiva, 
    en caso afirmativo consultar qué volumen de esta solución se agregará.
    """
    Bandera=False
    while not Bandera:
        agregar_solucion = input("¿Desea agregar una solución adicional durante la etapa productiva? (si/no): ").strip().lower().replace('í', 'i') # Comandos para pasar la respuesta ingresada por teclado a minúscula y remover el acento de ser necesario.
        if agregar_solucion in ["si","no"]:
            Bandera= True
        else:
            print("Error: Ingrese 'si' o 'no'.")
            
    if agregar_solucion == "si":
        Bandera=False
        while not Bandera:
            try:
                volumen_adicional = float(input("Ingrese el volumen de la solución adicional en ml que se añadirá en cada agregado: "))
                periodo_sol_adicional=float(input("Por cuantos días agregará esta solución: "))
                volumen_adicional_total=volumen_adicional*periodo_sol_adicional
                return volumen_adicional_total
            except ValueError:
                print("Error: Debe ingresar un número válido tanto para el dato del volumen como para el dato del período.")
    else:
        return None
#######################################################################################
"""
Combinación de funciones para calucular la glucosa necesaria para el proceso, durante la etapa productiva:
"""
def tasa_crecimiento(VCDiFB, DURACION_POR_DIA, diasAgregadoFeed):
    listaTasa_crecimiento = []
    VCDf = VCDiFB * 2
    
    for i in range(len(diasAgregadoFeed)):
        crecimiento = VCDf / (diasAgregadoFeed[i] * DURACION_POR_DIA)
        crecimientoRedondeado = float("{:.3f}".format(crecimiento))
        listaTasa_crecimiento.append(crecimientoRedondeado)
        VCDf *= 2
        
    return listaTasa_crecimiento

def calGlucConsumida(volInicialFB, FeedPorAgregados, TASA_ESPECIFICA_CONSUMO_GLUC, diasAgregadoFeed, tasa_crecimiento):
    listaGlucConsumida = []
    MedioProdAcumulado = FeedPorAgregados + volInicialFB
    
    for i in range(len(diasAgregadoFeed)):
        GlucConsumida = TASA_ESPECIFICA_CONSUMO_GLUC * MedioProdAcumulado * tasa_crecimiento[i]
        listaGlucConsumida.append(GlucConsumida)
        MedioProdAcumulado += FeedPorAgregados
    
    return listaGlucConsumida

def AgregadosGluc(diasAgregadoFeed, aporte_Gluc_MedioProd_inicial, aporte_Gluc_MedioProd, GlucTarget, lista_Gluc_Consumida):
    GlucPorAgregado = []
    calcuGlucEsperada = aporte_Gluc_MedioProd_inicial
    
    for i in range(len(diasAgregadoFeed)):
        calcuGlucEsperada -= lista_Gluc_Consumida[i]
        
        if GlucTarget < calcuGlucEsperada:
            Gluc_Agregar = 0
        else:
            Gluc_Agregar = GlucTarget - calcuGlucEsperada
        
        GlucPorAgregado.append(Gluc_Agregar)
        
        # Asegurar que la glucosa esperada se reinicia cada ciclo
        calcuGlucEsperada += aporte_Gluc_MedioProd
    
    return GlucPorAgregado
#######################################################################################
"""
Combinación de funciones para efectuar los cálculos de los costos que conllevará el preceso de acuerdo a la información recolectada:
"""
def calcular_costos():
    pass
#######################################################################################
"""
Combinación de funciones para efectuar los cálculos de productividad esperada:
"""
def calcular_productividad():
    pass
#######################################################################################
def cargar_datos_proceso(nombre_molecula, ListavolFinalPasajes, volInicialFB, diasAgregadoFeed, volFinalFB, diasxpasaje, cantPasajes, cantdiasFB, listaTasaCrecimiento, lista_Gluc_Consumida, lista_Agregados_Gluc):
    """"
    Crear un diccionario que será completado con las características de la molécula.
    Parámetros de ingreso: nombre_molecula,ListavolFinalPasajes,volInicialFB,diasAgregadoFeed,volFinalFB,diasxpasaje,cantPasajes,cantdiasFB.
    """
    proceso = {}
       
    proceso["nombre_molecula"] = nombre_molecula 
    
    proceso["Volumen de Medio de Expansión necesario"]="{:.1f}".format(calcularMedioExp(ListavolFinalPasajes,volInicialExp))
      
    proceso["Volumen_Inicial"]=volInicialFB
        
    proceso["Volumen_feed_por_agregado"]=cantFeedPorAgregado(diasAgregadoFeed,volFinalFB,volInicialFB)
    
    proceso["Duracion_Proceso"] = calcular_dias_Exp(diasxpasaje, cantPasajes) + cantdiasFB
    
    proceso["tasa_crecimiento"]=["{:.2f}".format(tasa)for tasa in listaTasaCrecimiento]
    
    proceso["gluc_consumida"]=["{:.2f}".format(tasa) for tasa in lista_Gluc_Consumida]
    
    proceso["Agregados_Glucosa"]=["{:.2f}".format(tasa) for tasa in lista_Agregados_Gluc]
    
    volumen_sol_adicional = agregar_solucion_adicional()
    if volumen_sol_adicional is not None:
        proceso["Volumen_Solución_Adicional"] = "{:.1f}".format(volumen_sol_adicional)
    else:
        proceso["Volumen_Solución_Adicional"] = "No se agrega solución adicional" 
         
    return proceso         
#######################################################################################
"""
Combinación de funciones para mostrar procesos guardados:
"""
def mostrar_todos_los_procesos():
    #Mostrar todos los procesos guardados.
    if not procesos_guardados:
        print("No hay procesos almacenados.")
    else:
        for i, (nombre, proceso) in enumerate(procesos_guardados.items()):
            print(f"\nProceso {i + 1}:")
            mostrar_proceso(proceso)

def mostrar_proceso(proceso):
    """
    Mostrar los detalles de un proceso guardados en la función "cargar_datos_proceso" como valores de las claves.
    """
    print(f"Nombre de la molécula: {proceso['nombre_molecula']}")
    print(f"Duración del Proceso: {proceso['Duracion_Proceso']}")
    print(f"Volumen de Medio de Expansión necesario: {proceso['Volumen de Medio de Expansión necesario']} ml")
    print(f"Volumen de Medio de Productivo con el que se debe iniciar el proceso: {proceso['Volumen_Inicial']} litros")
    print(f"Volumen de Solución Feed a añadir en cada agregado: {proceso['Volumen_feed_por_agregado']} litros")
    print(f"El crecimiento esperado por día de monitoreo es:{proceso["tasa_crecimiento"]}")
    print(f"La concentración de glucosa a agergar por cada día en el que se realiza monitoreo es: {proceso["Agregados_Glucosa"]} g/l")
    print(f"El consumo de glucosa esperada es: {proceso["gluc_consumida"]} g/l")
    print(f"Volumen de Solución Adicional: {proceso['Volumen_Solución_Adicional']} ml")

#######################################################################################
"""
#Programa Principal bloque 1= Menu interactivo principal:

"""
procesos_guardados={}
try:
    while True:
        print("\nBienvenido al menú principal, seleccione una opción para continuar\n")
        print("1. Cargar nuevo proceso")
        print("2. Ver procesos guardados")
        print("3. Calcular costos del proceso")
        print("4. Salir")
        
        try:
            opcion = int(input("Ingrese el número de la opción seleccionada: "))
            if opcion < 1 or opcion > 4:
                print("Error: Debe Ingresar un valor entre 1 y 4.")
                opcion= None
        except ValueError:
            print("Error: El valor ingresado es inválido.")
        
        if opcion == 1:
            print("SE ENCUENTRA EN LA SECCIÓN DE CARGA DE DATOS PARA GENERAR UN NUEVO PROCESO")
            """
            Datos de ingresos, llamados de funciones y funciones lambda necesarios:
           
            """
            nombre_molecula = input("Ingrese el nombre de la molécula: ")

            VCDinicial=input("Ingrese el valor de VCD con la que desea iniciar cada pasaje: ").replace(',', '.')
            VCDi=float(VCDinicial)

            cantPasajes=int(input("Ingrese la cantidad de pasajes que desea efectuar durante la etapa de expansión: "))
            diasxpasaje=int(input("Ingrese la cantidad de días que desea que tenga cada pasaje: "))

            """
            Función lambda para calcular el total de los días de la estapa de expansión:
            
            """
            calcular_dias_Exp=lambda diasxpasaje,cantPasajes: cantPasajes*diasxpasaje

            volInicialExp=int(input("Ingrese el volumen inicial del primer pasaje, en ml: "))
            VCDstarget=listaVCDtarget(cantPasajes)
            ListavolFinalPasajes=calcularVolFinalPasajes(VCDi,VCDstarget,cantPasajes,volInicialExp)


            """
            Creación de una matriz de forma estática:
            """
            
            matrizBrx=[["Biorreactor","BRX500","BRX1000","BRX2000"],["Volúmen mínimo","150","300","600"],["Volúmen máximo","550","1100","2200"]]
            ANCHO_COLUMNA=15
            print("Considerando los siguientes volúmenes mínimos y máximos permitidos por los biorreactores disponibles: ")
            MatrizComoTabla(matrizBrx,ANCHO_COLUMNA)     

            #Bloque para determinar el volumen inicial de la etapa productiva:
            volFinalFB=int(input("Ingrese el vólumen final al cual desea llegar en su etapa productiva en litros: "))
            Bandera=True
            while Bandera:
                if volFinalFB<=550 and volFinalFB>= 300:
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

            cantdiasFB=int(input("Ingrese la cantidad de días de la etapa productiva que tendrá su proceso: "))
            periodoFeed=int(input("Ingrese cada cuántos días se agregará el Feed: "))
            
            """
            Función lambda para armar una lista con números en un rango de 0 hasta n-1 de acuerdo a la cantidad de días de la etapa productiva: 
            
            """
            diasFB=(lambda n: list(range(n)))(cantdiasFB)
            
            """
            Función lambda para el calculo de Cantidad de Medio Productivo por agregado necesario en el proceso:
            
            """
            try:
                diasAgregadoFeed=diasFB[1::periodoFeed]
                cantFeedPorAgregado= lambda diasAgregadoFeed,volFinalFB,volInicialFB: "{:.1f}".format((volFinalFB-volInicialFB)/(len(diasAgregadoFeed)))
            except ZeroDivisionError:
                print("Error: La cantidad de días de agregado de Feed no puede ser cero.Reingrese un dato válido.") 
            
            """
            Información necesaria para las funciones involucradas en el cálculo de glucosa
            """
            VCDiFB=VCDstarget[-1]
            DURACION_POR_DIA=24 #h.
            TASA_ESPECIFICA_CONSUMO_GLUC=0.04 #g/cel/24h 
            APORTE_GLUC_MEDIOPROD=4.5 #g/L
            FeedPorAgregados = float(cantFeedPorAgregado(diasAgregadoFeed, volFinalFB, volInicialFB))
            listaTasaCrecimiento = tasa_crecimiento(VCDiFB, DURACION_POR_DIA, diasAgregadoFeed)
            lista_Gluc_Consumida= calGlucConsumida(volInicialFB,FeedPorAgregados,TASA_ESPECIFICA_CONSUMO_GLUC,diasAgregadoFeed,listaTasaCrecimiento)
            aporte_Gluc_MedioProd_inicial=APORTE_GLUC_MEDIOPROD*volInicialFB
            aporte_Gluc_MedioProd= APORTE_GLUC_MEDIOPROD*FeedPorAgregados
            GlucTarget=float(input("Ingrese el valor de concentración de glucosa en la que desea mantener el cultivo durante la etapa productiva en g/L:"))
            lista_Agregados_Gluc=AgregadosGluc(diasAgregadoFeed,aporte_Gluc_MedioProd_inicial,aporte_Gluc_MedioProd,GlucTarget,lista_Gluc_Consumida)
            
            proceso = cargar_datos_proceso(nombre_molecula, ListavolFinalPasajes, volInicialFB, diasAgregadoFeed, volFinalFB, diasxpasaje, cantPasajes, cantdiasFB, listaTasaCrecimiento, lista_Gluc_Consumida, lista_Agregados_Gluc)
            # Guardar el proceso en el diccionario global
            procesos_guardados[proceso["nombre_molecula"]]=proceso
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
            
            
except ValueError as e:
    print(f"Error de valor: {e}. Asegúrese de ingresar los datos correctamente.")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}. Por favor, intente nuevamente.")
finally:
    print("El programa ha finalizado, gracias por utilizarlo.")

#######################################################################################
 
