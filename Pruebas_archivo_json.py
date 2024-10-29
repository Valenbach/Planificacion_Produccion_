import json

def Crear_Procesos():
    proceso= {}
    
    bandera= True
    
    while bandera:
        try:
            proceso["Molecula"]=int(input("ingrese el nombr e de la molecula\n"))
            proceso["Etapas expansivas"]=int(input("ingrese la cantidad de etapas expansivas"))
            bandera= False
        except ValueError:
            print("Datos invalidos, reintente la carga")
    return proceso


def Cargar_Procesos(Procesos_Guardados.json, ):
