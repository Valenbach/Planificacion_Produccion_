
def MatrizComoTabla(matriz,ancho_columna):
    #Imprime una matriz en forma de tabla. Ingresos: una matriz y el ancho de la columna de la tabla(máximo de caracteres para que se ajusten las columnas)
    for fila in matriz:
        for elemento in fila:
            print(f"{elemento:>{ancho_columna}}",end=" | ")
        print()

diasFB=(lambda n: list(range(n)))(cantdiasFB+1)
cantMedioProductivoPorAgregado = lambda diasAgregadoFeed,volFinalFB,volInicialFB: ((volFinalFB-volInicialFB)/(len(diasAgregadoFeed))) 
cantdiasFB=int(input("Ingrese la cantidad de días de la etapa productiva: "))


periodoFeed=int(input("Ingrese cada cuántos días se agregará el Feed: "))
diasAgregadoFeed=diasFB[1::periodoFeed]


matrizBrx=[["Biorreactor","BRX500","BRX1000","BRX2000"],["Volúmen mínimo","150","300","600"],["Volúmen máximo","550","1100","2200"]]
anchoColumna=15

print("Considerando los siguientes volúmenes mínimos y máximos permitidos por los biorreactores disponibles: ")
MatrizComoTabla(matrizBrx,anchoColumna)
volInicialFB=int(input("Ingresar el volúmen de medio que desea ingresar a día 0: "))
volFinalFB=int(input("Ingrese el vólumen final al cual desea llegar en su etapa productiva en litros: "))

print(f"La cantidad de medio productivo por agregado es: {cantMedioProductivoPorAgregado(diasAgregadoFeed,volFinalFB,volInicialFB)}")


