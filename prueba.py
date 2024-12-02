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

def calcular_volumen_acumulado(volInicialFB, FeedPorAgregados, dias):
    """
    Calcula el volumen acumulado para cada día de agregado de feed.
    """
    vol_acumulado = []
    for i in range(len(dias)):
        vol_acumulado.append(volInicialFB + FeedPorAgregados * i)
    return vol_acumulado

print(calGlucConsumida(100, 50, 0.04, [1, 2, 3], [0.0, 0.0, 0.0]))


