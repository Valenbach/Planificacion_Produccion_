
from Planificacion_archivos import listaVCDtarget


def test_listaVCDtarget_valores_validos(monkeypatch):
    """
    Prueba que la función retorne una lista con los valores correctos cuando se ingresan entradas válidas.
    """
    # Simular entradas válidas
    entradas = iter(["1.5", "2.0", "3.0"])
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))
    
    resultado = listaVCDtarget(3)
    esperado = [1.5, 2.0, 3.0]
    assert resultado == esperado, f"Error: Resultado inesperado {resultado}"
    """
    Prueba que la función maneje correctamente una entrada no válida antes de recibir una válida.
    """
    # Simular una entrada inválida seguida de una válida
    entradas = iter(["invalido", "2.0"])
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))
    
    resultado = listaVCDtarget(1)
    esperado = [2.0]
    assert resultado == esperado, f"Error: Resultado inesperado {resultado}"

    """
    Prueba que la longitud de la lista sea igual a la cantidad de pasajes solicitados.
    """
    # Simular entradas válidas
    entradas = iter(["1.0", "2.0", "3.0", "4.0", "5.0"])
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))
    
    resultado = listaVCDtarget(5)
    assert len(resultado) == 5, f"Error: Longitud inesperada {len(resultado)}"