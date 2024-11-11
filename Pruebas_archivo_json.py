import json

def Cargar_Procesos(molecula,pasajes,fed):
    try:
        with open("Procesos.json","r") as archivo:
            procesos_guardados=json.load(archivo)
    except (IOError,json.JSONDecodeError):
        procesos_guardados=[]
    
    proceso={"nombre de molecula":molecula,"cantidad de pasajes":pasajes, "dias etapa productiva": fed}
    
    procesos_guardados.append(proceso)
    with open("Procesos.json","w") as archivo:
        json.dump(procesos_guardados,archivo,indent=4)
        
    return proceso
        
###Función PPal############


Mol=(input("Ingrese el nombre del proceso"))

Pasajes=int(input("Ingrese la cantidad de pasajes"))

Dias_fed=int(input("ingrese la duracion de la etapa productiva"))

Cargar_Procesos(Mol,Pasajes,Dias_fed)