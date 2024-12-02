import json
import os
from Planificacion_archivos import (
    listaVCDtarget,
    calcularVolFinalPasajes,
    calcularMedioExp,
    cargar_datos,
    solicitar_valor_positivo,
    calcular_costos,
    calGlucConsumida,
    calcular_volumen_acumulado,
)

# Prueba para listaVCDtarget
def test_listaVCDtarget_valores_validos(monkeypatch):
    """
    Prueba que listaVCDtarget retorne los valores correctos cuando las entradas son válidas.
    """
    entradas = iter(["1.5", "2.0", "3.0"])
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))
    
    resultado = listaVCDtarget(3)
    esperado = [1.5, 2.0, 3.0]
    assert resultado == esperado, f"Error: Resultado inesperado {resultado}"

def test_listaVCDtarget_entrada_invalida(monkeypatch):
    """
    Prueba que listaVCDtarget maneje entradas inválidas correctamente.
    """
    entradas = iter(["invalido", "2.0"])
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))
    
    resultado = listaVCDtarget(1)
    esperado = [2.0]
    assert resultado == esperado

# Prueba para calcularVolFinalPasajes
def test_calcularVolFinalPasajes():
    """
    Prueba que calcularVolFinalPasajes calcule correctamente el volumen final de los pasajes.
    """
    resultado = calcularVolFinalPasajes(1.0, [2.0, 3.0], 2, 100)
    esperado = [50.0, 33.333333333333336]
    assert resultado == esperado
    resultado_2= calcularVolFinalPasajes(2.0, [1.0,2.0], 2, 20)
    esperado_2=[40.0, 20.0]
    assert resultado_2==esperado_2

# Prueba para calcularMedioExp
def test_calcularMedioExp():
    """
    Prueba que calcularMedioExp calcule correctamente el volumen de medio de expansión total.
    """
    resultado = calcularMedioExp([50.0, 33.333333333333336], 100)
    esperado = 183.33333333333334
    assert resultado == esperado
    
from Planificacion_archivos import calGlucConsumida
#Pruebas para calcular glucosa consumida

def test_calGlucConsumida_caso_simple():
    """
    Prueba básica con valores sencillos para verificar el cálculo correcto.
    """
    resultado = calGlucConsumida(100, 50, 0.04, [1, 2, 3], [1.2, 1.3, 1.4])
    esperado = [0.48, 0.78, 1.1199999999999999]
    assert resultado == esperado
    """
    Prueba donde todas las tasas de crecimiento son 0, lo que debería resultar en consumo 0.
    """    
    resultado = calGlucConsumida(100, 50, 0.04, [1, 2, 3], [0.0, 0.0, 0.0])
    esperado = [0.0, 0.0, 0.0]  # Sin crecimiento, no hay consumo
    assert resultado == esperado
    

def test_valor_positivo(monkeypatch):
    """
    Prueba que la función acepte un valor positivo correctamente.
    """
    entradas = iter(["5.5"])
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))
    
    resultado = solicitar_valor_positivo("Ingrese un valor positivo: ")
    assert resultado == 5.5
    """
    Prueba que la función rechace valores negativos y acepte uno positivo después.
    """
    entradas = iter(["-2", "3.0"])
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))
    
    resultado = solicitar_valor_positivo("Ingrese un valor positivo: ")
    assert resultado == 3.0
    """
    Prueba que la función maneje entradas inválidas y acepte un número válido después.
    """
    entradas = iter(["texto", "1.5"])
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))
    
    resultado = solicitar_valor_positivo("Ingrese un valor positivo: ")
    assert resultado == 1.5
    """
    Prueba que la función maneje correctamente entradas con comas como separadores decimales.
    """
    entradas = iter(["3,7"])
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))
    
    resultado = solicitar_valor_positivo("Ingrese un valor positivo: ")
    assert resultado == 3.7



