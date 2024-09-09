def tasa_crecimiento(VCDiFB,duracionPorDia,diasAgregadoFeed):
    #Calcula el crecimiento celular exponencial considerandi que la VCD se duplica en 24 hs.
    listaTasa_crecimiento=[]
    VCDf=VCDiFB*2
    for i in range(len(diasAgregadoFeed)):
        crecimiento=(VCDf-VCDiFB)/((diasAgregadoFeed[i])*duracionPorDia)
        crecimientoRedondeado=float("{:.3f}".format(crecimiento))
        listaTasa_crecimiento.append(crecimientoRedondeado)
        VCDf=VCDf*4
    return listaTasa_crecimiento
###############################
def calGlucConsumida(volInicialFB,cantMedioProductivoPorAgregado,TASA_CONSUMO,duracionProceso,diasAgregadoFeed):
    for i in range(len(diasAgregadoFeed)):
        listaGlucConsumida=[]
        MedioProdAcumulado=cantMedioProductivoPorAgregado
        volFB=volInicialFB+MedioProdAcumulado
        GlucConsumida=TASA_CONSUMO*volFB*duracionProceso
        listaGlucConsumida.append(GlucConsumida)
        MedioProdAcumulado=MedioProdAcumulado+cantMedioProductivoPorAgregado
    return listaGlucConsumida
###############################        
def listaGlucEsperada(listGlucConsumida,Gl)
###############################
def AgregadosGluc(diasAgregadoFeed,aporteMedio,GlucTarget,GlucEsperada):
    GlucPorAgregado=[]
    for i in range(len(diasAgregadoFeed)):
        calcuGluc=(GlucTarget-(aporteMedio+GlucEsperada[i]))
        GlucPorAgregado.append(calcuGluc)
    return GlucPorAgregado
######################################

aporteMedio= lambda cantMedioProductivoPorAgregado,APORTEPORLFEED: (APORTEPORLFEED*cantMedioProductivoPorAgregado)
APORTEPORLFEED=2 #g/L

#######################

TASA_CONSUMO=0.2 #g/L/h
duracionPorDia = 24  # horas por día
TASA_CONSUMO_INICIAL = 2  # g/L x h 

#######################
volInicialFB = 600  # L usar la otra pestaña
cantMedioProductivoPorAgregado = 200  # L usar la otra pestaña
diasAgregadoFeed = [1, 3, 5, 7, 9, 11, 13]  # usar la otra pestaña
#######################

GlucTarget=float(input("Ingrese la concentración de glucosa que desea mantener durante la etapa productiva en gramos por litro: "))
VCDiFB=float(input("Ingrese el valor de VCD con la que desea inocular la etapa Fed Batch: "))












    