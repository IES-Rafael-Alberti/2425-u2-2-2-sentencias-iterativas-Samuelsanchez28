# test_cuenta_atras.py

import pytest
from cuenta_atras import cuenta_atras

def test_cuenta_atras():
    assert cuenta_atras(5) == [5, 4, 3, 2, 1, 0]
    assert cuenta_atras(0) == [0] 
    assert cuenta_atras(3) == [3, 2, 1, 0]

def test_cuenta_atras_numero_negativo():
    with pytest.raises(ValueError) as excinfo:
        cuenta_atras(-1)
    assert str(excinfo.value) == "El número debe ser entero y positivo."
