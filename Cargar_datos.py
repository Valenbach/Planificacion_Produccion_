import json

def cargar_datos(molecula, exp, produ):
    # Intentamos cargar el archivo si existe, o inicializamos una lista vacía si no
    try:
        with open("procesos.json", "r") as procesos:
            data = json.load(procesos)
    except (IOError, json.JSONDecodeError):
        data = []  # Si el archivo está vacío o no existe, inicializamos una lista vacía

    # Agregamos el nuevo proceso a la lista de procesos
    nuevo_proceso = {"nombre": molecula, "dias expansion": exp, "dias produ": produ}
    data.append(nuevo_proceso)

    # Escribimos la lista actualizada de procesos en el archivo JSON
    with open("procesos.json", "w") as procesos:
        json.dump(data, procesos, indent=4)
        
def obtener_datos_por_molecula(nombre_molecula):
    try:
        with open("procesos.json", "r") as procesos:
            data = json.load(procesos)
    except (IOError, json.JSONDecodeError):
        return f"No se han guardado procesos aún."

    # Buscar la molécula en los datos cargados
    for proceso in data:
        if proceso["nombre"].lower() == nombre_molecula.lower():
            return proceso
    return "Molécula no encontrada."

### Función principal ############
while True:
    print("1. Cargar datos")
    print("2. Obtener datos de una molécula")
    print("3. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        mol = input("Ingrese el nombre del proceso: ")
        pasajes = int(input("Ingrese la cantidad de pasajes: "))
        dias_fed = int(input("Ingrese la duración de la etapa productiva: "))
        cargar_datos(mol, pasajes, dias_fed)
        print("Se cargaron los datos de manera exitosa.")
        
    elif opcion == "2":
        nombre_molecula = input("Ingrese el nombre de la molécula para obtener los datos: ")
        datos_molecula = obtener_datos_por_molecula(nombre_molecula)
        print(datos_molecula)
        
    elif opcion == "3":
        break
    else:
        print("Opción no válida. Intente de nuevo.")




        