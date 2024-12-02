import json
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
        try:
            volFinalPasaje=(VCDi*volInicialExp)/VCDstarget[i]
            listavolFinalPasajes.append(volFinalPasaje)
            VCDi=VCDstarget[i]
            volInicialExp=volFinalPasaje
        except ZeroDivisionError:
            print(f"Error: La VCD target no puede ser 0 en el pasaje {i+1}")
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
def tasa_crecimiento(VCDiFB, DURACION_POR_DIA, diasAgregadoFeed, DUPLICACION):
    """"
    Estimar el crecimiento celular esperado en los días en que se agrega Feed y crear una lista con estos datos.Recibe como parámetros: VCDiFB (VCD inicial de la etapa productiva), DURACION_POR_DIA (variable fija que transforma a la cantidad de días en horas), diasAgregadoFeed y DUPLICACION (factor de duplicacion estimado).
    """
    listaTasa_crecimiento = []
    VCDf = VCDiFB
    
    for dia in diasAgregadoFeed:
        crecimiento = VCDf * DUPLICACION / DURACION_POR_DIA
        crecimientoRedondeado = float("{:.3f}".format(crecimiento))
        listaTasa_crecimiento.append(crecimientoRedondeado)
        VCDf*=  DUPLICACION
        
    return listaTasa_crecimiento

def calcular_volumen_acumulado(volInicialFB, FeedPorAgregados, dias):
    """
    Calcula el volumen acumulado para cada día de agregado de feed.
    """
    vol_acumulado = []
    for i in range(len(dias)):
        vol_acumulado.append(volInicialFB + FeedPorAgregados * i)
    return vol_acumulado

def calGlucConsumida(volInicialFB, FeedPorAgregados, TASA_ESPECIFICA_CONSUMO_GLUC, diasAgregadoFeed, tasa_crecimiento):
    """"
    Calcular la glucosa consumida en los perídos de tiempo entre los días de agregado de feed y crear una lista con estos datos.Recibe como parámetros: volInicialFB (volumen inicial de la etapa productiva), FeedPorAgregados (cantidad de feed que se añade en cada agregregado, siempre se agrega el mismo volumen), TASA_ESPECIFICA_CONSUMO_GLUC (factor de consumo de glucosa estimado), diasAgregadoFeed y la lista tasa_crecimiento obtenida con la función anterior.
    """
    volAcumulado = calcular_volumen_acumulado(volInicialFB, FeedPorAgregados, diasAgregadoFeed)
    listaGlucConsumida = []
    for i in range(len(diasAgregadoFeed)):
        gluc_consumida= (TASA_ESPECIFICA_CONSUMO_GLUC * volAcumulado[i] * tasa_crecimiento[i])/10
        listaGlucConsumida.append(gluc_consumida)
    
    return listaGlucConsumida

def AgregadosGluc(diasAgregadoFeed, aporte_Gluc_MedioProd_inicial, aporte_Gluc_MedioProd, GlucTarget, lista_Gluc_Consumida):
    """"
    Estimar la glucosa que se necesitará agregar dependiendo del valor target en que se desea mantener ésta durante el la etapa productiva, en los días de agregado de feed y crear una lista con estos datos.Recibe como parámetros: diasAgregadoFeed, aporte_Gluc_MedioProd_inicial (aporte de glucosa del medio productivo que se agrega al inicio de la etapa), aporte_Gluc_MedioProd (aporte de glucosa del feed en cada agregado) GlucTarget (concentración de glucosa en la que se desea mantener la etapa productiva) y la lista lista_Gluc_Consumida obtenida con la función anterior.
    """
    GlucPorAgregado = []
    calcuGlucEsperada = aporte_Gluc_MedioProd_inicial / 10000
    
    for i in range(len(diasAgregadoFeed)):
        
        calcuGlucEsperada -= lista_Gluc_Consumida[i] / 10000
                
        if calcuGlucEsperada < GlucTarget :
            Gluc_Agregar = ((GlucTarget / 10000) - calcuGlucEsperada)*(-1)
            calcuGlucEsperada = GlucTarget / 10000
        else:
            Gluc_Agregar = 0
        
        GlucPorAgregado.append(Gluc_Agregar)
        
        calcuGlucEsperada = (GlucTarget/ 10000) + (aporte_Gluc_MedioProd/ 10000)
            
    return GlucPorAgregado
#######################################################################################
"""
Combinación de funciones para efectuar los cálculos de los costos que conllevará el preceso de acuerdo a la información recolectada:
"""
"""
A continuación se desarrollará la función que se utilizará 
para calcular los costos de producción de un proceso específico,
la idea es establecer una tarifa que aumentará en función de los días de proceso.

"""

def calcular_costos(molecula):
    try:
        with open("procesos.json", "r") as procesos:
            data = json.load(procesos)
    except (IOError, json.JSONDecodeError):
        return "No se han guardado procesos aún."

    # Buscar la molécula en los datos cargados
    for proceso in data:
        if proceso["nombre_molecula"].lower() == molecula.lower():
            dias_exp = proceso['Duracion de etapa Expansiva']
            dias_produ = proceso['Duracion de la etapa productiva']
            costo_base_exp = 1200
            costo_base_produ = 3500
            
            # Cálculo del costo de expansión
            if 1 <= dias_exp <= 3:
                costo_exp = costo_base_exp + (dias_exp * 300)
            elif 4 <= dias_exp <= 8:
                costo_exp = costo_base_exp + (dias_exp * 400)
            elif 8 < dias_exp <= 12:
                costo_exp = costo_base_exp + (dias_exp * 700)
            elif dias_exp > 12:
                costo_exp = costo_base_exp + (dias_exp * 900)
            else:
                costo_exp = 0  # Si no hay días de expansión, no hay costo

            # Cálculo del costo productivo
            if 1 <= dias_produ <= 4:
                costo_produ = costo_base_produ + (dias_produ * 700)
            elif 4 < dias_produ <= 6:
                costo_produ = costo_base_produ + (dias_produ * 900)
            elif 6 < dias_produ <= 9:
                costo_produ = costo_base_produ + (dias_produ * 1200)
            elif 9 < dias_produ <= 12:
                costo_produ = costo_base_produ + (dias_produ * 1500)
            elif dias_produ > 12:
                costo_produ = costo_base_produ + (dias_produ * 2000)
            else:
                costo_produ = 0  # Si no hay días productivos, no hay costo
            
            return costo_exp, costo_produ

    # Mensaje si no se encuentra la molécula
    return "Molécula no encontrada."
#######################################################################################
def calcular_productividad_esperada(listaTasaCrecimiento, cantdiasFB):
    """
    Calcular la productividad esperada del proceso.
    Recibe como parámetros:
    - listaTasaCrecimiento: Lista de la tasa de crecimiento diaria (VCD).
    - cantdiasFB: Cantidad de días de la etapa productiva.
    
    Retorna la productividad total estimada en gramos.
    """
    PRODUCTIVIDAD_FACTOR = 1.25  # g de producto por VCD y por día
    productividad_total = 0

    for vcd_dia in listaTasaCrecimiento[:cantdiasFB]:
        productividad_diaria = vcd_dia * PRODUCTIVIDAD_FACTOR
        productividad_total += productividad_diaria

    return productividad_total
#########################################################################################################################################################################

def cargar_datos(nombre_molecula, ListavolFinalPasajes, volInicialFB,DiasProdu, diasAgregadoFeed, volFinalFB, diasxpasaje, cantPasajes, cantdiasFB, listaTasaCrecimiento, lista_Gluc_Consumida, lista_Agregados_Gluc, productividad_esperada):
    # Intentamos cargar el archivo si existe, o inicializamos una lista vacía si no
    try:
        with open("procesos.json", "r") as procesos:
            data = json.load(procesos)
    except (IOError, json.JSONDecodeError):
        data = []  # Si el archivo está vacío o no existe, inicializamos una lista vacía

    # Agregamos el nuevo proceso a la lista de procesos
    volumen_sol_adicional = agregar_solucion_adicional()
    if volumen_sol_adicional is not None:
        Solu_adic= "{:.1f}".format(volumen_sol_adicional)
    else:
        Solu_adic= "No se agrega solución adicional"
    nuevo_proceso = {"nombre_molecula": nombre_molecula, "Volumen de Medio de Expansion necesario":"{:.1f}".format(calcularMedioExp(ListavolFinalPasajes,volInicialExp)),
                     "Duracion de etapa Expansiva": diasxpasaje*cantPasajes,"Duracion de la etapa productiva":DiasProdu,
                     "Volumen_Inicial":volInicialFB,"Volumen_feed_por_agregado":cantFeedPorAgregado(diasAgregadoFeed,volFinalFB,volInicialFB),
                     "Duracion_Proceso":calcular_dias_Exp(diasxpasaje, cantPasajes) + cantdiasFB,
                     "tasa_crecimiento":["{:.2f}".format(tasa)for tasa in listaTasaCrecimiento],
                     "gluc_consumida":["{:.2f}".format(tasa) for tasa in lista_Gluc_Consumida],
                     "Agregados_Glucosa":["{:.2f}".format(tasa) for tasa in lista_Agregados_Gluc],
                     "salucion adicional":Solu_adic, "productividad_esperada":"{:.2f}".format(productividad_esperada)}
    data.append(nuevo_proceso)

    # Escribimos la lista actualizada de procesos en el archivo JSON
    with open("procesos.json", "w") as procesos:
        json.dump(data, procesos, indent=4) 
    print("proceso guardado correctamente")
       
    

"""
Función para calcular costos de proceso:

"""
################################################################################################################################################################
"""
Función para mostrar procesos guardados:
"""
def mostrar_nombres_moleculas():
    try:
        # Cargar los datos del archivo JSON
        with open("procesos.json", "r") as procesos:
            data = json.load(procesos)
        
        # Extraer y mostrar los nombres de todas las moléculas guardadas
        nombres = [proceso["nombre_molecula"] for proceso in data]
        if nombres:
            print("Moléculas guardadas:")
            for nombre in nombres:
                print("- " + nombre)
        else:
            print("No hay moléculas guardadas.")
    
    except (IOError, json.JSONDecodeError):
        print("No se han guardado procesos aún.")

def obtener_datos_por_molecula(nombre_molecula):
    try:
        with open("procesos.json", "r") as procesos:
            data = json.load(procesos)
    except (IOError, json.JSONDecodeError):
        return "No se han guardado procesos aún."

    # Buscar la molécula en los datos cargados
    for proceso in data:
        if proceso["nombre_molecula"].lower() == nombre_molecula.lower():
            # Formateamos y retornamos los datos de la molécula
            return (
                f"\nDatos de la molécula '{proceso['nombre_molecula']}':\n"
                f"- Volumen de Medio de Expansión necesario: {proceso['Volumen de Medio de Expansion necesario']} ml\n"
                f"- Duración de la etapa Expansiva: {proceso['Duracion de etapa Expansiva']} días\n"
                f"- Duración de la etapa Productiva: {proceso['Duracion de la etapa productiva']} días\n"
                f"- Volumen Inicial: {proceso['Volumen_Inicial']} ml\n"
                f"- Volumen Feed por Agregado: {proceso['Volumen_feed_por_agregado']} ml\n"
                f"- Duración Total del Proceso: {proceso['Duracion_Proceso']} días\n"
                f"- Tasas de Crecimiento: {', '.join(proceso['tasa_crecimiento'])}\n"
                f"- Glucosa Consumida: {', '.join(proceso['gluc_consumida'])}\n"
                f"- Agregados de Glucosa: {', '.join(proceso['Agregados_Glucosa'])}\n"
                f"- Solución Adicional: {proceso['salucion adicional']}\n"
                f"- Productividad Esperada: {proceso['productividad_esperada']}\n"
            )
    return "Molécula no encontrada."

###########################################################################################################################################
"""
Función para validar que los números ingresaods sean positivos

"""
def solicitar_valor_positivo(mensaje):
    while True:
        try:
            valor = float(input(mensaje).replace(',', '.'))
            if valor <= 0:
                print("Error: El valor no puede ser negativo. Intente nuevamente.")
            else:
                return valor
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número válido.")

#############################################################################################################################################

"""
#Programa Principal bloque 1= Menu interactivo principal:

"""
try:
    while True:
        print("\n" + "="*40)
        print(f"{'BIENVENIDO AL SISTEMA DE PLANIFICACIÓN DE PRODUCCIÓN':^40}")
        print("="*40)
        print("\nSeleccione una opción:")
        print("1. Cargar nuevo proceso")
        print("2. Ver procesos guardados")
        print("3. Seleccionar datos de una molécula")
        print("4. Calcular costos del proceso")
        print("5. Salir")

        try:
            opcion = int(input("Ingrese el número de la opción seleccionada: "))
            if opcion < 1 or opcion > 5:
                print("Error: Debe Ingresar un valor entre 1 y 5.")
                opcion= None
        except ValueError:
            print("Error: El valor ingresado es inválido.")
        
        if opcion == 1:
            print("\nHas seleccionado 'Cargar nuevo proceso'.")
            """
            Datos de ingresos, llamados de funciones y funciones lambda necesarios:
           
            """
            nombre_molecula = input("Ingrese el nombre de la molécula: ")
        
            VCDinicial=int(solicitar_valor_positivo("Ingrese el valor de VCD con la que desea iniciar cada pasaje: "))
            VCDi=float(VCDinicial)

            cantPasajes=int(solicitar_valor_positivo("Ingrese la cantidad de pasajes que desea efectuar durante la etapa de expansión: "))
            diasxpasaje=int(solicitar_valor_positivo("Ingrese la cantidad de días que desea que tenga cada pasaje: "))

            """
            Función lambda para calcular el total de los días de la estapa de expansión:
            
            """
            calcular_dias_Exp=lambda diasxpasaje,cantPasajes: cantPasajes*diasxpasaje

            volInicialExp=int(solicitar_valor_positivo("Ingrese el volumen inicial del primer pasaje, en ml: "))
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
            volFinalFB=int(solicitar_valor_positivo("Ingrese el vólumen final al cual desea llegar en su etapa productiva en litros: "))
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

            cantdiasFB=int(solicitar_valor_positivo("Ingrese la cantidad de días de la etapa productiva que tendrá su proceso: "))
            periodoFeed=int(solicitar_valor_positivo("Ingrese cada cuántos días se agregará el Feed: "))
            
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
            APORTE_GLUC_MEDIOPROD=30 #g/L
            DUPLICACION=1.2
            FeedPorAgregados = float(cantFeedPorAgregado(diasAgregadoFeed, volFinalFB, volInicialFB))
            listaTasaCrecimiento = tasa_crecimiento(VCDiFB, DURACION_POR_DIA, diasAgregadoFeed,DUPLICACION)   
        
            lista_Gluc_Consumida= calGlucConsumida(volInicialFB,FeedPorAgregados,TASA_ESPECIFICA_CONSUMO_GLUC,diasAgregadoFeed,listaTasaCrecimiento)
            aporte_Gluc_MedioProd_inicial=APORTE_GLUC_MEDIOPROD*volInicialFB
            aporte_Gluc_MedioProd= APORTE_GLUC_MEDIOPROD*FeedPorAgregados
            GlucTarget=float(solicitar_valor_positivo("Ingrese el valor de concentración de glucosa en la que desea mantener el cultivo durante la etapa productiva en g/L:"))
            lista_Agregados_Gluc=AgregadosGluc(diasAgregadoFeed,aporte_Gluc_MedioProd_inicial,aporte_Gluc_MedioProd,GlucTarget,lista_Gluc_Consumida)
            productividad_esperada = calcular_productividad_esperada(listaTasaCrecimiento, cantdiasFB)
            proceso = cargar_datos(nombre_molecula, ListavolFinalPasajes, volInicialFB,cantdiasFB, diasAgregadoFeed, volFinalFB, diasxpasaje, cantPasajes, cantdiasFB, listaTasaCrecimiento, lista_Gluc_Consumida, lista_Agregados_Gluc,productividad_esperada)
            
            print(f"Proceso guardado exitosamente. confirmación\n")

            
        elif opcion == 2:
            print("\nHas seleccionado 'Ver procesos guardados'.")
            mostrar_nombres_moleculas()
        
        elif opcion == 3:
            print("\nHas seleccionado 'Seleccionar datos de una molécula'.")
            nombre = input("Ingrese el nombre de la molécula: ")
            print(obtener_datos_por_molecula(nombre))
        elif opcion == 4:
            print("\nHas seleccionado 'Calcular costos del proceso'.")
            nombre = input("Ingrese el nombre de la molécula: ")
            Costo_Expansiva, Costo_productiva= calcular_costos(nombre)
            Costo_Total=Costo_productiva+Costo_Expansiva
            print("\n" + "="*50)
            print(f"{'Cálculo de Costos del Proceso':^50}")
            print("="*50)
            
            # Formatear los costos con 2 decimales y separador de miles
            costo_exp_formateado = f"${Costo_Expansiva:,.2f}"
            costo_produ_formateado = f"${Costo_productiva:,.2f}"
            costo_total_formateado = f"${Costo_Total:,.2f}"
            
            # Imprimir los resultados alineados y con formato
            print(f"\n{'Costo de la etapa expansiva:':<40} {costo_exp_formateado:>10}")
            print(f"{'Costo de la etapa productiva:':<40} {costo_produ_formateado:>10}")
            print(f"{'Costo total de producción:':<40} {costo_total_formateado:>10}")
            
            print("="*50)
                       
        elif opcion == 5:
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
