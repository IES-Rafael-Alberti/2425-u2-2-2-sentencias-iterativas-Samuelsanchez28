# test_impares_hasta_numero.py

import pytest
from impares_hasta_numero import obtener_impares_hasta

def test_obtener_impares_hasta():
    assert obtener_impares_hasta(10) == [1, 3, 5, 7, 9]  # Números impares hasta 10
    assert obtener_impares_hasta(1) == [1]                 # Números impares hasta 1
    assert obtener_impares_hasta(0) == []                  # Números impares hasta 0
    assert obtener_impares_hasta(5) == [1, 3, 5]           # Números impares hasta 5

def test_obtener_impares_hasta_numero_negativo():
    with pytest.raises(ValueError) as excinfo:
        obtener_impares_hasta(-1)
    assert str(excinfo.value) == "El número debe ser entero y positivo."
