"""A continuación se desarrollará la función que se utilizará 
para calcular los costos de producción de un proceso específico,
la idea es establecer una tarifa que aumentará en función de los días de proceso.

"""

def Calcular_costos_dias(expansion, productivo):
    costo_base_exp=1200
    costo_base_produ=3500
    
    dias_exp=sum(expansion)
    dias_produ=productivo
    
    if dias_exp>=1 and dias_exp<=3:
        costo_exp=costo_base_exp +(dias_exp*300)
    elif dias_exp > 4 and dias_exp <=8:
        costo_exp=costo_base_exp +(dias_exp*400)
    elif dias_exp > 8 and dias_exp <=12:
        costo_exp=costo_base_exp +(dias_exp*700)
    elif dias_exp > 12:
        costo_exp=costo_base_exp +(dias_exp*900)   
    
    if dias_produ>=1 and dias_produ<=4:
        costo_produ= costo_base_produ +(dias_produ*700)
    elif dias_produ	>4 and dias_produ <=6:
        costo_produ= costo_base_produ +(dias_produ*900)
    elif dias_produ	>6 and dias_produ <=9:
        costo_produ= costo_base_produ +(dias_produ*1200)       
    elif dias_produ	>9 and dias_produ <=12:
        costo_produ= costo_base_produ +(dias_produ*1500)
    elif dias_produ	>12:
        costo_produ= costo_base_produ +(dias_produ*2000)    
        
    return costo_exp, costo_produ


############################# código ppal######################################


dias_etapas_espansivas=[6,3,3]

dias_etapa_productiva=8

Costo_Expansiva, Costo_productiva=Calcular_costos_dias(dias_etapas_espansivas,dias_etapa_productiva)
Costo_Total=Costo_productiva+Costo_Expansiva

print(f"\nEl costo de produción de la etapa expansiva es de ........................${Costo_Expansiva}\nEl costo de producción de la etapa productiva es de.......................${Costo_productiva}\nSiendo el costo total de producción de la molécula........................${Costo_Total}")

