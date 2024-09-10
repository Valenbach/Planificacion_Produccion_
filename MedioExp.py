def calcularVolFinalPasajes(VCDi,VCDstarget,cantPasajes,volInicial):
    #Generar una lista en la que se almacene el volumen final de cada pasaje.
    listavolFinalPasajes=[]
    for i in range(cantPasajes):
        volFinalPasaje=(VCDi*volInicial)/VCDstarget[i]
        listavolFinalPasajes.append(volFinalPasaje)
        VCDi=VCDstarget[i]
        volInicial=volFinalPasaje 
    return listavolFinalPasajes

def listaVCDtarget(cantPasajes):
    VCDstarget=[]
    for i in range(cantPasajes):
        VCDtarget=float(input(f"Ingrese el valor de VCD target para el pasaje {i+1}: "))
        VCDstarget.append(VCDtarget)
    return VCDstarget

def calcularMedioExp(listavolFinalPasajes):
    #Sumar los pesos de los volumenes finales de cada pasaje para calcular el volumen final de medio necesario.
    volMedioExp=sum(listavolFinalPasajes)
    return volMedioExp
VCDi=float(input("Ingrese el valor de VCD con la que desea iniciar cada pasaje: "))
while VCDi <= 0:
    VCDi = float(input("Ha ingresado un valor no permitido. Reingrese el valor de VCD con la que desea iniciar cada pasaje: "))

cantPasajes=int(input("Ingrese la cantidad de pasajes que desea efectuar durante la etapa de expansión: "))
VCDtarget=listaVCDtarget(cantPasajes)
volInicial=int(input("Ingrese el volumen inicial del primer pasaje, en ml: "))   
    
ListavolFinalPasajes=calcularVolFinalPasajes(VCDi,VCDtarget,cantPasajes,volInicial)
print("Los volumenes finales de los pasajes a realizar son los siguientes: ", ListavolFinalPasajes,"ml")
VolFinalPasajes=calcularMedioExp(ListavolFinalPasajes)
print("El volumen final de medio de expansión necesario para el proceso es: ", VolFinalPasajes,"ml")
