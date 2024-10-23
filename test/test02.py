# test_años_cumplidos.py

import pytest
from años_cumplidos import mostrar_años_cumplidos

def test_mostrar_años_cumplidos():
    assert mostrar_años_cumplidos(5) == [1, 2, 3, 4, 5]
    assert mostrar_años_cumplidos(0) == []         
    assert mostrar_años_cumplidos(1) == [1]        
    assert mostrar_años_cumplidos(3) == [1, 2, 3]
